#!/usr/bin/python
import socket
import time


ip = "172.16.32.128"
port = 31337

buffer="A"
counter=100
maxVal = 10000

for i in range(0, maxVal, counter):
    print("fuzzing with %x bytes" % i)
    buffer = ("A" * i)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect = s.connect((ip, port))
        time.sleep(1)
        s.send(buffer + "\r\n");
        s.close()
    except error as e:
        print(e)
