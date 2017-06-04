import zmq

ctx = zmq.Context()

sub = ctx.socket(zmq.SUB)
sub.connect ("tcp://localhost:5556")

sub.setsockopt(zmq.SUBSCRIBE, "")

#subscriber.setsockopt (zmq.SUBSCRIBE, "TEST")


while True:
    print "recv"
    message = sub.recv()
    print message

