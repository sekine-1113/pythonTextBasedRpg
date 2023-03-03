import csv
import io
from pathlib import Path


def _check_type(__obj, *types_) -> bool:
    return isinstance(__obj, types_)


def _make_json(csv_data):
    json_obj = []

    for data in csv_data:
        inner = {}
        for key, value in data.items():
            inner[key] = int(value) if value.isdecimal() else value
        json_obj.append(inner)

    return json_obj


def read_string(csv_string):
    """
    文字列からCSVを読み込み辞書型のデータのリストを返却する.
    """

    assert _check_type(csv_string, str)

    with io.StringIO() as f:
        f.write(csv_string)
        f.seek(0)
        reader = csv.DictReader(f)
        data = [row for row in reader]

    return _make_json(data)


def read_file(csv_file):
    """
    ファイルからCSVを読み込み辞書型のデータのリストを返却する.
    """

    assert _check_type(csv_file, str, Path)

    file = Path(csv_file) if isinstance(csv_file, str) else csv_file
    if not file.exists():
        raise FileNotFoundError

    with open(file, "r", encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    return _make_json(data)


def _jsonize(__obj):
    list_ = []
    for inner in __obj:
        __inner = {}
        for key, value in inner.items():
            if not isinstance(value, str):
                value = str(value)
            __inner[key] = value
        list_.append(__inner)
    return list_


def json2csv(__obj):
    """
    jsonからcsv文字列に変換する

    入力\n
    `[{"key": "value1", ...}, ..., {"key": "valueN", ...}]`

    出力\n
    key,key2,...\n
    value,value2,...
    """

    fieldnames = list(__obj[0].keys())

    obj = _jsonize(__obj)

    with io.StringIO() as f:
        f.seek(0)
        writer = csv.DictWriter(f, fieldnames=fieldnames, doublequote=True, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(obj)
        csv_string = f.getvalue()

    return csv_string.replace("\r", "").removesuffix("\n")


if __name__ == "__main__":
    print(read_string("a,b,c\n0,0,0"))