# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:39:31 2021

@author: Simone
"""

from socket import *

def connectToGateway():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    # Bind Socket to port & ip
    serverSocket.bind(("localhost", serverPort))
    
    # Listen Client request
    serverSocket.listen(1)
    print("SERVER CLOUD")
    print("Waiting on interface 10.10.10.0 on port {}..." .format(serverPort))
    
    # Waiting Gateway connection
    gatewayConnection, address = serverSocket.accept()
    print("Gateway connected!")
    try:
        # TCP Server socket
        print("All the measures from devices down here :\n")
        message = gatewayConnection.recv(bufferSize)
        print(message.decode("utf8"))
        gatewayConnection.send(("Ok, measures received!").encode())       
    except Exception as e:
        print(e)
    finally:
        gatewayConnection.close()
        serverSocket.close()
        

#---CLOUDSERVER---#
serverPort = 6942
serverIp = '10.10.10.2'
bufferSize = 4096
connectToGateway()