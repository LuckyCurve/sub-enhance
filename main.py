import urllib.parse


def enhance_proxy(data):
    with open("black.txt", "r") as file:
        for line in file.readlines():
            if line.strip():
                data["rules"].append(f"DOMAIN-SUFFIX,{line.strip()},🚀 节点选择")


def string_encode(data):
    return urllib.parse.quote(data)
