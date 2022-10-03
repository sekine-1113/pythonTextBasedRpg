import requests
import zipfile
import os




if False:
    URL = r"https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-large-zip-file.zip"
    res = requests.get(URL)
    with open("example.zip", "wb") as f:
        f.write(res.content)
    # ----- ^ download ---------
    # ----- ↓ unpack -----------
    with zipfile.ZipFile("example.zip") as f:
        f.extractall("example_zip_unpacks")

    os.remove("")

