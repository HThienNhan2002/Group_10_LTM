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