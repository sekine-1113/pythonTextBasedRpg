import copy
import csv
import json
import io


def read_csv(file=None):
    if file.endswith(".csv"):
        with open(file, "r", newline="") as f:
            reader = csv.DictReader(f)
            return [r for r in reader]
    else:
        f = io.StringIO()
        f.write(file)
        f.seek(0)
        reader = csv.DictReader(f)
    return [r for r in reader]

def castInt(x):
    x = copy.copy(x)
    for k,v in x.items():
        try:
            x[k] = int(v)
        except ValueError:
            pass
    return x

def csv_to_json(data, default_key="object"):
    d = {}
    d[default_key] = list(
        map(
            castInt,
            read_csv(data)
        )
    )
    return json.loads(json.dumps(d))

def json_to_csv(csvfile, data):
    data = data[list(data.keys())[0]]
    fieldnames = list(data[0].keys())
    with open(csvfile, "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        for dat in data:
            writer.writerow(dat)

data = """name,age
Alice,20
Bob,21"""
j1=csv_to_json(data)
print(j1)
json_to_csv("test.out.csv", j1)
j2=csv_to_json("test.out.csv")
print(j2)