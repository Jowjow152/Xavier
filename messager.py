from tkinter import LEFT
import PySimpleGUI as sg
import time
import socketClient
import json

client = socketClient.socketClient()  

layoutColumn1 = [[sg.Column([],size=(1000,500),key='-MESSAGES-',element_justification=LEFT,background_color='red',scrollable=True,vertical_scroll_only=True)],
          [sg.Input(key='-TEXT-',size=(80,20),font=(16),expand_x=True),sg.Button('Enviar',size=(20,1),font=(12))]
          ]

layoutFrame2 = [[sg.Text('Chats')]
]

layout = [[sg.Column(layoutFrame2,vertical_alignment='top'),sg.Column( layoutColumn1)]]

window = sg.Window('Mensagens', layout, finalize=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        client.closeConnection()
        break 
    elif event == 'Enviar':
        message = {
            "text": values['-TEXT-'],
            "username" : "user1",
            "date" : time.strftime('%Y-%b-%d %H:%M:%S', time.localtime())
        }
        client.sendMessage(json.dumps(message))
        window.extend_layout(window['-MESSAGES-'], [[sg.Text('(' + time.strftime("%H:%M:%S", time.localtime()) + ') user 1: ' + values['-TEXT-'])]])
        window['-MESSAGES-'].contents_changed()
        window['-MESSAGES-'].Widget.canvas.yview_moveto(1.0)
        window['-TEXT-'].update('')
