#!/usr/bin/python2

import socket
r_ip="127.0.0.1"
r_port=4444 # 0-1024  free udp port can be checked using netstat -nulp

#creating udp socket
#             ip type ipv4    ,udp                              
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#fitting ip and port with udp socket
s.bind((r_ip,r_port))

#recv data from sender
while 4>2:
 data=s.recvfrom(100)
 print("Message from sener-->",data[0])
 reply=raw_input("Enter your reply-->")
 if len(reply)>150:
  print("message very long")
 else:
  if reply=="ex":
   break
  else:
   s.sendto(reply,data[1])


