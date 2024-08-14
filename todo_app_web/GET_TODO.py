filepath= fr'..\files\todo.txt'


def get_todos():
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos
