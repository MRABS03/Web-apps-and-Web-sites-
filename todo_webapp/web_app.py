import streamlit as st
from GET_TODO import get_todos
from WRITE_TODO import write_todos
todos=get_todos()
def add_todo():
    new_todoo=st.session_state['new_todo'] +'\n'
    todos.append(new_todoo)
    write_todos(todos)


st.title("Your TODO app")
st.subheader("You're all todos are listed here.")
st.text("This will help you streamline your day to day task!")


for index,todo in enumerate(todos):
    checkbox=st.checkbox(todo,key=f'todo_{index}')
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[f'todo_{index}']
        st.rerun()
st.text_input(label='',placeholder='Add new todo...',on_change=add_todo,key='new_todo')
