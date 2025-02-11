import socket


class Client:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print(f"Connected to server at {self.host}:{self.port}")
        except ConnectionRefusedError:
            print("Failed to connect to the server. Make sure the server is running.")
            return

        self.send_message()

    def send_message(self):
        try:
            message = input("Enter a message to send to the server: ")
            self.client_socket.sendall(message.encode())  # Send message to server

            response = self.client_socket.recv(1024)  # Receive server response
            print(f"Received from server: {response.decode()}")
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.client_socket.close()
            print("Connection closed.")



if __name__ == "__main__":
    client = Client()
    client.connect()
