filepath= fr'D:\User\Documents\ML\Python Mega Course\todo_webapp\todo.txt'


def get_todos():
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos
