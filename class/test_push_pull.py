from produceur_class import Producer
from consumer import Consumer
from collector import Collector


prod = Producer()
cons = Consumer()
coll = Collector()

prod.producer()
cons.consumer()
cons.consumer()
coll.collector()


