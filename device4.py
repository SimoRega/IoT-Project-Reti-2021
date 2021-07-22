# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:35:33 2021

@author: Simone
"""

import DeviceUtils as dev

#Constants
deviceIP = "192.168.1.5"
deviceSubnet= "255.255.255.0"
filePath = "DataDevice1.txt"
gatewayAddress = ("localhost", 6969)

#Generate random measures, param = quantity
dev.getRandomMeasures(4)
#Obtain the data from the file
message = dev.getDataFromFile(deviceIP, filePath)
#Sending the data to the gateway
dev.sendDataToGateway(deviceIP,deviceSubnet,gatewayAddress, message)