import json



class PyObjectEncoder(json.JSONEncoder):
    def default(self, o):
        if hasattr(o, "__dict__"):
            return o.__dict__
        return super().default(o)


def test_encoder():
    print(json.dumps({"a":"a"}, ensure_ascii=False, cls=PyObjectEncoder))


if __name__ == "__main__":
    test_encoder()

