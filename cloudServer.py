# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:39:31 2021

@author: Simone
"""

import socket as sk

def connectToGateway():
    # TCP Server socket
    serverSocket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    # Bind Socket to port & ip
    serverSocket.bind(("localhost", serverPort))
    
    # Listen Client request
    serverSocket.listen(1)
    print("SERVER CLOUD")
    print("Waiting on interface 10.10.10.0 on port {}..." .format(serverPort))
    
    # Waiting Gateway connection
    gatewayConnection, address = serverSocket.accept()
    print("Gateway connected!")
    print("Detections")
    message = gatewayConnection.recv(bufferSize)
    print(message.decode("utf8"))
    gatewayConnection.send(("Ok, detections received!").encode())
    gatewayConnection.close()
    serverSocket.close()

# TCP Server port and ip
serverPort = 8002
serverIp = '10.10.10.2'
bufferSize = 4096
connectToGateway()