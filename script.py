#!/usr/bin/env python

import string  
import random
import argparse
import sys
import os 
import re
import subprocess
class Tools :
   
    def __init__(self):

	parser = argparse.ArgumentParser( description="Usage: [OPtion] [arguments]  [length]  [arguments] Exsample: -c a -l 300")
	parser.add_argument( '-c',"--char"     , metavar='' , action=None  ,help ="to generate A or B..etc char " "Exsample : -c a -l 220")
	parser.add_argument( '-r',"--random"   , metavar='' , action =None ,help ="to gentreta random pattern " "Exsample : -r r -l 200", type = str)
	parser.add_argument( '-a',"--alfa"     , metavar='' , action =None ,help ="to generate AAAAtoZZZZ 32bit " "Exsample : -a x86 -l 26 ")
	parser.add_argument( '-A',"--alfa_64"  , metavar='' , action =None,help ="generate AAAAAAAAtoZZZZZZZZ 64bit ""Exsample :-A x64 -l 26")
	parser.add_argument( '-H',"--Hexdecode", metavar='' , action =None ,help ="to decode hex address ""Exampel: -H 0x00000000", type =str)
	parser.add_argument( '-l',"--length"   , metavar='' , action =None,help ="to give length of the pattern ", type = int)
	parser.add_argument( '-s',"--L_endian", metavar='' , action =None ,help ="to little-endian struct " "EExsample: -s 0x0876bf67") 
        parser.add_argument( '-G',"--libc"    , metavar='' , action =None ,help ="to grep from libc Library " "Exsample -G /bin/sh") 
        parser.add_argument( '-F',"--object"  , metavar='' , action =None ,help ="Select  program  dump " "Exsample: -F program.o -D ret") 
        parser.add_argument( '-D',"--dump"  , metavar='' , action =None ,help ="grep program addresses " " Exsample: -F Program -D pop") 
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
                 print"Exsample: -c a -l 200"  
                 exit()
    def ran(self):        
            argv = sys.argv[2]                  
            if self.args.random and argv =="r": 
                 len_long_1 = self.args.length                                     
                 result = "".join(random.choice(string.ascii_letters)for i in range(len_long_1)).lower() 
                 print result 
                 with open("./.data",'w')as data:
                    self.dataW = data.write(result)
                 exit()
            else:
                 print"Usege : [Option] -r [arguments] r [OPtion] -l [arguments] Number of length."
                 print"Exsample: -r  r -l 100" 
                 exit()
    def AAAA(self): 
        try:    
            argv = sys.argv[2]
            if self.args.alfa and argv =="x86": 
                 len_alfa= self.args.length 
            if len_alfa == 1 or len_alfa < 27:                    
                 ALfa = ''.join((string.ascii_uppercase[i:i+1]*4)for i in range(len_alfa)) 
                 print ALfa
                 with open("./.data",'w')as data:
                    self.dataW =  data.write(ALfa)
                 exit()    
            else:
                 print"Usege : [Option] -a [arguments] x86 [OPtion] -l [arguments] Number of length."
                 print "minimum  '1' maximum '26'"
                 print"Exsample: -a  x86 -l 26"           
        except UnboundLocalError:
                 print"Usege : [Option] -a[arguments] x86 [OPtion] -l [arguments] Number of length."
                 print"Exsample: -a  x86 -l 26"      
                            
    def x86_64(self):
        try:    
            argv_1 = sys.argv[2]
            if self.args.alfa_64 and argv_1 =="x64": 
                 len_alfa_1= self.args.length 
            if len_alfa_1 == 1 or len_alfa_1 < 27:                    
                 ALfa_1 = ''.join((string.ascii_uppercase[i:i+1]*8)for i in range(len_alfa_1)) 
                 print ALfa_1
                 with open("./.data",'w')as data:
                     self.dataW = data.write(ALfa_1)
                 exit()
            else:
                 print"Usege : [Option] -A [arguments] x64 [OPtion] -l [arguments] Number of length."
                 print "minimum  '1' maximum '26'"
                 print"Exsample: -A  x64 -l 26"            
        except UnboundLocalError:
                 print"Usege : [Option] -A [arguments] x64 [OPtion] -l [arguments] Number of length."
                 print"Exsample: -A  x64 -l 26"                           
   
    def decode(self):
        try:
            if self.args.Hexdecode  :
                 hexdecode = self.args.Hexdecode
                 hexdecode = hexdecode.replace("0x","")
                 hexdecode ="".join(reversed([hexdecode[i:i+2] for i in range(0,len( hexdecode), 2)]))
                 hexdecode = hexdecode.decode("hex")
                 print"decode HEX is : ", hexdecode                
                 with open("./.data",'r')as data:
                     find = data.read()                    
                 located = find.find( hexdecode)
                 if hexdecode in find  :
                    print "Offset Found at  : ",located      
                    if os.path.isfile("./.data"):
                       os.remove("./.data")
                    else:
                        pass                        
                 else:
                       print "No Offset Found "
            else:
                 print"Usege : [Option] -H [arguments]  HexNumber "
                 print"Exsample: -H 0x00000000 "
        except IOError:
                pass                                            
        except Exception :
            print "[IndexError]-[TypeError]"
            exit()               
            
    def little_endian1(self):
       
            if self.args.L_endian:
               little_endian =  self.args.L_endian
               little_endian1  =   little_endian.replace("0x","")
               little_endian = "".join(reversed([little_endian1  [i:i+2] for i in range(0, len(little_endian1  ), 2)]))
               little_endian = "".join('\\x%s'% little_endian[i:i+2] for i in range(0, len( little_endian), 2))
               little_endian = "".join('"\\x%s"'% little_endian[i:i+32] for i in range(0, len( little_endian), 32))
               little_endian.replace(" ","")
               little_endian.replace(" ","")
               little_endian= little_endian.replace('"\\x','"')               
               print "little_endian is : ",little_endian
               print "struck mode :","struct.pack","('I',",'{}'.format(self.args.L_endian),")".strip()
            else:
               print"Usege : [Option] -s [arguments]  Hexaddress "
               print"Exsample: -s 0x0876bf67 "                
    
    def libc_Library(self):
            if self.args.libc:  
               Libc_libc = self.args.libc     
               process = subprocess.Popen(['strings', '-a', '-t','x','/lib/i386-linux-gnu/libc.so.6'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
               stdout, stderr = process.communicate()
               stdout_libc =stdout
               get_gerp= re.findall("......."+'{}'.format(Libc_libc),stdout_libc) 
               if Libc_libc in stdout_libc:   
                  print"grep _from _libc: ", '\n'.join(get_gerp)                    
               else:
                  print "[Error][NotFound] "
            else:
               print "[Error][/lib/i386-linux-gnu/libc.so.6]"   
                  
    def objdump_file(self):  
                 
            if self.args.object and sys.argv[1] == "-F" and sys.argv[2]=="-D":
               FileName = self.args.object
               FileDump = self.args.dump
               with open('./.file_1','w')as file:                 
                   stdout = subprocess.call(['objdump','-d','{}'.format(FileName)], stdout=file, stderr=file)                         
               process = subprocess.Popen(['grep','{}'.format(FileDump), './.file_1'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
               stdout, stderr = process.communicate()
               print stdout
               if os.path.isfile("./.file_1"):
                     os.remove("./.file_1")
               else:
                  pass      
            else:
               print"Usege : [Option] -F [arguments] filename [OPtion] -D [arguments] grep txt ."
               print"Exsample -F  Objectfile -D pop"            
               
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
        
        if self.args.libc:
             self.libc_Library()
             
        if self.args.object:
             self.objdump_file()   
                                  
if __name__=="__main__":
    Tools()
    
    
    
    

