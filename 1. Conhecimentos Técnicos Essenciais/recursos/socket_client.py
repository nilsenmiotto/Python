import socket

HOST = "127.0.0.1"
PORT = 6512

def start_client():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall("Olá, servidor!".encode())

        data = client.recv(1024)
        print(f"Resposta do servidor: {data.decode()}")

if __name__ == "__main__":
    start_client()