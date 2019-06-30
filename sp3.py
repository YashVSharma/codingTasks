#!/usr/bin/python2
#sender


import os
import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024  free udp port can be checked using netstat -nulp

#creating udp socket
#             ip type ipv4    ,udp                              
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>3 :
 a=input("Enter message--->(enter ex to exit)")
 if len(a)>150:
  print("message length exceded")
 else:
  if a=="ex":
   os.system("exit()")
  else:
   na=a.encode("ascii")
   s.sendto(na,(recv_ip,recv_port))
   dta=s.recvfrom(100)
   ndta=dta[0].decode(ascii)
   print("ndta")

