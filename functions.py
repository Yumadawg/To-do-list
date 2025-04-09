FILE_PATH = "files/todos.txt"

def get_todos():
    """Gets the todos from the file."""
    with open(FILE_PATH, "r") as file_local:
        list_of_todos_local = file_local.readlines()
    return list_of_todos_local


def write_todos(todos_for_write):
    """Writes the new todos to the file."""
    with open(FILE_PATH, "w") as file:
        file.writelines(todos_for_write)


def refresh_list(widget):
    widget.clear()
    todos = get_todos()
    for item in todos:
        widget.addItem(item.strip())


if __name__ == "__main__":
    print(get_todos())