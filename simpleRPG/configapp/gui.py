import PySimpleGUI as sg


layout = [
    [sg.T("Hello!"), sg.T("", size=(20, 1), key="-name-")],
    [sg.T("Input your name: "), sg.I(key="-nameinput-")],
    [sg.T("Your selection Folder: "), sg.T("", size=(30, 1), key="-folder-")],
    [sg.FolderBrowse(key="-selectionFolder-")],
    [sg.Button("Update", key="-update-"), sg.Button("Write", key="-write-")]
]

window = sg.Window("Notitle", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    window["-name-"].update(values["-nameinput-"])
    window["-folder-"].update(values["-selectionFolder-"])
    print(values)
    if event == "-write-":
        print("Write,", values["-nameinput-"], values["-selectionFolder-"])
        sg.Popup("Write a cui.")

window.close()

