import socket

HOST, PORT = "127.0.0.1", 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"[SERVER1] Listening on {HOST}:{PORT}")
    conn, addr = s.accept()
    with conn:
        print(f"[SERVER1] Connected by {addr}")
        data = conn.recv(1024).decode('utf-8').strip()
        print(f"[SERVER1] Received: {data}")
        reply = f"Đã nhận {data}"
        conn.sendall(reply.encode('utf-8'))
    print("[SERVER1] Done.")
