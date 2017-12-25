# _*_ coding:utf-8 _*_

from xmlrpc.server import SimpleXMLRPCServer
from socketserver import ThreadingMixIn


class ThreadXMLRPCServer(ThreadingMixIn, SimpleXMLRPCServer):
    pass

# 调用函数1
def respon_string(str):
    return "get string:%s"%str

# 调用函数2
def add(x, y):
    return x + y


if __name__ == '__main__':
    server = ThreadXMLRPCServer(('localhost', 8888)) # 初始化
    server.register_function(respon_string, "get_string") # 注册函数1
    server.register_function(add, 'add') # 注册函数2
    print ("Listening for Client")
    server.serve_forever() # 保持等待调用状态
