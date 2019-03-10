# ! /usr/bin/env python

import grpc
import sys

sys.path.append('../')

from example import data_pb2, data_pb2_grpc

_HOST = 'localhost'
_PORT = '9200'


def run():
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)  
    print(conn)
    client = data_pb2_grpc.FormatDataStub(channel=conn)   
    print(client)
    response = client.DoFormat(data_pb2.actionrequest(text='hello,world!'))   
    print("received: " + response.text)

run()
