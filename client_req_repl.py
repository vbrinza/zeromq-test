import zmq
context = zmq.Context()
p = "tcp://localhost:5555"
s = context.socket(zmq.REQ)

s.connect(p)
s.send(b"Hello world 1")
message = s.recv()
s.send_string("STOP")
print(message)
