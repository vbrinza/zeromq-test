import zmq

context = zmq.Context()

p = "tcp://*:5555"
s = context.socket(zmq.REP)

s.bind(p)
while True:
    message = s.recv()
    print(message + b"*")
    if not b"STOP" in message:
        s.send(message + b"*")
    else:
        break
