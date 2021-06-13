import socket
host = 'localhost'
port = 7720
lk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lk.bind((host, port))
while True:
    lk.listen()
    client, address = lk.accept()
    response = client.recv(1024)
    if response != "":
        print("Server Received Message -- " + response.decode())
    print("Processed Data -- " + (response.decode()).upper())
    client.send((response.decode()).upper().encode())
    print('Response Sent.')
    client.close()

