# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:46 2021

@author: Simone
"""

from socket import *
import time
from random import *
from AddressTools import *

def getRandomMeasures(q):
    filePath="Data/DataDevice"
    for i in range(4):
        temp=filePath+str(i)+".txt"
        dataRandom=generateData(q)   
        with open(temp,"w") as f:
            f.write(dataRandom)   

def generateData(q):
    output=""
    temp=0
    offset=(24/q)-1
    for x in range(q):
        line= ("{}:00 - {} - {}%\n".format(randint(0+temp,1+temp),randint(25, 45),randint(15, 60)))
        temp+=offset
        output+=line
    return output

def getDataFromFile(device_ip, fileName):
    filePath = "Data/" + fileName
    print("Reading the measures from file, please wait")

    with open(filePath, "r") as f:
        output = f.read();
    for line in output:
        line= "" + device_ip + " = " + line + "\n"

    print("Done! Here we have the measures :\n")
    print(output) 
    print("--------------------\n")
    return output
    
# Send info to Gatway
def sendDataToGateway(deviceIP,deviceSubnet,gateway_address, message):
    ip=deviceIP
    subnet=deviceSubnet
    
    myAddTool= AddressTools(ip,subnet)
    outputToGateway= myAddTool.getAddressEncoded()+message.encode("utf-8")
    
    # Create the UDP socket
    connection_socket = socket(AF_INET, SOCK_DGRAM)
    buffer = 1024
    try:
        print("Sending data to Gateway on interface 192.168.1.0")
        initialTime = time.perf_counter()
        
        connection_socket.sendto(outputToGateway, gateway_address)
        print("Waiting the Gateway response...")
        data, server = connection_socket.recvfrom(buffer)
        # Get the elapsed time from the start
        elapsedTime = round(time.perf_counter() - initialTime,3)
        print("Received Message: {}" .format(data.decode("utf8")))
        print("UDP connection took {} seconds with buffer size = {}" .format(elapsedTime, buffer))
    except Exception as e:
        print(e)
    finally:
        print("Closing Socket")
        connection_socket.close()