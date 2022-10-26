import csv
import io
from pathlib import Path

from pprint import pprint

def _make_dictionary(csv_data):
    dictionary = []
    for data in csv_data:
        inner = {}
        for key, value in data.items():
            if value.isdecimal():
                value = int(value)
            inner[key] = value
        dictionary.append(inner)
    return dictionary


def read_string(string: str, skip_header: bool =True) -> list[dict[str, object]]:
    """
    文字列からCSVを読み込む.
    """
    f = io.StringIO()
    f.write(string)
    f.seek(0)
    reader = csv.DictReader(f)
    data = [row for row in reader]
    f.close()
    return _make_dictionary(data)

def read_file(file: Path|str) -> list[dict[str, object]]:
    """
    ファイルからCSVを読み込む.
    """
    if isinstance(file, str):
        file = Path(file)
    if not file.exists():
        raise FileNotFoundError

    with open(file, "r", encoding="UTF-8") as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return _make_dictionary(data)


def json2csv(obj: list[dict[str, object]]) -> str:
    """
    jsonからcsv文字列に変換する

    入力\n
    `[{"key": "value1", ...}, ..., {"key": "valueN", ...}]`

    出力\n
    key,key2,...\n
    value,value2,...
    """
    fieldnames = list(obj[0].keys())
    with io.StringIO() as f:
        f.seek(0)
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(obj)
        csv_string = f.getvalue()
    return csv_string.replace("\r", "").removesuffix("\n")

if __name__ == "__main__":
    file = r"D:\myscript\games\cui\textbasedrpg\datastore\text.csv"
    csv_text = ""
    with open(file, "r", encoding="UTF-8") as f:
        csv_text = f.read()

    excepted_result = [
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


    csv_object = read_string(csv_text)
    assert excepted_result == csv_object

    csv_object_from_file = read_file(file)
    assert excepted_result == csv_object_from_file

    assert csv_text == json2csv(csv_object)
    assert csv_text == json2csv(csv_object_from_file)
    print("======= CSV text =======")
    print(csv_text)
    print("======= CSV to JSON =======")
    pprint(csv_object, width=32, sort_dicts=False)