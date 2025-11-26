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
        

#50 đến 53 Viên
 if __name__ == "__main__":
     root = tk.Tk()
     app = RPSClientGUI(root)
     root.mainloop()