from modules import functions
import PySimpleGUI as sg
import os
import datetime
import todos_window
working_directory = os.getcwd()

sg.theme("Dark Brown")

todos_list = []
headings = ['TO-DO']

def make_main_window():
    main_layout = [
        [sg.Text("", key="-CLOCK-")],
        [sg.Text("Type in a to-do to add, new to-do to edit or select to-do to complete")],
        [sg.InputText(tooltip="Enter a todo", key="-TODO-"), sg.Button("Add")],
        [sg.Listbox(values=[item.replace("\n", "") for item in functions.get_data_from_todos_file()], key="-TODOS-", enable_events=True, size=[45, 10]), sg.Button("Edit")],
        [sg.InputText(tooltip="Choose a file", key="-FILE_PATH-"), sg.FileBrowse(initial_folder=working_directory, file_types=[("TEXT Files", "*.txt")])],
        [sg.Button("Submit"), sg.Button("Show Todos"), sg.Button("Complete"), sg.Button("Exit")]
        ]
    return sg.Window("To_Do App", main_layout, finalize=True, font=("Helvetica", 20))

window = make_main_window()
while True:
    event, values = window.read(timeout=2000)
    window["-CLOCK-"].update(value=datetime.datetime.now().strftime("%b %d, %Y %H:%M:%S"))
    if event in (sg.WIN_CLOSED, "Exit"):
        break
    elif event == "Add":
        window["-TODO-"].Update("")
        todos = functions.get_data_from_todos_file()
        new_todo = f"{values["-TODO-"]}\n"
        todos.append(new_todo)
        functions.write_todos(todos_args=todos)
        todos_list = [item.replace("\n", "") for item in todos]
        window["-TODOS-"].update(values=todos_list)
    elif event == "Submit":
        window["-FILE_PATH-"].Update("")
        filepath = values["-FILE_PATH-"]
        content = functions.get_data_from_todos_file(filepath)
        todos_list = [[item.replace("\n", "")] for item in content]
        print(todos_list)
    elif event == "Show Todos":
        todos_window.create(todos_list, headings)
    elif event == "Edit":
        try:
            todo_to_edit = values["-TODOS-"][0]
            new_todo = values["-TODO-"]
            todos = functions.get_data_from_todos_file()
            index = todos.index(todo_to_edit + "\n")
            todos[index] = f"{new_todo}\n"
            functions.write_todos(todos_args=todos)
            todos_list = [item.replace("\n", "") for item in todos]
            window["-TODO-"].Update("")
            window["-TODOS-"].update(values=todos_list)
        except IndexError as e:
            sg.popup("Please select an item to edit first.", font=("Helvetica", 20))
    elif event == "-TODOS-":
        window["-TODO-"].update(value=values["-TODOS-"][0])
    elif event == "Complete":
        try:
            todo_completed = values["-TODOS-"][0]
            todos = functions.get_data_from_todos_file()
            index = todos.index(todo_completed)
            todos.pop(index)
            functions.write_todos(todos_args=todos)
            todos_list = [item.replace("\n", "") for item in todos]
            window["-TODOS-"].update(values=todos_list)
            window["-TODO-"].Update("")
        except (ValueError, IndexError) as e:
            sg.popup("Please select an item to remove first.", font=("Helvetica", 20))

window.close()