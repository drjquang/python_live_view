import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


DISCONNECT_MESSAGE = '!DISCONNECTED'


class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__()
        self.connected_clients = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server.bind(ADDR)

        self.geometry("640x240")
        self.title("Tkinter multithreading")

        self.create_frame_button().pack(fill="x", expand=True)

    def on_start_button_clicked(self):
        self.lbl_status.configure(text="Server is running ...")
        serve_thread = threading.Thread(target=self.start_server, daemon=True)
        serve_thread.start()

    def start_server(self):
        self.server.listen()
        print(f'[LISTENING] Server is listening on {SERVER}:{PORT}')
        while True:
            conn, addr = self.server.accept()
            self.connected_clients.append((conn, addr))
            for client in self.connected_clients:
                print(f"Client INFO ----- {client[1]}")
            thread = threading.Thread(target=self.handle_client, args=(conn, addr), daemon=True)
            thread.start()
            print(f'[ACTIVE CONNECTIONs] {threading.active_count() - 1}')

    def handle_client(self, conn, addr):
        print(f'[NEW CONNECTION] {addr} connected')
        isConnected = True
        while isConnected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    isConnected = False
                print(f'[{addr}] {msg}')
                conn.send('MSG received'.encode(FORMAT))

        conn.close()

    def create_frame_button(self) -> ttk.Frame:
        """ Create and return a frame that contains a butto and a label """
        self.frame_button = ttk.Frame(self)
        self.btn_download = ttk.Button(self.frame_button, text="Start", command=self.on_start_button_clicked)
        self.lbl_status = ttk.Label(self.frame_button, background="white", anchor="center")

        self.btn_download.pack(side='left', padx=10, pady=10)
        self.lbl_status.pack(side='left', fill='x', expand=True, padx=10, pady=10)

        return self.frame_button


if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()