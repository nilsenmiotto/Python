import socket

HOST = "127.0.0.1"
PORT = 6512

def start_server():

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Aguardando conexão em {HOST}:{PORT}...")

        try:
            while True:
                conn, addr = server.accept()
                with conn:
                    print(f"Conexão estabelecida por {addr}")
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        print(f"Recebido: {data.decode()}")
                        conn.sendall("Mensagem recebida com sucesso!".encode())
        except KeyboardInterrupt:
            print("\nServidor encerrado pelo usuário.")

if __name__ == "__main__":
    start_server()