#! /usr/bin/python

import grpc
import time
import sys
import json
import redis
import hashlib
import token_list

sys.path.append('../')

from concurrent import futures
from proto import data_pb2, data_pb2_grpc

_ONE_DAY_IN_SECONDS = 60*60*24
_HOST = "localhost"
_PORT = "9200"

class RegisterData(data_pb2_grpc.RegisterDataServicer):
    def DoRegister(self, request, context):
        info = request.info
        info_dict = json.loads(info)
        if not ("name" in info_dict.keys() or "email" in info_dict.keys()):
            return data_pb2.actionresponse(text = "info is error")
        
        else:
            r = redis.Redis(host = 'localhost', port = 6379, decode_responses = True)
            name = info_dict["name"]
            email = info_dict["email"]
            to_calc = name+email

            md5_val = hashlib.md5(to_calc.encode('utf8')).hexdigest()
            if r.setnx(md5_val, info):
                return data_pb2.actionresponse(text = "you have registered "+name)
            else:
                return data_pb2.actionresponse(text = "info already exsits")

    def checkToken(self, request, context):
        token = request.token
        
        result_dic = {"result":"",
                    "msg":""
                }

        if token not in token_list.tokens:
            result_dic["result"] = 100
            result_dic["msg"] = "length is not correct"
        else:
            result_dic["result"] = 200
            result_dic["msg"] = "token is correct"

        return data_pb2.actionresult(result = json.dumps(result_dic))

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers = 4))
    data_pb2_grpc.add_RegisterDataServicer_to_server(RegisterData(), grpcServer)
    grpcServer.add_insecure_port(_HOST+":"+_PORT)
    grpcServer.start()
    print "server start"
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)


serve()


