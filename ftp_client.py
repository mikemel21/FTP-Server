from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

while True:
    message = input("> ")

    if message.startswith("CONNECT"):
        args = message.split()
        if len(args) == 3:
            HOST = args[1]
            PORT = int(args[2])
            clientSocket.connect((HOST, PORT))
            print(f"You have successfully connected to {HOST} on port {PORT}")

            clientSocket.send(message.encode())
        else:
            print("Invalid syntax.")
    elif message == "LIST":
        clientSocket.send(message.encode())
    elif message == "QUIT":
        clientSocket.send(message.encode())
        break

    data = clientSocket.recv(1024).decode()
    print(data)
    if data.startswith("Error"):
        break

print("FTP session has ended.")
clientSocket.close()
