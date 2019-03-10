#! /usr/bin/python

import grpc
import time
import sys

sys.path.append('../')

from concurrent import futures
from example import data_pb2, data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60*60*24
_HOST = "localhost"
_PORT = "9200"

class FormatData(data_pb2_grpc.FormatDataServicer):
    def DoFormat(self, request, context):
        s = request.text
        return data_pb2.actionresponse(text = s.upper())

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    data_pb2_grpc.add_FormatDataServicer_to_server(FormatData(), grpcServer)
    grpcServer.add_insecure_port(_HOST+":"+_PORT)
    grpcServer.start()
    print "1"
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


serve()


