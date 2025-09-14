import zmq, time, pickle, sys

context = zmq.Context()
me = str(sys.argv[1])
p1 = "tcp://localhost:5555"

r = context.socket(zmq.PULL)
r.connect(p1)
while True:
    work = pickle.loads(r.recv())
    print(work)
