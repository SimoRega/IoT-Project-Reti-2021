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

def getDataFromFile(device_ip, fileName):
    filePath = "Data/" + fileName
    print("Reading the measures from file, please wait",end="")
    fakeSleep(3)

    with open(filePath, "r") as f:
        output = f.read();
    for line in output:
        line= "" + device_ip + " = " + line + "\n"

    print("Done! Here we have the measures :\n")
    print(output) 
    print("--------------------\n")
    return output
    
# Send info to Gatway
def sendDataToGateway(gateway_address, message):
    # Create the UDP socket
    connection_socket = socket(AF_INET, SOCK_DGRAM)
    buffer = 1024
    try:
        print("Sending data to Gateway on interface 192.168.1.0",end="")
        fakeSleep(3)
        initialTime = time.time()
        
        connection_socket.sendto(message.encode(), gateway_address)
        print("Waiting the Gateway response...")
        data, server = connection_socket.recvfrom(buffer)
        # Get the elapsed time from the start
        elapsedTime = round( time.time() - initialTime, 3)
        time.sleep(2)
        print("Received Message: {}" .format(data.decode("utf8")))
        print("UDP connection took {} seconds with buffer size = {}" .format(elapsedTime, buffer))
    except Exception as e:
        print(e)
    finally:
        print("Closing Socket")
        connection_socket.close()