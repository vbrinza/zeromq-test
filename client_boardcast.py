import zmq

context = zmq.Context()
s = context.socket(zmq.SUB)
p = "tcp://localhost:5555"

s.connect(p)
s.setsockopt_string(zmq.SUBSCRIBE, "TIME")
for i in range(5):
    time = s.recv()
    print(time)
