from functions.GET_TODO import filepath

filepath = fr'..\files\todo.txt'


def write_todos(task):
    with open(filepath, "w") as file:
        file.writelines(task)
