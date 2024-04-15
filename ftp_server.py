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

        print(f"received {data}")

        if str(data).startswith("CONNECT"):
            resp = "Successfully connected"
        if str(data) == "LIST":
            dirList = os.listdir(os.getcwd())
            resp = "\n".join(dirList)
        elif str(data) == "QUIT":
            break
        else:
            resp = "Nothing was done."
        conn.send(resp.encode())
    except IOError:
        resp = "Error occurred. Terminating connection."
        conn.send(resp.encode())
        conn.close()
print("Terminating connection")
conn.close()
