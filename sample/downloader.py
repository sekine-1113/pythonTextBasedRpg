import os
import zipfile
from pathlib import Path

import requests


def download_zip(url: str, save_filepath: Path|str) -> None:
    """zipフォルダをダウンロードする.
    url: zipフォルダのurl
    save_filepath: zipフォルダのフォルダ名
    """
    res = requests.get(url)
    with open(save_filepath, "wb") as f:
        f.write(res.content)


def unpack_zip(filepath: Path|str , unpacked_filepath: Path|str):
    """ zipフォルダを解凍する.
    filepath: Zipフォルダ
    unpacked_filepath: 解凍後Zipフォルダ
    """
    with zipfile.ZipFile(filepath) as f:
        f.extractall(unpacked_filepath)



if False:
    URL = r"https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-large-zip-file.zip"
    res = requests.get(URL)
    with open("example.zip", "wb") as f:
        f.write(res.content)
    # ----- ^ download ---------
    # ----- ↓ unpack -----------
    with zipfile.ZipFile("example.zip") as f:
        f.extractall("example_zip_unpacks")

    os.remove("example_zip_unpacks")

