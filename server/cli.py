while True:
    command = input("> ")
    if command == "q":
        break

    with open('command.txt', 'w') as f:
        f.write(command)
