import PySimpleGUI as sg


layout = [
    [sg.T("Hello!"), sg.T("", size=(20, 1), key="-name-")],
    [sg.T("Input your name: "), sg.I(key="-nameinput-")],
    [sg.Button("Yes")]
]

window = sg.Window("Notitle", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window["-name-"].update(values["-nameinput-"],text_color="red")

window.close()