import socket
host = 'localhost'
port = 7720
lk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lk.connect((host, port))
msg = ""
while True:
    msg = input("Enter the message to be sent or q to quit : ")
    if msg == 'q':
        break
    print(f"I am going to send the data -- {msg}")
    lk.send(f"{msg}".encode())
    response = lk.recv(1024)
    if response != "":
        print("Server Send Message -- " + response.decode())
lk.detach()