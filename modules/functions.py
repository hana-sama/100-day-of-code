FILEPATH ="todos.txt"

def get_data_from_todos_file(filepath=FILEPATH):
    """ Read a text file and return the list of todo items

    Args:
        filepath (str, optional): _description_. Defaults to "todos.txt".

    Returns:
        list: todo items
    """
    try:
        with open(filepath, "r") as local_file:
            content = local_file.readlines()
            local_file.seek(0)
    except FileNotFoundError as e:
        with open(FILEPATH, "w") as file:
            pass
    finally:
        with open(filepath, "r") as local_file:
            content = local_file.readlines()
            local_file.seek(0)
    return content

def write_todos(filepath=FILEPATH, todos_args=None, mode="w"):
    """ Store input from user in a text file

    Args:
        filepath (str, optional): _description_. Defaults to "todos.txt".
        todos_args (_type_, optional): _description_. Defaults to None.
        mode (str, optional): _description_. Defaults to "w".
    """
    with open(filepath, mode) as local_file:
        local_file.writelines(todos_args)
        local_file.seek(0)


if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(text)