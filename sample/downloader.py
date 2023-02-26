import os
import zipfile
from pathlib import Path

import requests


def download_zip(zip_url: str, save_filepath: Path|str) -> None:
    """zipフォルダをダウンロードする.
    url: zipフォルダのurl
    save_filepath: zipフォルダのフォルダ名
    """
    res = requests.get(zip_url)
    with open(save_filepath, "wb") as f:
        f.write(res.content)


def unpack_zip(filepath: Path|str, unpacked_filepath: Path|str):
    """ zipフォルダを解凍する.
    filepath: Zipフォルダ
    unpacked_filepath: 解凍後Zipフォルダ
    """
    with zipfile.ZipFile(filepath) as f:
        f.extractall(unpacked_filepath)


