import time
import zmq
import random


class Consumer():

    def consumer(self):
        consumer_id = random.randrange(1, 10005)
        print "i am consumer #%s" % (consumer_id)
        context = zmq.Context()

        #revieve work from consumer
        consumer_receiver = context.socket(zmq.PULL)
        consumer_receiver.connect("tcp://127.0.0.1:5557")

        #send work to result colector
        consumer_sender = context.socket(zmq.PUSH)
        consumer_sender.connect("tcp://127.0.0.1:5558")

        while True:
            work = consumer_receiver.recv_json()
            data = work['num']
            result = {'consumer': consumer_id, 'num': data}
            if data % 2 == 0:
                consumer_sender.send_json(result)
