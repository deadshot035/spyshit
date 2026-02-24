from time import sleep

command = input("Enter command: ")
s = float(input("Enter timeout in minutes: "))
sec = int(60*s)
for i in range(sec,0,-1):
    sleep(1)
    print(f"{i} seconds left",end="\r")

with open('command.txt', 'w') as f:
    f.write(command)

print("Command added")
