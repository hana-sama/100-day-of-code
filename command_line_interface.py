from modules import functions
import datetime

today = datetime.datetime.now()
string_format = today.strftime('%b, %d, %Y %H:%M:%S')
print("-"*20 + " Todo App " + "-"*20)
print(f"It is {string_format}")
print("Welcome to the Todo App!")



while True:
    user_action = input("Type 'add','show', 'edit', 'complete' or 'exit': ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = functions.get_data_from_todos_file()
        todos.append(f"{todo}\n")
        function.write_todos(todos_args=todos)
    elif user_action.startswith("show"):
        content = functions.get_data_from_todos_file()
        new_line_removed_content = [item.replace("\n", "") for item in content]
        for key, value in enumerate(new_line_removed_content):
            row = f"{key + 1} - {value}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5])
            number = number - 1
            new_todo = input("Enter a new todo: ")
            todos = functions.get_data_from_todos_file()
            todos[number] = f"{new_todo}\n"
    
            functions.write_todos(todos_args=todos)
        except (ValueError, IndexError) as e:
            print(e)
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9])
            number = number - 1
            todos = functions.get_data_from_todos_file()
            todos.pop(number)
            todos = "".join(todos)
            functions.write_todos(todos_args=todos)
        except (ValueError, IndexError) as e:
            print(e)
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("An invalid input. Please select from 'add', 'show', 'edit', 'complete' or 'exit'")
print("-"*20 + " Bye! " + "-"*20)

