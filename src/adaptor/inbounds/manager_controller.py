import fastapi

router = fastapi.APIRouter()


@router.get("/list")
def list_black_host():
    with open("black.txt", "r") as file:
        return [item.strip() for item in file.readlines() if item.strip()]


@router.get("/delete")
def delete_item(index: int):
    with open("black.txt", "r") as file:
        items = [item.strip() for item in file.readlines() if item.strip()]
        del items[index]

    with open("black.txt", "w") as file:
        for item in items:
            file.write(item + "\n")

    return "ok"


@router.get("/add")
def add_item(host: str):
    with open("black.txt", "a") as file:
        file.write(host + "\n")
    return "ok"
