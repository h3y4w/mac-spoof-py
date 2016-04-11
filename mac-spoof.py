#!/usr/bin/env python
import subprocess
import os
from sys import argv

def main():
	p = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)
	(user, err) = p.communicate()
	user = user.replace("\n", "")
	macDir = '/sys/class/net/wlan0/subsystem/wlan0/address'
	os.chdir('/home/deno/')
	with open(macDir,'r') as defaultMacFile:
		defaultMac=defaultMacFile.read().replace('\n', '')
	p = subprocess.Popen('ip route ls', stdout=subprocess.PIPE, shell=True)
	(tempDevice, err) = p.communicate()
	device_index=tempDevice.find('dev')+3
	print device_index
	device=""
	for i in range(device_index,device_index+8):
		if(tempDevice[i]!=' '):
			device+=tempDevice[i]
	
		
main()
