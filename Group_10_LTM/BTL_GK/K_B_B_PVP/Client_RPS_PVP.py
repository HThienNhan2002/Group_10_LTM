# ================================
# Import toàn bộ thư viện
# Khởi tạo socket client
# Kết nối đến server
# Hiển thị trạng thái đầu tiên
# ================================

import socket
import threading
import tkinter as tk
from tkinter import messagebox

HOST = "127.0.0.1"      # đổi sang IP server khi chơi LAN
PORT = 7000

class RPSClientGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kéo Búa Bao – PVP")

        self.s = socket.socket()
        try:
            self.s.connect((HOST, PORT))
        except:
            messagebox.showerror("Lỗi", "Không kết nối được tới server!")
            root.destroy()
            return
        
        msg = self.s.recv(1024).decode()
        tk.Label(root, text=msg, font=("Arial", 12)).pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        frame = tk.Frame(root)
        frame.pack()

        tk.Button(frame, text="Kéo", width=10, command=lambda: self.send_choice("keo")).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Búa", width=10, command=lambda: self.send_choice("bua")).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Bao", width=10, command=lambda: self.send_choice("bao")).grid(row=0, column=2, padx=5)

        threading.Thread(target=self.receive_result, daemon=True).start()