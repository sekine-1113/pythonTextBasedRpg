import sys
import os

text = {
    "ja": {
        "some": "日本語です"
    },
    "en": {
        "some": "English"
    }
}

system = {
    "allow_lang": ["en", "ja"],
    "lang": "en",
    "auto_save": False,
    "root": os.path.dirname(sys.argv[0])
}



if __name__ == "__main__":
    lang = system["lang"]
    if lang in system["allow_lang"]:
        pass
    else:
        system["lang"] = "en"
    print(text[lang]["some"])