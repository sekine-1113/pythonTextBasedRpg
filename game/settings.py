
from datetime import datetime

class Mail:
    def __init__(self, title, content, time: datetime=None) -> None:
        self.title = title
        self.content = content
        self.time = time

    def view(self):
        date = self.time.today().date()
        date_ = f"{self.time.now().time().hour:02}:{self.time.now().time().minute:02}:{self.time.now().time().second:02}"
        time = f"{date} {date_}"
        return f"件名:{self.title}\n{self.content}\n{time}"

    def send(self, mailbox):
        mailbox.recieve(self)


class MailBox:
    def __init__(self) -> None:
        self.box = []

    def recieve(self, mail: Mail):
        self.box.append(mail)
        print("recieve ->\n", mail.view(), sep="")

    def find(self, title: str):
        for mail in self.box:
            if mail.title == title:
                return mail


mbox = MailBox()
mbox.recieve(Mail("テスト", "内容", datetime))

mail = mbox.find("テスト")
mail.send(mbox)
print(mail.view())

for m in mbox.box:
    print(m.view())