import copy
import csv
import io
import json
from pathlib import Path



def loads(text, rtype=dict, skip_header=True):
    f = io.StringIO()
    f.write(text)
    f.seek(0)
    if rtype == dict:
        reader = csv.DictReader(f)
        reader.fieldnames = text.split("\n")[0].split(",")
        d = [rt for rt in reader][skip_header:]
    else:
        reader = csv.reader(f)
        d = [rt for rt in reader]
    f.close()
    return d

def load(file, rtype=dict, skip_header=False):
    if isinstance(file, str):
        file = Path(file)
        if not file.exists():
            raise FileNotFoundError
    elif isinstance(file, Path):
        if not file.exists():
            raise FileNotFoundError
    else:
        raise TypeError(f"current file type is {type(file)}, but except 'str' or 'Path' object.")
    with open(file, "r", encoding="UTF-8") as f:
        if rtype == dict:
            reader = csv.DictReader(f)
            d = [rt for rt in reader]
        else:
            reader = csv.reader(f)
            d = [rt for rt in reader][skip_header:]
    return d

def to_csv(data):
    f = io.StringIO()
    f.seek(0)
    row = ",".join(data["object"][0].keys()) + "\n"
    for value in data["object"]:
        row += ",".join(value.values()) + "\n"
    f.write(row)
    csv_object = f.getvalue()
    f.close()

    return csv_object


def to_json(data, default_key="object"):
    def castInt(x):
        x = copy.copy(x)
        for key, value in x.items():
            try:
                x[key] = int(value)
            except ValueError:
                pass
        return x
    json_object = dict()
    json_object[default_key] = list(map(castInt, data))
    return json.loads(json.dumps(json_object))

if __name__ == "__main__":
    csv_object = loads("""name,age\nalice,20""")

    file = r"D:\myscript\games\cui\textbasedrpg\datastore\text.csv"
    csv_object_from_file = load(file)

    print(to_csv(to_json(csv_object_from_file)))

