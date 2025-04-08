def get_todos(filepath = "files/todos.txt"):
    """Gets the todos from the file."""
    with open(filepath, "r") as file_local:
        list_of_todos_local = file_local.readlines()
    return list_of_todos_local


def write_todos(todos_for_write, filepath = "files/todos.txt"):
    """Writes the new todos to the file."""
    with open("files/todos.txt", "w") as file:
        file.writelines(todos_for_write)

if __name__ == "__main__":
    print(get_todos())