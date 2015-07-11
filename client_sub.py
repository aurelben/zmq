import sys
import zmq

port = "4242"
# Socket to talk to server

context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Collect In Progress ..."

socket.connect("tcp://localhost:%s" % port)

#subscribe to topic

topicfilter = "10001"
socket.setsockopt(zmq.SUBSCRIBE, topicfilter)

#process 5 update
total_value = 0
for update_nbr in range (5):
	string = socket.recv()
	topic, messagedata = string.split()
	total_value += int(messagedata)
	print topic, messagedata

print "Average messagedata value for topic '%s' was %d" % (topicfilter, total_value / update_nbr)