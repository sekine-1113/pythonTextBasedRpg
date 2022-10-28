import requests
import zipfile
import os


# zipインストール
def download_zip(url, save_filepath):
    res = requests.get(url)
    with open(save_filepath, "wb") as f:
        f.write(res.content)

# 解凍
def unpack_zip(filepath, unpacked_filepath):
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

