# Sahar Shlichove - סהר שליחוב
# Guess the number - Client side
import socket

running = 1
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1",1337))

while running:
    reply = s.recv(2048).decode()
    print(reply)
    if("Good job" in reply):
        quit()
    elif("No more" in reply):
        quit()
    data = input("Please enter your guess: ")
    if(data == 'q'):
        # Client side Close input
        quit()
    elif(data):
        # Send data
        s.send(data.encode())
    else:
        running = 0