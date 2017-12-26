# _*_ coding:utf-8 _*_

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn
import xmlrpc.client


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass


# 调用函数1
def respon_string(str):
    return "get string:%s"%str


# 调用函数2
def add(x, y):
    return x + y


# 供客户端下载文件
def image_get():
    handle = open("boy.jpg", 'rb')
    return xmlrpc.client.Binary(handle.read())


# 供客户端上传文件
def image_put(data):
    handle = open("get_girl.jpg", 'wb')
    handle.write(data.data)
    handle.close()


if __name__ == '__main__':
    server = ThreadXMLRPCServer(('localhost', 8888), allow_none=True) # 初始化
    server.register_function(respon_string, "get_string") # 注册函数1
    server.register_function(add, 'add') # 注册函数2
    server.register_function(image_put, 'image_put')
    server.register_function(image_get, 'image_get')
    print ("Listening for Client")
    server.serve_forever() # 保持等待调用状态
