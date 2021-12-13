import PySimpleGUI as sg

layout = [
    [sg.T("A:"), sg.I(key="-A-")],
    [sg.T("D:"), sg.I(key="-D-")],
    [sg.T("R:"), sg.I(key="-R-")],
    [sg.T("H:"), sg.I(key="-H-")],
    [sg.T(size=(55, 1), key="-out-")],
    [sg.B("Calc"), sg.B("Exit")]
]

window = sg.Window("Calc", layout)
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break

    attack_point = int(values["-A-"])
    defence_point = int(values["-D-"])
    r = int(values["-R-"])
    h = int(values["-H-"])

    expr = int(attack_point*4 / (defence_point*2) + r + h)
    window["-out-"].update(str(expr))

window.close()