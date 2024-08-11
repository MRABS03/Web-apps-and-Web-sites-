from functions.GET_TODO import get_todos
from functions.WRITE_TODO import write_todos


while True:
    x=int(input("Add -> 1 ,Show ->2 ,Edit ->3 ,Complete ->4 ,Close ->0  \nEnter:"))
    match x:
        case 1:
            todo = input("Enter task to your todo.txt list: ") +'\n'
            todos= get_todos()
            todos.append(todo)
            write_todos(todos)

        case 2:
            todos= get_todos()
            for index,todo in enumerate(todos):
                todo=todo.strip()
                print(f"{index}-{todo}")
        case 3:
            todos= get_todos()
            for index,todo in enumerate(todos):
                todo=todo.strip()
                print(f"{index}-{todo}")


            index=int(input("Enter the index of TODO you want to edit: "))
            new_todo=input("Enter the task you want to replace it with: ")
            todos[index]=new_todo
            write_todos(todos)
        case 4:
            todos= get_todos()
            for index,todo in enumerate(todos):
                todo=todo.strip()
                print(f"{index}-{todo}")
            index = int(input("Enter the index of TODO you want to mark as complete: "))
            todos.pop((index))
            write_todos(todos)
        case 0:
            break
