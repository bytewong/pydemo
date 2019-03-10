import socket
import threading


class server:
    def __init__(self):
        self.HOST = "127.0.0.1"
        self.PORT = 8080
        self.socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket_server.bind((self.HOST, self.PORT))
        self.socket_server.listen(5)
        self.total = 0
        self.userDict = {}
        self.addrList = []
        self.userWords = []
        self.userList = []

    def newClientConnection(self, conn, addr):
        welcomeWords = "connected by " + str(addr[0]) + " " + str(addr[1]) + "...Welcome!~"
        welcomeWords_str = welcomeWords.encode()
        print(self.userList)
        for connection in self.userList:
            connection.sendall(welcomeWords_str)
        while True:
            words_byte = conn.recv(1024)
            words = words_byte.decode()
            print(words)
            for c in self.userList:
                c.sendall(words.encode())

    def gewNewConnection(self):
        while True:
            conn, addr = self.socket_server.accept()
            # conn为新的socket对象，与服务器连接后的后续操作由conn去处理
            self.userDict[conn] = addr
            self.userList.append(conn)
            thread = threading.Thread(target=self.newClientConnection, args=(conn, addr))
            thread.start()

server_conn=server()
server_conn.gewNewConnection()