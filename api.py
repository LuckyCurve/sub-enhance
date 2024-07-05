import logging

import yaml
import fastapi
import requests
from fastapi.responses import Response
from starlette.requests import Request

auth_str = "sadfglkrtjhioerfgsdfsdfg"

app = fastapi.FastAPI()

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


@app.middleware("http")
async def dispatch(request: Request, call_next) -> Response:
    auth = request.query_params.get("auth")

    if auth == auth_str:
        return await call_next(request)
    else:
        return Response("auth failed!", status_code=401)


@app.get("/")
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
        for line in file.readlines():
            if line.strip():
                data["rules"].insert(0, f"DOMAIN-SUFFIX,{line.strip()},🚀 节点选择")

    return yaml.safe_dump(data)
