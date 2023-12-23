import PySimpleGUI as sg
def create(todos_list, headings):
    display_layout = [
        [sg.Table(values=todos_list,
                  headings=headings,
                  max_col_width=300,
                  auto_size_columns=True,
                  display_row_numbers=True,
                  justification="left",
                  num_rows=10,
                  key='-TABLE-',
                  row_height=35)]
         ]
    
    todos_window = sg.Window("To-Do Display Window", display_layout, modal=True, font=("Helvetica", 15))

    while True:
        event, values = todos_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
    todos_window.close()