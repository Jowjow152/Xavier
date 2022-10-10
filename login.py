import PySimpleGUI as sg
import time

# username = sg.PopupGetText('Enter your username')
# password = sg.PopupGetText('Entery your password', password_char='*')

layout = [[sg.Text('Username'), sg.Input()],
          [sg.Text('Password'), sg.Input(password_char='*')],
          [sg.OK()]]

window = sg.Window('Login', layout, finalize=True)

while True:
    event, values = window.read()
    print(window.read())
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

