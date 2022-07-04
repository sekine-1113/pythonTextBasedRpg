import PySimpleGUI as sg



class EventHandlers:
    Update = "-update-"
    Write = "-write-"
    Exit = "-exit-"

layout = [
    [sg.T("Hello!"), sg.T("", size=(20, 1), key="-name-")],
    [sg.T("Input your name: "), sg.I(key="-nameinput-")],
    [sg.T("Your selection Folder: "), sg.T("", size=(30, 1), key="-folder-"), sg.FolderBrowse(key="-selectionFolder-")],
    [sg.Button("Update", key=EventHandlers.Update), sg.Button("Write", key=EventHandlers.Write)]
]

window = sg.Window("Notitle", layout)


def update_event(values):
    window["-name-"].update(values["-nameinput-"])
    window["-folder-"].update(values["-selectionFolder-"])

def write_event(values):
    print("Write,", values["-nameinput-"], values["-selectionFolder-"])


event_handler = {
    EventHandlers.Update: update_event,
    EventHandlers.Write: write_event,
    EventHandlers.Exit: lambda: print("Exit")
}
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    event_handler.get(event)(values)


window.close()

