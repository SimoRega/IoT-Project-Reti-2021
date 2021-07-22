# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 21:23:48 2021

@author: Simone
"""

class AddressTools:
    def __address_splitter(self, ip):
        octets = []
        for octet in ip.split("."):
            octets.append(int(octet))
        return octets

    def __init__(self, ip, subnet):
        self.ip = ip
        self.subnet = subnet
        self.ip_octets = self.__address_splitter(ip)
        self.subnet_octets = self.__address_splitter(subnet)

    def getAddressEncoded(self):
        return bytes(self.ip_octets) + bytes(self.subnet_octets)

    def convertBytesToIP(ip_bytes, subnet_bytes):
        ipTemp = ''
        subnetTemp = ''
        for i in range(4):
            ipTemp += str(ip_bytes[i]) + ('.' if i < 3 else '')
            subnetTemp += str(subnet_bytes[i]) + ('.' if i < 3 else '')
        return AddressTools(ipTemp, subnetTemp)