#!/usr/bin/python2
import os
import socket
recv_ip="127.0.0.1"
recv_port=4444 # 0-1024  free udp port can be checked using netstat -nulp

#creating udp socket
#             ip type ipv4    ,udp                              
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 4>3 :
 a=raw_input("Enter message--->(enter ex to exit)")
 if len(a)>150:
  print("message length exceded")
 else:
  if a=="ex":
   break
  else:
   s.sendto(a,(recv_ip,recv_port))
   print(s.recvfrom(100))

