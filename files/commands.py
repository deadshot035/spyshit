import os
import pyautogui as pg
from time import sleep
from webbrowser import open
import tkinter as tk
from PIL import ImageTk
from random import randint
from time import time
class Command:
    def __init__(self) -> None:
        self.validKeys = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
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

    def _showMessage(self, msg:str):
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
    
    def _off(self, flicker=False):
        screen = tk.Tk()
        screen.attributes(topmost=True, fullscreen=True)
        screen.configure(background="#000000", cursor="none")
        dur = randint(2000, 3000)
        if flicker:
            dur = randint(20,60)
        screen.after(dur, lambda: screen.destroy())
        screen.mainloop()

    def executeCommand(self, command:str):
        print(command)
        if command == "shutdown":
            os.system("shutdown /s /t 0")
        
        elif command == "reboot":
            os.system("shutdown /r /t 0")
        
        elif command == "lock":
            os.system("rundll32.exe user32.dll, LockWorkStation")
        
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
        
        elif command == "caps":
            pg.press('capslock')

        elif command.startswith("open"):
            url = command.split("!")[1].strip()
            open(url)
        elif command.startswith("spam"):
            n = int(command.split("!")[0].removeprefix("spam"))
            url = command.split("!")[1].strip()
            for i in range(0, n):
                open(url)
        elif command.startswith("close"):
            n = int(command.split("!")[1])
            for i in range(0, n):
                pg.hotkey('ctrl', 'w')
        elif command == "refresh":
            pg.press('browserrefresh')
        elif command == "closetab":
            pg.hotkey('ctrl', 'w')
        
        elif command.startswith("ssfreeze"):
            try:
                dur = int(float(command.split("!")[1])*1000)
            except Exception as e:
                dur = 4000
            print(dur)
            screen = tk.Tk()
            screen.attributes(topmost=True, fullscreen=True)
            screen.configure(background="#000000", cursor="none")
            # pg.screenshot('ss.png')
            img = ImageTk.PhotoImage(pg.screenshot())
            imgPanel = tk.Label(screen, image=img)
            imgPanel.pack()
            screen.after(dur, lambda : screen.destroy())
            screen.mainloop()
         
        elif command == "savess":
            pg.screenshot('image.png')
        elif command == "removess":
            os.remove('image.png')
        
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
        elif command.startswith("loopmouse"):
            n = int(command.split("!")[1])
            # x,y = pg.size()[0]/2,pg.size()[1]/2
            x,y = pg.position()
            t = time()
            while True:
                if int(time()-t)>=n:
                    break
                pg.moveTo(x,y)
                sleep(0.2)
        elif command.startswith("click"):
            ogpos = pg.position()
            pos = command.split("!")[1].split(" ")
            pos = [float(pos[0]),float(pos[1])]
            width,height = pg.size()
            pos = [pos[0]*width, pos[1]*height]
            pg.moveTo(pos)
            pg.click()
            pg.moveTo(ogpos)
        elif command.startswith("scroll"):
            n = int(command.split("!")[1])
            t = time()
            while True:
                if int(time()-t)>=n:
                    break
                n = randint(-3000, 3000)
                pg.scroll(n)
        
        elif command.startswith("combo"):
            keys = command.split("!")[1]
            for k in keys.split(" "):
                if "+" in k:
                    keys = k.split("+")+['' for i in range(0,30)]
                    pg.hotkey(keys[0], keys[1], keys[2], keys[3], keys[4], keys[5],keys[6],keys[6],keys[7],keys[8],keys[9],keys[10],keys[11],keys[12] )
                elif k in self.validKeys:
                    pg.press(k)
                else:
                    pg.write(k+" ")
                sleep(0.5)
        
        elif command == "exit":
            pg.hotkey("alt", "f4")
        
        elif command.startswith("msg"):
            msg = command.replace("msg", "").strip()
            self._showMessage(msg)
        
        elif command == "off":
            self._off()
        
        elif command == "flicker":
            n = randint(10, 25)
            for i in range(0,n):
                self._off(True)
                sleep(0.02)
        
        elif command.startswith("erase"):
            n = int(command.split("!")[1])
            pg.press('backspace', n)