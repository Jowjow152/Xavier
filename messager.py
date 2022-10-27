import time
from tkinter import LEFT
import PySimpleGUI as sg
import socket
import threading
import json
import keyboard

class MessagerUI:

    HOST, PORT = "localhost", 1234

    def __init__(self, userId, username):

        self.userId = userId
        self.username = username

        layoutColumn1 = [[sg.Column([],size=(1000,500),key='-MESSAGES-',element_justification=LEFT,scrollable=True,vertical_scroll_only=True)],
                        [sg.Input(key='-TEXT-',size=(80,20),font=(16),expand_x=True),sg.Button('Enviar',size=(20,1),font=(12))]
                        ]

        layoutFrame2 = [[sg.Text('Chats')]]

        layout = [[sg.Column(layoutFrame2,vertical_alignment='top'),sg.Column( layoutColumn1)]]

        self.window = sg.Window('Mensagens', layout, finalize=True)

        self.s = socket.socket() 
        self.s.connect((self.HOST, self.PORT))
        thread_recieve = threading.Thread(target=self.recieveMessage)
        thread_recieve.daemon = True
        thread_recieve.start()

        keyboard.add_hotkey('enter', lambda: self.sendMessage())

        while True:
            event, values = self.window.read()
            if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes self.window or clicks cancel
                self.closeConnection()
                break 
            elif event == 'Enviar':
                
                self.sendMessage()

    def sendMessage(self):
        text = self.window['-TEXT-'].get()
        text = text.strip()
        if text != '':
            message = {
                "text": text,
                "username": self.username,
                "userId": self.userId,
                "date": time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            }
            message = json.dumps(message)
            self.s.sendall(bytes(message, "utf-8"))

    def recieveMessage(self):
        try:
            while True:
                msg = json.loads(self.s.recv(1024))
                self.window.extend_layout(self.window['-MESSAGES-'], [[sg.Text(f'{msg["username"]}',text_color='#FFFFFF'), sg.Text(f'({msg["date"]})',text_color='#BDC3CB')],[sg.Text(f'{msg["text"]}')]])
                self.window['-MESSAGES-'].contents_changed()
                self.window['-MESSAGES-'].Widget.canvas.yview_moveto(1.0) 
                self.window['-TEXT-'].update('')
        except:
            return


    def closeConnection(self):
        self.s.sendall(bytes("exit()", "utf-8"))
        self.s.close()


    
if __name__ == "__main__":
    MessagerUI(2,"Anonimo")
        