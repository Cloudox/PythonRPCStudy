from xmlrpc.client import ServerProxy

if __name__ == '__main__':
    server = ServerProxy("http://localhost:8888")
    print (server.get_string("cloudox"))
    print (server.add(8, 8))
