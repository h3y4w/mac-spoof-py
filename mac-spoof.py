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
		else:
			print 'Not connected to the Internet!'
	
	
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
	choice=input('>>')

	if(choice==1):
		mac=random_mac()
		print mac
	if(choice==2):
		is_valid=False
		while(is_valid!=True):
			mac=raw_input('MAC Address: ')
			is_valid=valid_mac(mac)
		set_mac(mac,device)

def valid_mac(mac):
	error_notif = ''
	error_index = ''
	for i in range(9):
		if((i+1)%3==0 and i!=0):
			if(mac[i]!=':'):
				error_index=str(i)
				error_letter=mac[i]
				error_notif+=' \n> Expected ":" before %s at index %s' % (error_letter,error_index)
				break
	if(len(mac)!=17):
		error_index=str(len(mac)-5)
		error_notif+=' \n> MAC is not correct length of 17 characters (Including ":")'
	if(len(error_notif)==0):
		return True
	else:
		print 'Invalid MAC Address: %s' % (error_notif)
		return False
	
def set_mac(mac,device):
	print 'CHANGING MAC!'
	sudo_ifconfig = 'sudo ifconfig ' + device
	ifconfig_down = sudo_ifconfig + ' down'
	ifconfig_ether = sudo_ifconfig + ' hw ether ' + mac
	ifconfig_up = sudo_ifconfig + ' up'
	ifconfig_HW = sudo_ifconfig + ' |grew HWaddr'
	#cmd=[sudo_ifconfig, 'down']
	subprocess.call(ifconfig_down, shell=True)
	subprocess.call(ifconfig_ether, shell=True)
	subprocess.call(ifconfig_up, shell=True)
	subprocess.call(ifconfig_HW, shell=True) 
	if(device[0]=='w'):
		print "Rebooting WIFI...\n"
		subprocess.call('nmcli nm wifi off', shell=True)
		subprocess.call('nmcli nm wifi on', shell=True)
	menu(mac,device)	

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
