import socket
import threading

HOST = 'localhost'
PORT = 12345

def recibir_mensajes(sock):
    while True:
        try:
            mensaje = sock.recv(1024).decode()
            if mensaje:
                print("\n📩 " + mensaje)
        except:
            print("❌ Error al recibir mensaje.")
            sock.close()
            break

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((HOST, PORT))
print("🟢 Conectado al chat. Escribe tu mensaje:")

thread = threading.Thread(target=recibir_mensajes, args=(cliente,))
thread.start()

while True:
    mensaje = input("> ")
    try:
        cliente.send(mensaje.encode())
    except:
        print("❌ Error al enviar mensaje.")
        break
