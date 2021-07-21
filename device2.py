# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 15:34:01 2021

@author: Simone
"""

import DeviceUtils as dev

#Constants
deviceIP = "192.168.1.3"
filePath = "DataDevice2.txt"
gatewayAddress = ("localhost", 6969)

#Obtain the data from the file
message = dev.getDataFromFile(deviceIP, filePath)
#Sending the data to the gateway
dev.sendDataToGateway(gatewayAddress, message)