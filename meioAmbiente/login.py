from http.client import UnknownTransferEncoding
import PySimpleGUI as sg
import time
from messager import messagerUI

# username = sg.PopupGetText('Enter your username')
# password = sg.PopupGetText('Entery your password', password_char='*')

def login(user,password):
    if  password== 'admin':
        print("Logado com sucesso")
        window.close()
        messagerUI(user)
    else:
        print("Senha ou usuário incorretos")

layout = [[sg.Text('Usuário')],
          [sg.Input(key='-USER-')],
          [sg.Text('Senha')],
          [sg.Input(password_char='*',key='-PASSWORD-')],
          [sg.Button('Entrar',size=(10,1))]
         ]

window = sg.Window('Login', layout, finalize=True)
    
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        print(event)
        break
    elif event == 'Entrar':
        login(user=values['-USER-'],password=values['-PASSWORD-'])
