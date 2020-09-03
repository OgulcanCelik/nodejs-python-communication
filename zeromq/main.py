import zmq
import random
import sys
import time
import base64
from queue import Queue


context = zmq.Context()

# initialize different types of zeromq clients for different types of use cases
rep_port = 5556
rep_socket = context.socket(zmq.REP)
rep_socket.bind("tcp://*:%s" % rep_port)

pub_port = 5557
pub_socket = context.socket(zmq.PUB)
pub_socket.bind("tcp://*:%s" % pub_port)

print("listening")
# in an infinite loop, listen for messages
while True:
    #  Wait for next request from client
    message = rep_socket.recv_string()

    print("Received request: ", message)

    # check if the message is the command we are looking for
    if message == "sendImage":
        # open an image as bytes
        with open("test.jpg", "rb") as img_file:
            # ! you can base64 encode an image bytes to share between network easily
            my_string = base64.b64encode(img_file.read())
    # send encoded image through pub/sub socket
    pub_socket.send(my_string)
    # send acknowledgement through request/response socket
    rep_socket.send_string("OK")
    # time.sleep(0.1)