import zmq
import time
import random
import sys


class PubServer():

    def pub_server(self):

        port = "4242"

        context = zmq.Context()

        socket = context.socket(zmq.PUB)
        socket.bind("tcp://*:%s" % port)

        while True:
            topic = random.randrange(9999, 10005)
            messagedata = random.randrange(1, 215) - 80
            print "%d %d" % (topic, messagedata)
            socket.send("%d %d" % (topic, messagedata))
            time.sleep(1)
