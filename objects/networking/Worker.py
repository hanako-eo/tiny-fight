import threading
from constant import FORMAT
import time

class Worker(threading.Thread):

  # Thread class with a _stop() method.
  # The thread itself has to check
  # regularly for the stopped() condition.

  def __init__(self, conn, addr):
    super(Worker, self).__init__()
    self.room_id = 0
    self.id = id(self)
    self.conn = conn
    self.addr = addr

  def send(self, **kwargs):
    data = f"room={self.room_id}\r\nuser={self.id}\r\n"
    for key, v in kwargs.items():
      data += f"{key}={v}\r\n"
    self.conn.send(data.encode(FORMAT))

  # function using _stop function
  def stop(self):
    self._stop.set()

  def stopped(self):
    return self._stop.isSet()

  def run(self):
    self._stop = threading.Event()
    while True:
      if self.stopped():
        break

      print(f"[{self.addr}]: Message sending")
      self.send(message="data")
      time.sleep(5)
