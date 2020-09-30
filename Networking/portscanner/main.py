import socket
import threading
from queue import Queue


#target = "YOUR ROUTER IP"
queue = Queue()
open_ports = []

def portscan(port):
  try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    return True
  except:
    return False

def fillQueue(port_list):
  for port in port_list:
    queue.put(port)

def worker():
  # Once queue has been filled with ports, get() each port
  # If portscan(port) returns True, append() to open_ports
  while not queue.empty():
    port = queue.get()
    if portscan(port):
      print("Port {} is opened!".format(port))
      open_ports.append(port)

port_list = range(1, 1024)
# 1. Call fillQueue function with 1-1024 integers to create a queue
fillQueue(port_list)

thread_list = []
for t in range(100):
  # 2. Create a thread with worker as a target function
  thread = threading.Thread(target=worker)
  # 3. Append each thread of worker functions into thread_list
  thread_list.append(thread)

# 4. Call all threads of the worker function
for thread in thread_list:
  thread.start()

# 5. Once all threads of the worker function finish, join them
for thread in thread_list:
  thread.join()

# 6. Print only when the threads are finished
print("Open ports are: ", open_ports)