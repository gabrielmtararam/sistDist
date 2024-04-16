#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5553")
time_spent_total = 0
total_server_runs = 0

while True:
    #  Wait for next request from client
    ti = time.time()
    message = socket.recv()
    message = message+"*"

    #  Do some 'work'
    time.sleep(1)
    # teste = {
    #     'chave':'valor'
    # }
    #  Send reply back to client
    # socket.send(b"World")
    # r = json.dumps(teste)
    # socket.send_json(teste)
    socket.send(message)
    tf = time.time()
    time_sum = tf - ti
    time_spent_total +=time_sum
    total_server_runs +=1

    print(f'taxa servidor {total_server_runs / time_spent_total}   time_spent_total{time_spent_total} total_server_runs{total_server_runs}')


