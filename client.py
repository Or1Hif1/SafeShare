import socket


class Client:

    def __init__(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

