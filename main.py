# import webbrowser
# # webbrowser.open("https://www.google.com")

class PostedItem:
    def __init__(self) -> None:
        self.item = []

    def recieve(self, item):
        self.item.append(item)

    def show_list(self):
        for item in self.item:
            print(item)

class User:
    def __init__(self, name, _id) -> None:
        self.name = name
        self._id = _id
        self.items = []

    def post(self, content, reply_from_id=None):
        pass

    def set_item(self, item):
        self.items.append(item)


class Questioner(User):
    def post(self, content, reply_from_id=None):
        item = Question(self._id, 0, content, "その他")
        self.set_item(item)
        print(f"内容「{item.content}」({item.category})を投稿しました。")
        return item

    def evaluate(self, ):
        pass


class Respondent(User):
    def post(self, content, reply_from_id=None):
        item = Answer(self._id, 0, content, reply_from_id)
        self.set_item(item)
        print(f"内容「{content}」を投稿しました。")
        return item


class Item:
    def __init__(self, user_id, item_id, content) -> None:
        self.user_id = user_id
        self.item_id = item_id
        self.content = content

    def __repr__(self) -> str:
        return self.content


class Question(Item):
    def __init__(self, user_id, item_id, content, category) -> None:
        super().__init__(user_id, item_id, content)
        self.category = category
        self.reply = None

    def set_reply(self, reply):
        self.reply = reply


class Answer(Item):
    def __init__(self, user_id, item_id, content, reply_from) -> None:
        super().__init__(user_id, item_id, content)
        self.evaluation = None
        self.reply_from = reply_from


if __name__ == "__main__":
    print("== アカウント作成 ==")
    q1 = Questioner("アリス", 0)
    q2 = Questioner("ボブ", 1)
    a1 = Respondent("学芸員A", 2)
    print("== データベース構築 ==")
    pi = PostedItem()

    print("== サービス開始 ==")
    pi.recieve(q1.post("だみー質問"))

    rp = a1.post("へんとう", pi.item[0].item_id)

    pi.item[0].set_reply(rp)
    pi.recieve(rp)