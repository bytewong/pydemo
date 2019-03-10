#! /usr/bin python

import grpc
import sys
import json

sys.path.append('../')

from proto import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '9200'


def register(client):
    info = {"name":"tom", "email":"tom@google.com", "age":"20"}
    encode_info = json.dumps(info)
    response = client.DoRegister(data_pb2.actionrequest(info = encode_info))   
    print("received: " + response.text)

def get_connect():
    conn = grpc.insecure_channel(_HOST+":"+_PORT)
    client = data_pb2_grpc.RegisterDataStub(channel = conn)
    return client

def check_token(client, token):
    response = client.checkToken(data_pb2.actiontoken(token = token))
    token_return = json.loads(response.result)
    
    result = token_return["result"]
    if result == 200:
        print "check token success"
        print token_return["msg"]
        return True

    else:
        print "check token fail"
        print token_return["msg"]
        return False

def main():
    client = get_connect()
    if check_token(client,"123456"):
        register(client)
    else:
        print "register fail"

if __name__ == "__main__":
    main()
