from pprint import pprint
print = pprint

import csv


def read_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            data_reader = csv.DictReader(f)
            data = [dict(row) for row in data_reader]
            for d in data:
                for k, v in d.items():
                    if v.isdecimal():
                        d[k] = int(v)
    except FileNotFoundError:
        raise Exception('File not found')
    return data


print(read_csv(r"D:\myscript\games\cui\textbasedrpg\datastore\text.csv"))