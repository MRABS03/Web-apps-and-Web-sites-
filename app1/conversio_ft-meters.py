import FreeSimpleGUI as sg

feet_text=sg.Text("Enter feet: ")
inches_text=sg.Text("Enter inches: ")
feet_input=sg.InputText(tooltip='feet',key='ft')
inches_input=sg.InputText(tooltip='inches',key='in')

conv_button=sg.Button(button_text="Convert")
Answer=sg.Text('',key='ans')

def conv(ft,inch):
    return f"{ft*0.3048+inch*0.0254} m"

window=sg.Window('Conversion APP',
                 layout=[[feet_text,feet_input],[inches_text,inches_input],[conv_button,Answer]])
while True:
    command,values=window.read()
    match command:
        case 'Convert':
            window['ans'].update(value=conv(ft=float(values['ft']),inch=float(values['in'])))
        case sg.WIN_CLOSED:
            break


