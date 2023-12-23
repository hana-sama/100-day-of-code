import PySimpleGUI as sg
from unzip import unarchive


sg.theme("Black")

layout = [
    [sg.InputText("Select archive for unzip"), sg.FilesBrowse("Choose", key="-ZIP_FILE-")],
    [sg.InputText("Select destination folder"), sg.FolderBrowse("Choose", key="-FOLDER-")],
    [sg.Button("Unzip"), sg.Button("Exit"), sg.Text(key="-OUTPUT-", text_color="green")]
]

window = sg.Window("Archive Extractor", layout=layout)
while True:
    event, values = window.read()
    filepath = values["-ZIP_FILE-"]
    folder = values["-FOLDER-"]
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "Unzip":
        unarchive(filepath=filepath, dest_directory=folder)
        window["-OUTPUT-"].update(value="Unzip successed.")
window.close()