
filepath = fr'D:\User\Documents\ML\Python Mega Course\todo_app_web\todo.txt'


def write_todos(task):
    with open(filepath, "w") as file:
        file.writelines(task)
