# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:46 2021

@author: Simone
"""

from socket import *
import time

message = ""

socket_device = socket(AF_INET, SOCK_DGRAM)
socket_device.bind(("localhost",6969))
print('Listening for devices')

# Waiting devices's detections
ipAlreadyListened=list()
try:
    while len(ipAlreadyListened)<4:
        data, address = socket_device.recvfrom(1024)
        if address not in ipAlreadyListened:
            ipAlreadyListened.append(address)
            
            
            
            
            indexDevice=len(ipAlreadyListened)+1
            
            print(""+str(indexDevice)+"° Device = "+address)
            
            
            
            message = message + data.decode("utf8") + '\n'
            time.sleep(2)
            messageReply = "Detection arrived"
            socket_device.sendto(messageReply.encode(), address)
except Exception as e:
    print(e)
finally:
    socket_device.close()
    

    
print("Detections arrived. Open connection interface 10.10.10.0")

# Device detections have arrived and sending everything to the cloud
socket_cloud = socket(AF_INET, SOCK_STREAM)
socket_cloud.connect(('localhost', 8002))
startTime = time.time()
socket_cloud.send(message.encode())
buffer = 4096
data = socket_cloud.recv(buffer)
print("Waiting the server's response...")
finalTime = startTime - time.time()
print("Received Message: {}" .format(data.decode("utf8")))
print("TCP message's sending time {} and the size of used buffer is {}" .format(finalTime, buffer))
print("Closing connection")
socket_cloud.close()
# %%
