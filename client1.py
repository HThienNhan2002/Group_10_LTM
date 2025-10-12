import socket

HOST, PORT = "127.0.0.1", 5000
msg = "Hello World"
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(msg.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    print("[CLIENT1] Reply:", data)
