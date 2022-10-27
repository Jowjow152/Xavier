import PySimpleGUI as sg
from messager import MessagerUI
from sqlConnector import DbConnector

# username = sg.PopupGetText('Enter your username')
# password = sg.PopupGetText('Entery your password', password_char='*')

class Login:

    layout = [[sg.Text('Usuário')],
             [sg.Input(key='-USER-')],
             [sg.Text('Senha')],
             [sg.Input(password_char='*',key='-PASSWORD-')],
             [sg.Button('Entrar',size=(10,1))]
             ]

    window = sg.Window('Login', layout, finalize=True)

    conn = DbConnector()

    def __init__(self):
        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                print(event)
                break
            elif event == 'Entrar':
                self.login(username=values['-USER-'],password=values['-PASSWORD-'])

    def login(self,username,password):
        self.username = username
        self.password = password
        result = self.conn.searchUser(username)
        if result == None:
            print("Usuário não encontrado") 
        elif password == result[2]:
            self.window.close()
            MessagerUI(userId=result[0],username=result[1])
        else:
            print("Senha incorreta")

if __name__ == "__main__":
    Login()