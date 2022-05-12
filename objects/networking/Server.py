import socket 
from constant import PORT
from objects.networking.Worker import Worker

class Server:
  def __init__(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    ADDR = (ip, PORT)
    self.closed = False
    self.threads = []
    self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.server.bind(ADDR)
      
  def open(self):
    self.server.listen()
    while not self.closed:
      conn, addr = self.server.accept()
      worker = Worker(conn, addr)
      worker.start()
      self.threads.append(worker)

  def close(self):
    self.closed = True
    for worker in self.threads:
      worker.stop()
    self.server.close()