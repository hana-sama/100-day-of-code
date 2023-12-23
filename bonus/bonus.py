import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="-FILES-")

label2 = sg.Text("Select desination folder: ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="-FOLDER-")

compress_button = sg.Button("Compress")
exit_buttin = sg.Button("Exit")
window = sg.Window("File Compressor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [compress_button, exit_buttin]])

while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["-FILES-"].split(";")
    folder = values["-FOLDER-"]
    make_archive(filepaths, folder)
    if event in (sg.WIN_CLOSED, "Exit"):
        break

window.close()