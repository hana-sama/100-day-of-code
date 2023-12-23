class TodoApp:
    def __init__(self, filename):
        self.filename = filename

    def add(self, todo):
        with open(self.filename, "a") as todos_file:
            todos_file.write(f"{todo}\n")

    def show(self):
        with open(self.filename, "r") as todos_file:
            content = todos_file.readlines()
            new_line_removed_content = [item.replace("\n", "") for item in content]
            for key, value in enumerate(new_line_removed_content):
                print(f"{key + 1} - {value}")

    def edit(self, number, new_todo):
        with open(self.filename, "r") as todos_file:
            content = todos_file.readlines()
            content[number - 1] = f"{new_todo}\n"
            with open(self.filename, "w") as todos_file:
                todos_file.writelines(content)

    def complete(self, number):
        with open(self.filename, "r") as todos_file:
            content = todos_file.readlines()
            content.pop(number - 1)
            with open(self.filename, "w") as todos_file:
                todos_file.writelines(content)

def main():
    app = TodoApp("todos.txt")
    actions = {'add': app.add, 'show': app.show, 'edit': app.edit, 'complete': app.complete}

    while True:
        user_action = input("Type 'add', 'show', 'edit', 'complete' or 'exit': ").strip()
        if user_action in actions:
            if user_action == 'add':
                todo = input("Enter a new todo: ")


main()