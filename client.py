
import zmq

import time
import threading

num_threads = 100
num_req = 2

time_spent_total = 0
def minha_funcao(numero):
    global time_spent_total
    context = zmq.Context()
    #  Socket to talk to server
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5553")

    #  Do 10 requests, waiting each time for a response
    for request in range(num_req):
        # message = f" thread {numero} req {request} "
        message = " a "

        print("a")
        ti = time.time()
        socket.send_string(message)
        message = socket.recv()
        tf = time.time()
        t_total = tf - ti
        time_spent_total += t_total



# Número de threads que você deseja executar

# Lista para armazenar as threads
threads = []

# Criar e iniciar as threads
ti = time.time()
for i in range(num_threads):
    thread = threading.Thread(target=minha_funcao, args=(i,))
    thread.start()
    threads.append(thread)

# Esperar que todas as threads terminem
for thread in threads:
    thread.join()

tf = time.time()
time_sum = tf - ti

print(f"t_total {time_sum}")

total_runs = num_threads * num_req
print(f"total_runs {total_runs}")
print(f"div {total_runs/time_sum}")
