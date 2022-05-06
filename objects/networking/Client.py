import socket
from constant import FORMAT, PORT
from objects.EventBus import EventBus

class Client(EventBus):
  def __init__(self):
    super().__init__()
    self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.room_id = 0
    self.id = id(self)
    self.add_listener("received", print)

  def send(self, **kwargs):
    data = f"room={self.room_id}\r\nuser={self.id}\r\n"
    for key, v in kwargs.items():
      data += f"{key}={v}\r\n"
    self.client.send(data.encode(FORMAT))

  def listen(self):
    message = ""
    while True:
      chunk = self.client.recv(128)
      message += chunk.decode(FORMAT)
      if len(chunk) < 128:
        self.emit("received", message)
        message = ""

  def open(self, server):
    self.client.connect((server, PORT))


"""
Room=test\r\n
User=...\r\n
Troop=x;y
Action=move
Effects=[]
"""
