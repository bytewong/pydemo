import socketserver

class ForkingTCPServer(socketserver.ForkingMixIn,socketserver.TCPServer):
    pass

class DIYHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("connected from   :   "+str(self.client_address))
        while True:
            recvData=self.request.recv(1024)
            print(recvData.decode())
server_socket=socketserver.ThreadingTCPServer(("127.0.0.1",8080),DIYHandler)
server_socket.serve_forever()