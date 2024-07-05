import urllib.parse


def enhance_proxy(data):
    with open("black.txt", "r") as file:
        for line in file.readlines():
            if line.strip():
                data["rules"].append(f"DOMAIN-SUFFIX,{line.strip()},🚀 节点选择")


def string_encode(data):
    return urllib.parse.quote(data)


if __name__ == '__main__':
    url = "https://url.v1.mk/sub?target=clash&url=hysteria2%3A%2F%2F8b896c56-3ccf-488e-bb70-d817f8d6c3ca%40www.luckycurve.space%3A31285%3Fpeer%3Dwww.luckycurve.space%26insecure%3D0%26sni%3Dwww.luckycurve.space%26alpn%3Dh3%238b896c56-singbox_hysteria2%7Chysteria2%3A%2F%2Fe3cc7fec-ccc9-4abb-a9b0-b7ae026105fb%40www.luckycurve.xyz%3A22933%3Fpeer%3Dwww.luckycurve.xyz%26insecure%3D0%26sni%3Dwww.luckycurve.xyz%26alpn%3Dh3%23e3cc7fec-singbox_hysteria2&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online_Mini_AdblockPlus.ini&emoji=true&list=false&xudp=false&udp=false&tfo=false&expand=true&scv=false&fdn=false&new_name=true"
    print(urllib.parse.quote(url))