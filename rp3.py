#!/usr/bin/python2
#reciever
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
 newdata=data[0].decode("ascii")#convert data into byte form
 print("Message from sener-->",newdata)
 reply=input("Enter your reply-->")
 if len(reply)>150:
  print("message very long")
 else:
  if reply=="ex":
   s.close()
  else:
   s.sendto(reply.encode('ascii'),data[1])
s.close()

