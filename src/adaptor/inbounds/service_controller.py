import logging

import fastapi
import requests
import yaml
from starlette.responses import Response

BLACK_URL_FILE_PATH = "black.txt"
router = fastapi.APIRouter()


@router.get("/")
def root(url: str, host: list[str] = fastapi.Query(None)) -> fastapi.responses.Response:
    """
    This function is the root endpoint of the API. It takes a URL and an optional list of hosts as parameters.
    The function encrypts the URL using the provided hosts, sends a GET request to the encrypted URL,
    decrypts the response data, enhances the YAML format of the response data, and returns the enhanced data as a response.

    Args:
        url (str): The original URL to be encrypted and sent as a request.
        host (list[str], optional): A list of hosts to be used for encryption and decryption. Defaults to None.

    Returns:
        fastapi.responses.Response: The enhanced response data in YAML format, use clash proxy
    """
    url = hide_actual_host(url, host)
    logging.info(f"actually execute request utl: {url}")
    response_data = replace_with_actual_host(requests.get(url).text, host)
    response_data = enhance_yaml(response_data, BLACK_URL_FILE_PATH)
    return Response(content=response_data, media_type="text/html")


def hide_actual_host(url: str, hosts: list[str]) -> str:
    encrypt_map = dict(
        (host, generate_encode_url_with_index(index))
        for (index, host) in enumerate(hosts)
    )
    for k, v in encrypt_map.items():
        url = url.replace(k, v)
    return url


def replace_with_actual_host(response_data: str, hosts: list[str]) -> str:
    decrypt_map = dict(
        (generate_encode_url_with_index(index), host)
        for (index, host) in enumerate(hosts)
    )
    for k, v in decrypt_map.items():
        response_data = response_data.replace(k, v)
    return response_data


def generate_encode_url_with_index(index: int) -> str:
    return f"www.encode{index}.com"


def enhance_yaml(response_data: str, file_path: str) -> str:
    data = yaml.safe_load(response_data)

    with open(file_path, "r") as file:
        [
            data["rules"].insert(0, f"DOMAIN-SUFFIX,{item.strip()},🚀 节点选择")
            for item in file.readlines()
            if item.strip()
        ]

    return yaml.safe_dump(data)
