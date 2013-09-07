'''
Created on Apr 7, 2012
@author: cgrubb
'''

import zmq
from zmq.eventloop import zmqstream, ioloop

ioloop.install()

import tornado
from tornado import web, websocket

_sockets = []

class EarthSocket(websocket.WebSocketHandler):
    
    def open(self):
        print "Socket open"
        _sockets.append(self)
        
    def on_close(self):
        print "Socket closed"
        _sockets.remove(self)

    def on_message(self, message):
        print message

class Listener():
    
    def __init__(self):
        '''
        Constructor
        '''
        self.context = zmq.Context().instance()
        self.socket = self.context.socket(zmq.PULL)
        self.socket.bind("tcp://*:20005")
        self.loop = ioloop.IOLoop.instance()
        self.stream = zmqstream.ZMQStream(self.socket)
        self.stream.on_recv(self.handle_msg)
        
    def handle_msg(self, msg):
        for sock in _sockets:
            sock.write_message(unicode(msg[0]))
    

if __name__ == "__main__":
    listener = Listener()
    application = tornado.web.Application([
            (r"/static/(.*)", web.StaticFileHandler,{"path":"static"}),
            (r"/socket", EarthSocket)])
    application.listen(8888)
    ioloop.IOLoop.instance().start()