# Overview
This project is an implementation of an FTP application that supports text file transfer. The client program presents a command line interface that allows a user to:
- Connect to a server
- List files stored at the server
- Download (retrieve) a file from the server
- Upload (store) a file from the client to the server
- Terminate the connection to the server

The server program binds to a port and listens for requests from a client. After a client connects to the server, the server waits for commands. When the client sends a terminate message (quit), the server terminates the connection and waits for the next connection.

# ftp_client.py
This file implements an FTP client. This client file is in charge of prompting the user for a command and then executing code based on the command.
The commands are as follows:
- ```CONNECT <IP address> <Port #>```: Requests a connection to the server corresponding to the given IP address and port number.
- ```LIST```: Lists the files in the server's directory.
- ```RETRIEVE <filename>```: Retrieves the given file from the server.
- ```STORE <filename>```: Stores the given file in the server.
- ```QUIT```: Terminates the current session.

The script starts by importing the socket module, which is used for network communication. The HOST and PORT variables are initially set to None, as they are determined later by the ```CONNECT``` command. A TCP socket is created using ```socket(AF_INET, SOCK_STREAM)```. The user is prompted to enter a command within the main loop, which runs until the ```QUIT``` command is executed. The script receives and prints the server's responses to the above commands. Finally, the socket connection is closed, and the script prints a message indicating the end of the FTP section.

To run: ```python ftp_client.py``` or ```python3 ftp_client.py```

# ftp_server.py
The script starts by importing the ```socket``` module, which is used for network communication, and the ```os``` module, which is used to interact with the operating system. The server's hostname and IP address are determined using the ```gethostname()``` and ```gethostbyname()``` functions. The server's host and port are set to the determined IP address and port 8888. A TCP socket is created using ```socket(AF_INET, SOCK_STREAM)```. The server begins listening for incoming connections using ```serverSocket.listen()```, and the ```serverSocket.accept()``` call block until a client connects. The main loop contains the logic for the server to receive, parse, and process commands from the connected client. If an ```IOError``` occurs during the processing of a command, the server sends an error message to the client and closes the connection. The server then closes the connection with the client and prints a mnessage indicating the connection has been terminated.

To run: ```python ftp_server.py``` or ```python3 ftp_server.py```

# clientTestFile.txt and serverTestFile.txt
These files are simply test files for the client and server, respectively. They are used to test the ```STORE``` and ```RETRIEVE``` commands to ensure these commands correctly send the text files without losing any information.