from games.cui.textbasedrpg.util.gentoken import create_id, create_token, create_random_password, get_password
import PySimpleGUI as sg


class UserAccount:
    def __init__(self) -> None:
        pass

    def set_accounts(self):
        pass

    def set_identifier(self, _id):
        self._id = _id

    def set_password(self, _password):
        self._password = _password

user = {
    "idx": 0,
    "name": "aliec",
    "id": "fgrarea",
    "password": "fwahigw",
    "created_at": "2022/9/7 13:22"
}

class Actor:
    def __init__(self) -> None:
        pass


def gui():
    layout = [
        [sg.T("アカウント登録します")],
        [sg.T("ユーザー名"), sg.I(key="-name-")],
        [sg.T("パスワード"), sg.I(key="-pass-", disabled=True), sg.B("自動生成")],
        [sg.B("登録")]
    ]

    window = sg.Window("アカウント登録", layout)
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        if event == "登録":
            print(values["-name-"])
            print(values["-pass-"])
            text = values["-name-"] + "\n" + values["-pass-"]
            sg.popup(text+"\n登録しました。")
            break

        if event == "自動生成":
            window["-pass-"].update(create_random_password()[0])
    window.close()

if __name__ == "__main__":
    user_account: UserAccount = UserAccount()

    gui()
