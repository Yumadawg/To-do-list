#from functions import get_todos, write_todos
import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    action = input("Hello, please choose add, show, complete, edit or exit: ")
    action = action.strip()
    
    if action.startswith("add"):

        todo = action[4:]
        list_of_todos = functions.get_todos()
        list_of_todos.append(todo + "\n")
        functions.write_todos(list_of_todos)
    
        print(f'{todo} has been added')

    elif action.startswith("show"):

        list_of_todos = functions.get_todos()
        for index, item in enumerate(list_of_todos):
            itemer = item.strip("\n")
            print(f'{index + 1}.{itemer.capitalize()}')

    elif action.startswith("edit"):

        try:
            list_of_todos = functions.get_todos()
            number = int(action[5:])
            edit_case = input("Please edit to do: ")
            list_of_todos[number - 1] = edit_case + "\n"
            functions.write_todos(list_of_todos)

        except ValueError:
            print("Command is not valid")
            continue

    elif action.startswith("complete"):

        list_of_todos = functions.get_todos()
        number = int(action[9:])
        to_do_to_remove = list_of_todos[number - 1].strip('\n')
        list_of_todos.remove(list_of_todos[number - 1])

        print(f'Todo {to_do_to_remove} was removed from the list successfully')

        functions.write_todos(list_of_todos)

    elif action.startswith("clear"):

        list_of_todos = functions.get_todos()
        list_of_todos = []
        functions.write_todos(list_of_todos)

        print("The list has been cleared")

    elif action.startswith("exit"):
        break

    else:
        print("Command is not valid")
        continue

print("bye!")