from xmlrpc.client import ServerProxy
import xmlrpc.client

if __name__ == '__main__':
    server = ServerProxy("http://localhost:8888", allow_none=True)
    print (server.get_string("cloudox"))
    print (server.add(8, 8))
    # 上传文件
    put_handle = open("girl.jpg", 'rb')
    server.image_put(xmlrpc.client.Binary(put_handle.read()))
    put_handle.close()
    # 下载文件
    get_handle = open("get_boy.jpg", 'wb')
    get_handle.write(server.image_get().data)
    get_handle.close()
