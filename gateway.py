# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:46 2021

@author: Simone
"""

from socket import *
import time
from AddressTools import *

def startGateway():
    message=""
    NUM_DEVICE=int(4)
    socket_device = socket(AF_INET, SOCK_DGRAM)
    socket_device.bind(("localhost",6969))
    print('Ready to Serve. Listening for devices...')
    
    # Waiting devices's detections
    ipAlreadyListened=list()
    try:
        #Keep listening until my list is filled with all the devices
        while len(ipAlreadyListened)<NUM_DEVICE:
            data, address = socket_device.recvfrom(1024)
            deviceIP=AddressTools.convertBytesToIP(data[:4],data[4:8])
            deviceData=(data[8:]).decode("utf8")
            #Checking if an IP is already in my list or subnet isn't 255.255.255.0
            if (deviceIP.ip not in ipAlreadyListened) or (deviceIP.subnet!="255.255.255.0"):
                ipAlreadyListened.append(deviceIP.ip)
                indexDevice=len(ipAlreadyListened)
                print("{}° Device = {}".format(str(indexDevice),deviceIP.ip))
                messageReply = "Detection arrived"
                socket_device.sendto(messageReply.encode(), address)
                #Filling the final message with the current device data
                for line in deviceData.split('\n'):
                    if(line!=""):
                        message+=("{} - {}\n".format(deviceIP.ip,line))
    except Exception as e:
        print(e)
    finally:
        socket_device.close()   
    print("Measures delivered!") 
    return message
   
def sendToCloudServer(message):   
    PORT=6942
    BUFFER = 1024
    print("Trying to connect to Cloud Server on port {}".format(PORT))
    try:
        socket_cloud = socket(AF_INET, SOCK_STREAM)
        socket_cloud.connect(('localhost', PORT))
        initialTime = time.perf_counter()
        socket_cloud.send(message.encode())
        data = socket_cloud.recv(BUFFER)
        print("Waiting the Cloud Server's answer...")
        elapsedTime = round(time.perf_counter() - initialTime,5)
        print("Received Message: {}" .format(data.decode("utf8")))
        print("TCP message's sending time {} and the size of used buffer is {}" .format(elapsedTime, BUFFER))      
    except Exception as e:
        print(e)
    finally:
        print("Closing connection")
        socket_cloud.close()

#---GATEWAY---#
dataFromSockets=startGateway()
sendToCloudServer(dataFromSockets)