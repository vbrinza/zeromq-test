import zmq, time, pickle, sys, random

context = zmq.Context()
me = str(sys.argv[1])
s = context.socket(zmq.PUSH)
p = "tcp://*:5555"
s.bind(p)

for i in range(100):
    workload = random.randint(1, 100)
    s.send(pickle.dumps((me,workload)))
