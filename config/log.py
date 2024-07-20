import logging


def init():
    # 配置日志
    logging.basicConfig(
        level=logging.WARN,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
