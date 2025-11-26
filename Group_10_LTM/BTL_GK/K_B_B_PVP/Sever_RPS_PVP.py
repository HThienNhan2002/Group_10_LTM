# ================================
# Import tất cả thư viện của server
# Cấu hình HOST / PORT
# Khởi tạo danh sách client và lựa chọn
# Viết hàm check thắng–thua cho game
# ================================

import socket
import threading

HOST = "0.0.0.0"
PORT = 7000

clients = []
choices = {}

def check_winner(p1, p2):
    if p1 == p2:
        return "Hòa"
    rules = {"keo": "bao", "bao": "bua", "bua": "keo"}
    if rules[p1] == p2:
        return "P1 thắng"
    return "P2 thắng"


def handle_player(conn, index):
    global choices

    while True:
        try:
            data = conn.recv(1024).decode()
        except:
            break
        if not data:
            break

        choices[index] = data

        if len(choices) == 2:
            p1, p2 = choices[0], choices[1]
            result = check_winner(p1, p2)

            clients[0].send(f"Bạn: {p1} – Đối thủ: {p2} → {result}".encode())
            clients[1].send(f"Bạn: {p2} – Đối thủ: {p1} → {result}".encode())

            choices = {}

    conn.close()


def main():
    s = socket.socket()
    s.bind((HOST, PORT))
    s.listen(2)
    print("Server đang chờ 2 người chơi...")

    while len(clients) < 2:
        conn, addr = s.accept()
        clients.append(conn)
        print("Người chơi kết nối:", addr)
        conn.send("Đã kết nối! Chờ người chơi còn lại...".encode())

    print("Đủ 2 người → bắt đầu trận!")