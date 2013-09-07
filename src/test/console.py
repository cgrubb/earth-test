'''
Created on Apr 7, 2012
@author: cgrubb
'''

import sys
import signal

def signal_handler(signum, frame):
    sys.exit()

import zmq

context = zmq.Context().instance()
socket = context.socket(zmq.PUSH)
socket.connect("tcp://localhost:20005")
signal.signal(signal.SIGINT, signal_handler)
msg = ''
while msg != 'exit':
    try:
        msg = raw_input("> ")
        socket.send(msg)
    except EOFError:
        break

socket.close()
context.term()
