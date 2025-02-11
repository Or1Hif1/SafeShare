import socket


class Server:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(1)  # Listen for one connection at a time
        print(f"Server is listening on {self.host}:{self.port}")

    def start(self):
        while True:
            print("Waiting for a client to connect...")
            conn, addr = self.server_socket.accept()  # Accept a client connection
            print(f"Connected by {addr}")

            with conn:
                while True:
                    data = conn.recv(1024)  # Receive data from client
                    if not data:
                        print("Client disconnected.")
                        break  # Exit if no data is received
                    print(f"Received from client: {data.decode()}")

                    response = "Message received!"
                    conn.sendall(response.encode())  # Send response to client


if __name__ == "__main__":
    server = Server()
    server.start()
