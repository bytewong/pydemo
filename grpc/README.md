## grpc

### 安装过程
```
1. gRPC 的安装：
$ pip install grpcio

2. 安装 ProtoBuf 相关的 python 依赖库：
$ pip install protobuf

3. 安装 python grpc 的 protobuf 编译工具：
$ pip install grpcio-tools
```

### 定义data.proto文件
``` proto
syntax = "proto3";
package example;

service FormatData {   //定义服务,用在rpc传输中
  rpc DoFormat(actionrequest) returns (actionresponse){}
}
message actionrequest {
  string text = 1;
}
message actionresponse{
  string text=1;
}
```

### 生成proto数据的python调用格式和grpc服务接口
```
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./data.proto
```

### google cloud apis design
```
https://cloud.google.com/apis/design/
```
