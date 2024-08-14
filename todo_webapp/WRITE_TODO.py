filepath = fr'D:\User\Documents\ML\Python Mega Course\todo_webapp\todo.txt'


def write_todos(task):
    with open(filepath, "w") as file:
        file.writelines(task)
