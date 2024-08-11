from functions.GET_TODO import get_todos
from functions.WRITE_TODO import write_todos
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do.")
input_box=sg.InputText(tooltip='Enter to-do')
add_button=sg.Button(button_text="Add")

window=sg.Window("MY-TODO-APP",layout=[[label],[input_box,add_button]])
window.read()
window.close()
