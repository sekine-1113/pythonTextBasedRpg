from simpleRPG import (
    os,
    sys,
)
from simpleRPG.io import (
    json,
)


def get_path():
    return os.path.dirname(sys.argv[0])


def load(path: str) -> object:
    with open(path, mode="r", encoding="UTF-8") as f:
        return json.load(f)


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
