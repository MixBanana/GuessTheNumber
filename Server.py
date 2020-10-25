# Sahar Shlichove - סהר שליחוב
# Guess the number - Server side
import socket
import random

rand = random.randint(1,20)
running = 1
counter = 0

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("", 1337))
s.listen(1)
print("Waiting for a client..")
(client,(ip,port)) = s.accept()
print("Received connection from:", ip, "source port number:", port)
client.send("Well, I am thinking of a number between 1 and 20. Take a guess. ".encode())
while(running):
    try:
        data = client.recv(2048).decode()
        data = int(data)
        counter += 1
        if(counter>=5):
            client.send("No more chances!".encode())
            running = 0
        #client.send(data.encode())
        # DEBUG SOME DETAILS
        print(F"Client sent: {data}", F"Server counter: {counter}", F"Generated number: {rand}")
        print(F"Data: {data} Type: ",type(data), F"Rand: {rand} Type:",type(rand))
        if(data=='q'): # Server side close connection check
            s.close()
        elif(rand == data):
            client.send(F"Good job! You guessed my number in {rand} guesses!".encode())
            running = 0
        elif(data < rand):
            # DEBUG LOW
            #print(F"LOW: Data: {data} Rand: {rand}")
            client.send("Your guess is too low.\n".encode())
        elif(data > rand):
            # DEBUG HIGH
            #print(F"HIGH: Data: {data} Rand: {rand}")
            client.send("Your guess is too high.\n".encode())
        else:
            client.send("BASTARD".encode())
            running=0
    except:
        # GOTCHA BASTARD - Prevent unexpected data
        client.send(F"I am afraid '{data}' is not a number".encode())