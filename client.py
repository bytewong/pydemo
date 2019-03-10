import socket
import threading


class client:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 8080
        self.socket_client = socket.socket()
        self.socket_client.connect((self.HOST, self.PORT))
        self.dataFromServer_byte = b'text'
        print(self.socket_client)

    def sendMessage(self, sock):
        while True:
            self.words = input()
            message = self.name + "  :   " + self.words
            sock.sendall(message.encode())

    def receiveMessage(self, sock):
        while True:
            self.dataFromServer_byte = sock.recv(1024)
            str = self.dataFromServer_byte.decode()
            print(str)

    def thread_send_accept(self, sock):
        thread_send = threading.Thread(target=self.sendMessage, args=(sock,))
        thread_send.start()
        thread_receive = threading.Thread(target=self.receiveMessage, args=(sock,))
        thread_receive.start()


client_conn = client()
name_input = input("please enter your name  :   ")
client_conn.name = name_input
sock = client_conn.socket_client
client_conn.thread_send_accept(sock)
