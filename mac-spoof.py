#!/usr/bin/env python
import subprocess
import os
from sys import argv
		
def initial_setup():
	
	p = subprocess.Popen('ip route ls', stdout=subprocess.PIPE, shell=True)
	(tempDevice, err) = p.communicate()
	device_index=tempDevice.find('dev')+3
	print device_index
	device=""
	for i in range(device_index,device_index+8):
		if(tempDevice[i]!=' '):
			device+=tempDevice[i]
	
	
	p = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)
	(user, err) = p.communicate()
	user = user.replace("\n", "")
	macDir = '/sys/class/net/%s/subsystem/%s/address' % (device,device)
	os.chdir('/home/deno/')
	with open(macDir,'r') as defaultMacFile:
		defaultMac=defaultMacFile.read().replace('\n', '')
		mac=defaultMac
	menu(mac,device)
	
def menu(mac,device):
	print '\t\t\t\tMac Spoofer\n\t\t\t\t~~~~~~~~~~~'
	print 'Current Device: %s' %(device)
	print 'Current MAC: %s\n\n' % (mac)
	print '\t1)Random\n'
	print '\t\t2)Input\n'
	print '\t\t\t3)Reset\n'
	print '\t\t\t\t4)Change Device\n'
	print '\t\t\t\t\t\t5)Exit\n\n'
	print '>> '

	
initial_setup()
