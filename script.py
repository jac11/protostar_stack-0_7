#!/usr/bin/env python

import string  
import random
import argparse
import sys

class Tools :
   
    def __init__(self):

	    parser = argparse.ArgumentParser( description="Usage: [OPtion] [arguments]  [length]  [arguments] Example: -c a -l 300")
	    parser.add_argument( '-c',"--char"     , metavar='' , action=None  , help ="to generate A or B..etc char " "Example : -c a -l 220")
	    parser.add_argument( '-r',"--random"   , metavar='' , action =None , help ="to gentreta random pattern " "Example : -r r -l 200", type = str)
	    parser.add_argument( '-a',"--alfa"     , metavar='' , action =None , help ="to generate AAAA to ZZZZ 32bit " "Example : -a x86 -l 26 ")
	    parser.add_argument( '-A',"--alfa_64"  , metavar='' , action =None, help ="generate AAAAAAAA to ZZZZZZZZ 64bit " "Example :-A x64 -l 26")
	    parser.add_argument( '-H',"--Hexdecode", metavar='' , action =None , help ="to decode hex address ""Exampel: -H 0x00000000", type =str)
	    parser.add_argument( '-l',"--length"   , metavar='' , action =None , help ="to give length of the pattern ", type = int)
	    parser.add_argument( '-s',"--L_endian", metavar='' , action =None , help ="to little-endian struct " "Exsampel: -s 0x0876bf67") 
	    self.args = parser.parse_args()
	    self.Main()    
       
    def ALFA__(self):
        try: 
            argv = sys.argv[2]  
            if self.args.char and len(argv) ==1 and sys.argv[1]=="-c" :             
                 char = self.args.char.upper()           
                 len_long = self.args.length
                 result = char*len_long
                 print result 
                 exit()
            else:
                 print"Usege : [Option] -c [arguments] a [OPtion] -l [arguments] Number of length."        
        except UnboundLocalError:
                 print"Usege : [Option] -c [arguments] a [OPtion] -l [arguments] Number of length."
                 print"Exsampel: -c a -l 200"  
                 exit()
    def ran(self):        
            argv = sys.argv[2]                  
            if self.args.random and argv =="r": 
                 len_long_1 = self.args.length                                     
                 result = "".join(random.choice(string.ascii_letters)for i in range(len_long_1)).lower() 
                 print result 
                 exit()
            else:
                 print"Usege : [Option] -r [arguments] r [OPtion] -l [arguments] Number of length."
                 print" exsampel: -r  r -l 100" 
                 exit()
    def AAAA(self): 
        try:    
            argv = sys.argv[2]
            if self.args.alfa and argv =="x86": 
                 len_alfa= self.args.length 
            if len_alfa == 1 or len_alfa < 27:                    
                 ALfa = ''.join((string.ascii_uppercase[i:i+1]*4)for i in range(len_alfa)) 
                 print ALfa
                 exit()
            else:
                 print"Usege : [Option] -a [arguments] x86 [OPtion] -l [arguments] Number of length."
                 print" exsampel: -a  x86 -l 26"            
        except UnboundLocalError:
                 print"Usege : [Option] -a[arguments] x86 [OPtion] -l [arguments] Number of length."
                 print" exsampel: -a  x86 -l 26"      
                            
    def x86_64(self):
        try:    
            argv_1 = sys.argv[2]
            if self.args.alfa_64 and argv_1 =="x64": 
                 len_alfa_1= self.args.length 
            if len_alfa_1 == 1 or len_alfa_1 < 27:                    
                 ALfa_1 = ''.join((string.ascii_uppercase[i:i+1]*8)for i in range(len_alfa_1)) 
                 print ALfa_1
                 exit()
            else:
                 print"Usege : [Option] -r [arguments] x64 [OPtion] -l [arguments] Number of length."
                 print" exsampel: -A  x64 -l 26"            
        except UnboundLocalError:
                 print"Usege : [Option] -A [arguments] x64 [OPtion] -l [arguments] Number of length."
                 print"Exsampel: -A  x64 -l 26"                           
   
    def decode(self):
        try:
            if self.args.Hexdecode  :
                 hexdecode = self.args.Hexdecode
                 hexdecode = hexdecode.replace("0x","")
                 hexdecode = hexdecode.decode("hex")
                 print"decode HEX is : ", hexdecode
            else:
                 print"Usege : [Option] -H [arguments]  HexNumber "
                 print"Exsampel: -H 0x00000000 "                                 
        except Exception :
            print "[IndexError] "
            exit()               
            
    def little_endian1(self):
        #try: 
            if self.args.L_endian:
               little_endian =  self.args.L_endian
               little_endian  =   little_endian.replace("0x","")
               little_endian =   little_endian[::-1]
               little_endian = "".join('\\x%s'% little_endian[i:i+2] for i in range(0, len( little_endian), 2))
               little_endian = "".join('"\\x%s"'% little_endian[i:i+16] for i in range(0, len( little_endian), 16))
               little_endian.replace(" ","")
               little_endian.replace(" ","")
               little_endian= little_endian.replace('"\\x','"')               
               print "little_endian is : ",little_endian
            else:
               print"Usege : [Option] -s [arguments]  Hexaddress "
               print"Exsampel: -s 0x0876bf67 "                
                         
                       
    def Main(self):
        if self.args.char :       
             self.ALFA__()  
             
        if self.args.random :
             self.ran()   
                 
        if self.args.alfa:      
             self.AAAA()
              
        if self.args.alfa_64:
             self.x86_64()
               
        if self.args.Hexdecode:
             self.decode()
                    
        if self.args.L_endian:
             self.little_endian1()
             
                     
if __name__=="__main__":
    Tools()







