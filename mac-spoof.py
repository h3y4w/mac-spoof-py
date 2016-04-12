#!/usr/bin/env python
import subprocess
import os
import random
from sys import argv
		
def initial_setup():
	
	p = subprocess.Popen('ip route ls', stdout=subprocess.PIPE, shell=True)
	(tempDevice, err) = p.communicate()
	device_index=tempDevice.find('dev')+3
	print device_index
	device=""
	for i in range(device_index,device_index+8):
		if(tempDevice[i]!=" "):
			device+=tempDevice[i]
	
	
	p = subprocess.Popen("whoami", stdout=subprocess.PIPE, shell=True)
	(user, err) = p.communicate()
	user = user.replace("\n", "")
	mac_dir = '/sys/class/net/%s/subsystem/%s' % (device,device)
	os.chdir(os.pardir)
	subprocess.call('pwd')
	os.chdir(mac_dir)
	with open('address','r') as defaultMacFile:
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
	print '>>'

	choice=input()
	if(choice==1):
		mac=random_mac()
		print mac
	if(choice==2):
		counter=0
		error_notif=' '
		while(error_notif!='OK'):
			if(counter>0):
				print 'Invalid MAC Address: %s' % (error_notif)
			mac=raw_input('MAC Address: ')
			error_notif=valid_mac(mac)
			if(error_notif=='OK'):
				set_mac(mac,device)
			else:
				counter+=1

def valid_mac(mac):
	error_notif = ''
	error_index = ''
	for i in range(9):
		if(i%2==0):
			print mac[i]
			if(mac[i]!=':'):
				error_index=str(i)
				error_notif+=' \n> Expected ":" at %s' % (error_index)
		if(len(mac)!=12):
			error_index=str(len(mac)-5)
			error_notif+=' \n> MAC is not correct length of 12, now at %s' % (error_index)
	if(len(error_notif)==0):
		error_notif = 'OK'

	return error_notif
	
def set_mac(mac,device):
	sudo_ifconfig='sudo ifconfig' + device
	subprocess.call('sudo ifconfig', device, 'down')
	subprocess.call('sudo ifconfig', device, 'hw ether', mac)
	subprocess.call('sudo ifconfig', device, 'up')
	subprocess.call('sudo ifconfig', device, '|grep HWaddr')
	if(device[0]=='w'):
		print "Rebooting WIFI...\n"
		subprocess.call('nmcli nm wifi off')
		subprocess.call('nmcli nm wifi on')	

def random_mac():
	for i in range(12):
		random_number=random.randint(1-9)
		if(i%2==0):
			if(random_num>5):
				random_number=random_number/2
		 	letter= 'a'
			#letter=chr(ord(letter)+random_number
		
		elif(len(mac)==1):
		#	number=str(random.randint(1,5)
			mac+=number
		if(len(mac)==2):
			 mac+=':'
		elif(len(mac)<17 and len(mac)>2 and (i+1)%2==0):
			mac+=':'
	return mac
		

initial_setup()
