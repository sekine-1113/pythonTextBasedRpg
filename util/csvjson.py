import csv
import io
from pathlib import Path

from pprint import pprint


def _make_json(csv_data: list[dict[str, str]]) -> list[dict[str, str|int]]:
    # data: dict[str, str]
    # inner: dict[str, str|int]
    # key: str
    # value: str
    # json_obj: list = []
    json_obj = list()
    for data in csv_data:
        inner = dict()
        for key, value in data.items():
            inner[key] = int(value) if value.isdecimal() else value
        json_obj.append(inner)

    return json_obj


def read_string(csv_string: str) -> list[dict[str, str|int]]:
    """
    文字列からCSVを読み込み辞書型のデータのリストを返却する.
    """

    if not isinstance(csv_string, str):
        raise TypeError

    f: io.StringIO
    reader: csv.DictReader
    data: list[dict[str, str]]
    with io.StringIO() as f:
        f.write(csv_string)
        f.seek(0)
        reader = csv.DictReader(f)
        data = [row for row in reader]

    return _make_json(data)


def read_file(csv_file: Path|str) -> list[dict[str, str|int]]:
    """
    ファイルからCSVを読み込み辞書型のデータのリストを返却する.
    """

    if not isinstance(csv_file, Path|str):
        raise TypeError

    file: Path = Path(csv_file) if isinstance(csv_file, str) else csv_file

    if not file.exists():
        raise FileNotFoundError

    reader: csv.DictReader
    data: list[dict[str, str]]
    with open(file, "r", encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    return _make_json(data)


def _stringify(__obj: str|int|None) -> str:
    if __obj is None:
        return "None"
    return str(__obj) if not isinstance(__obj, str) else __obj


def jsonize(__obj: list[dict[str, str|int]]) -> list[dict[str, str]]:
    inner: dict[str, str|int]
    key: str
    value: str|int
    list_: list[dict[str, str]] = []
    __inner: dict[str, str]
    for inner in __obj:
        __inner = {}
        for key, value in inner.items():
            __inner[key] = _stringify(value)
        list_.append(__inner)
    return list_


def json2csv(__obj: list[dict[str, str|int]]) -> str:
    """
    jsonからcsv文字列に変換する

    入力\n
    `[{"key": "value1", ...}, ..., {"key": "valueN", ...}]`

    出力\n
    key,key2,...\n
    value,value2,...
    """

    fieldnames: list[str] = list(__obj[0].keys())

    f: io.StringIO
    writer: csv.DictWriter
    csv_string: str
    obj: list[dict[str, str]] = jsonize(__obj)

    with io.StringIO() as f:
        f.seek(0)
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(obj)
        csv_string = f.getvalue()
    return csv_string.replace("\r", "").removesuffix("\n")


if __name__ == "__main__":
    file: str = r"D:\myscript\games\cui\textbasedrpg\datastore\text.csv"
    csv_text: str = ""

    with open(file, "r", encoding="UTF-8") as f:
        csv_text = f.read()

    excepted_result: list[dict[str, str|int]] = [
        {
            'user_id': 0,
            'user_name': 'alice',
            'password': 'passw0rd',
            'comment': 'none'
        },
        {
            'user_id': 1,
            'user_name': 'bob',
            'password': 'bob1218',
            'comment': 'none'
        }
    ]

    csv_object: list[dict[str, str|int]] = read_string(csv_text)

    assert excepted_result == csv_object

    csv_object_from_file: list[dict[str, str|int]] = read_file(file)
    assert excepted_result == csv_object_from_file

    assert csv_text == json2csv(csv_object)
    assert csv_text == json2csv(csv_object_from_file)

    print("======= CSV text =======")
    print(csv_text)
    print("======= CSV to JSON =======")
    pprint(csv_object, width=32, sort_dicts=False)
