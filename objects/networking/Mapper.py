import os
import socket
import multiprocessing
import subprocess

from constant import PORT
from objects.EventBus import EventBus

class Mapper(EventBus):
  def __init__(self):
    super().__init__()

  def test_connection(self, ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(6)
    result = client.connect_ex((ip, PORT))
    client.close()
    if result == 0:
      self.emit("validate", ip)

  def get_client_ip(self):
    """
    Find the client's IP address
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


  def map(self, pool_size=255):
    """
    Maps the network
    IN: amount of parallel ping processes
    OUT: list of valid ip addresses
    """

    base_ip = ".".join(self.get_client_ip().split(".")[:3]) # get my IP and compose a base like 192.168.1.xxx

    pool = [multiprocessing.Process(target=self.test_connection, args=(f"{base_ip}.{i}",)) for i in range(pool_size)]

    for p in pool:
      p.start()

    for p in pool:
      p.join()
