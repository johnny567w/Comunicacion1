import socket
import threading
from datetime import datetime

HOST = 'localhost'
PORT = 12345
LOG_FILE = 'chat_log.txt'

clients = []

def broadcast(message, source_socket):
    with open(LOG_FILE, 'a') as f:
        f.write(message + '\n')
    for client in clients:
        if client != source_socket:
            try:
                client.send((message + '\n').encode())
            except:
                clients.remove(client)

def handle_client(client_socket, addr):
    print(f"✅ Cliente conectado desde {addr}")
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                final_msg = f"[{timestamp}] {addr}: {msg}"
                print(final_msg)
                broadcast(final_msg, client_socket)
            else:
                break
        except:
            break
    print(f"❌ Cliente desconectado: {addr}")
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"🟢 Servidor escuchando en {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()

if __name__ == "__main__":
    start_server()
