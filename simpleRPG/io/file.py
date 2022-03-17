from simpleRPG import (
    os,
    sys,
)
from simpleRPG.io import (
    json,
)


def get_path():
    return os.path.dirname(sys.argv[0])

def exists(path):
    return os.path.exists(path)


def load(path: str) -> object:
    with open(path, mode="r", encoding="UTF-8") as f:
        return json.load(f)

def dump(path: str, data):
    with open(path, mode="w", encoding="UTF-8") as f:
        json.dump(data, f)


if __name__ == "__main__":
    path = get_path()
    print(
        load(
            os.path.join(
                os.path.dirname(path),
                "data/sample.json"
            )
        )
    )
