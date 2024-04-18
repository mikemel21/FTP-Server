from socket import *
import os

hostname = gethostname()
ipaddress = gethostbyname(hostname)
HOST = ipaddress
PORT = 8888
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((HOST, PORT))

print(f"Server has begun runnning on {HOST} and port {PORT}")

serverSocket.listen()

conn, address = serverSocket.accept()
while True:
    try:
        data = conn.recv(1024).decode()
        if not data:
            break

        if str(data).startswith("CONNECT"):
            print("Established connection with a client")
            resp = f"Successfully connected to {HOST} on port {PORT}"
            conn.send(resp.encode())
        elif str(data) == "LIST":
            print("Displaying directory to client.")
            dirList = os.listdir(os.getcwd())
            resp = "\n".join(dirList)
            conn.send(resp.encode())
        elif str(data).startswith("RETRIEVE"):
            filename = str(data).split()[1]
            resp = f"Retrieving file '{filename}'"
            conn.send(resp.encode())
            server_file_path = os.path.join (os.getcwd(), filename)
            try:
                with open(filename, 'rb') as f:
                    file_data = f.read()
                conn.send(file_data)
                print(f"File '{filename}' sent to client")
            except FileNotFoundError:
                print(f"Error: file '{filename}' not found")
                resp = f"Error: file '{filename}' not found"
                conn.send(resp.encode())
        elif str(data).startswith("STORE"):
            filename = str(data).split()[1]
            print(f"Receiving file '{filename}'")
            server_file_path = os.path.join(os.getcwd(), filename)
            file_data = conn.recv(1024*1024)
            with open(server_file_path, 'wb') as f:
                f.write(file_data)
            print(f"File '{filename}' saved on server with a path of {server_file_path}")
            resp = f"File '{filename}' saved on server."
            conn.send(resp.encode())
        elif str(data) == "QUIT":
            break
        else:
            resp = "Enter a command to interact with the server."
    except IOError:
        resp = "Error occurred. Terminating connection."
        conn.send(resp.encode())
        conn.close()
print("Terminating connection")
conn.close()


