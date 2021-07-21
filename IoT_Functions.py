# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:46 2021

@author: Simone
"""

from socket import *
import time

def fakeSleep(timestamp):
    for x in range(timestamp-1):
        time.sleep(1)
        print(".",end="")
    time.sleep(1)
    print(".")

def getDataFromFile(deviceIP, filePath):
    filePath = "Data/" + filePath
    print("Reading the measures from file, please wait",end="")
    fakeSleep(3)

    with open(filePath, "r") as f:
        output = f.read();
    for line in output:
        line= "" + deviceIP + " = " + line + "\n"

    print("Done! Here we have the measures :\n")
    print(output+"\n") 
    print("--------------------\n")
    return output
    
# Send info to Gatway
def connectToGateway(gateway_address, message):
    # Create the UDP socket
    connection_socket = socket(AF_INET, SOCK_DGRAM)
    buffer = 1024
    try:
        print("Sending data to Gateway on interface 192.168.1.0...")
        time.sleep(2)
        startTime = time.time()
        
        sent = connection_socket.sendto(message.encode(), gateway_address)
        print("Waiting the Gateway response...")
        data, server = connection_socket.recvfrom(buffer)
        # Calculate the time to send the message
        finalTime = time.time() - startTime
        time.sleep(2)
        print("Received Message: {}" .format(data.decode("utf8")))
        print("UDP message's sending time {} and the size of used buffer is {}" .format(finalTime, buffer))
    except Exception as info:
        print(info)
    finally:
        print("Closing Socket")
        connection_socket.close()