import copy
import csv
import io
import json


def read_csv(fileOrText: str=None) -> list:
    if fileOrText.endswith(".csv"):
        with open(fileOrText, "r", encoding="UTF-8", newline="") as f:
            reader = csv.DictReader(f)
            return [r for r in reader]
    else:
        f = io.StringIO()
        f.write(fileOrText)
        f.seek(0)
        reader = csv.DictReader(f)
        reader.fieldnames = fileOrText.split("\n")[0].split(",")
        d = [r for r in reader][1:]
        f.close()
    return d

# jsonに変換
def csv_to_json(data, default_key="object") -> dict:
    def castInt(x):
        x = copy.copy(x)
        for k, v in x.items():
            try: x[k] = int(v)
            except ValueError: pass
        return x
    d = dict()
    d[default_key] = list(map(castInt, read_csv(data)))
    return json.loads(json.dumps(d))


# csvに変換
def json_to_csv(data, csvfile=None) -> str:
    def write(fp, fieldnames):
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        for dat in data:
            writer.writerow(dat)
        return writer

    data = data[list(data.keys())[0]]
    if len(data) <= 0: return
    fieldnames = list(data[0].keys())

    f = io.StringIO()
    f.seek(0)
    write(f, fieldnames)
    d = f.getvalue()
    f.close()
    if csvfile is None:
        return d

    with open(csvfile, "w", encoding="UTF-8", newline="") as fp:
        write(fp, fieldnames)
    return d


if __name__ == "__main__":
    csv_ = read_csv("""name,a,b
alice,2,3
bob,2,3""")
    print(json_to_csv(csv_))
    # csv_path = r"D:\myscript\games\cui\textbasedrpg\text.csv"
    # messages = csv_to_json(csv_path)

    # def find_text(text_id, using_lang):
    #     for message in messages.get("object"):
    #         if message.get("text_id") == text_id:
    #             return message.get(using_lang)
    #     return

    # text_id = "update"
    # using_lang = "en"
    # print(find_text(text_id, using_lang))