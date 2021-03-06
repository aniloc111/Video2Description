import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from config import getRpcConfig

config = getRpcConfig()
SERVER_RUNAS = config["RPC_SERVER_RUNAS"]
PORT = config["RPC_PORT"]
SERVER_IP = config["RPC_ENDPOINT"]

def register_server(framework):
    print 'Preparing for Register Server'
    server = SimpleXMLRPCServer((SERVER_RUNAS, PORT))
    print 'Listening to %d' % PORT
    server.register_function(framework.predict_fnames, 'predict_fnames')
    server.register_function(framework.predict_ids, 'predict_ids')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        raise
    except Exception:
        raise
    finally:
        print "Exiting"
        server.server_close()

def get_rpc():
    proxy = xmlrpclib.ServerProxy("http://%s:%d/" % (SERVER_IP, PORT))
    return proxy
