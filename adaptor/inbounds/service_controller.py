import logging

import fastapi
import requests
import yaml
from starlette.responses import Response

router = fastapi.APIRouter()


@router.get("/")
def root(url: str, host: list[str] = fastapi.Query(None)):
    url = encrypt_request_url(url, host)
    logging.info(f"actually execute request utl: {url}")
    response_data = decrypt_response(requests.get(url).text, host)
    response_data = enhance_yaml(response_data)
    return Response(content=response_data, media_type="text/html")


def encrypt_request_url(url: str, host: list[str]) -> str:
    encrypt_map, _ = generate_host_map(host)
    for k, v in encrypt_map.items():
        url = url.replace(k, v)
    return url


def decrypt_response(response_data: str, host: list[str]) -> str:
    _, decrypt_map = generate_host_map(host)
    for k, v in decrypt_map.items():
        response_data = response_data.replace(k, v)
    return response_data


def generate_host_map(host: list[str]) -> tuple[dict[str, str], dict[str, str]]:
    encrypt_map = {}
    decrypt_map = {}

    for i, e in enumerate(host):
        encrypt_str = f"www.encode{i}.url"
        encrypt_map[e] = encrypt_str
        decrypt_map[encrypt_str] = e

    return encrypt_map, decrypt_map


def enhance_yaml(response_data):
    data = yaml.safe_load(response_data)

    with open("black.txt", "r") as file:
        [data["rules"].insert(0, f"DOMAIN-SUFFIX,{item.strip()},🚀 节点选择") for item in file.readlines() if
         item.strip()]

    return yaml.safe_dump(data)
