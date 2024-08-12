from functions.GET_TODO import get_todos
from functions.WRITE_TODO import write_todos
import FreeSimpleGUI as sg
import time


sg.theme('Black')
clock=sg.Text('',key='clock')
label=sg.Text("Type in a to-do.")
input_box=sg.InputText(tooltip='Enter to-do',key='todo')
add_button=sg.Button(button_text="Add")
todos_list=sg.Listbox(values=get_todos(),
                      key='todos', enable_events=True , size=(45,10))
edit_button=sg.Button(button_text="Edit")
delete_button=sg.Button(button_text='Delete')
button_exit=sg.Button(button_text='Exit')


window=sg.Window("MY-TODO-APP",
                 layout=[[clock],[label],[input_box,add_button],
                         [todos_list,edit_button,delete_button],
                         [button_exit]],
                 font=('Haventica',20))

while True:
    event,values=window.read(timeout=200)
    window['clock'].update(value=time.strftime("%b %d ,%Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case 'Add':
            todos=get_todos()
            new_todo=values['todo']+'\n'
            todos.append(new_todo)
            write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                old_todo=values['todos'][0]
                new_todo=values['todo']+'\n'
                todos=get_todos()
                old_todo_index=todos.index(old_todo)
                todos[old_todo_index]=new_todo
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please Select a todo first!')
        case 'Delete':
            try:
                todo_to_delete=values['todos'][0]
                todos=get_todos()
                todo_to_delete_index=todos.index(todo_to_delete)
                todos.pop(todo_to_delete_index)
                write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please Select a todo first!')
        case 'Exit':
            exit()
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break


window.close()
