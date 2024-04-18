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

            clientSocket.send(message.encode())
        else:
            print("Invalid syntax.")
    elif message == "LIST":
        clientSocket.send(message.encode())
    elif message.startswith("RETRIEVE"):
        filename = message.split()[1]
        clientSocket.send(message.encode())
        data = clientSocket.recv(1024*1024)
        with open (filename, 'wb') as f:
            f.write(data)
        print(f"File '{filename}' retrieved successfully with the following contents:")
    elif message.startswith("STORE"):
        filename = message.split()[1]
        try:
            with open(filename, 'rb') as f:
                file_data = f.read()
            clientSocket.send(message.encode())
            clientSocket.send(file_data)
            print(f"File '{filename}' sent.")
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
    elif message == "QUIT":
        clientSocket.send(message.encode())
        break

    data = clientSocket.recv(1024).decode()
    print(data)
    # if data.startswith("Error"):
    #     break
print("FTP session has ended.")
clientSocket.close()
