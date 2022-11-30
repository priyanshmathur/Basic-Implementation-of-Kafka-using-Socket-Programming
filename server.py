#!/usr/bin/python3
from socket import *
import time
import schedule
import platform    # For getting the operating system name
import subprocess  # For executing a shell command

def ping():
	    """
	    Returns True if host (str) responds to a ping request.
	    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
	    """

	    # Option for the number of packets as a function of
	    param = '-n' if platform.system().lower()=='windows' else '-c'

	    # Building the command. Ex: "ping -c 1 google.com"
	    command = ['ping', param, '1', 'localhost']

	    subprocess.call(command)
	    
serverPort1_list = [12001,12002,12003]
serverPort2_list = [12004,12005,12006]

def zookeeper():
	sock = socket(AF_INET, SOCK_STREAM)
	result = sock.connect_ex(('localhost',serverPort1_list[0]))
	sock1 = socket(AF_INET, SOCK_STREAM)
	result1 = sock.connect_ex(('localhost',serverPort2_list[0]))
	if result == 0 and result1 == 0:
	   print ("Port is open")
	   serverPort1=serverPort1_list[0]
	   serverPort2=serverPort2_list[0]
	else:
	   print ("Port is not open")
	   serverPort1=serverPort1_list[1]
	   serverPort2=serverPort2_list[1]
	sock.close()
	sock1.close()
	print(serverPort1,serverPort2)
	return serverPort1,serverPort2

serverPort1,serverPort2=zookeeper()
serverSocket1 = socket(AF_INET,SOCK_STREAM)
serverSocket1.bind(('',serverPort1))
serverSocket1.listen(1)

def server():
	serverSocket2 = socket(AF_INET,SOCK_STREAM)
	serverSocket2.bind(('',serverPort2))
	serverSocket2.listen(1)
	connectionSocket2, addr = serverSocket2.accept()
	topic2=connectionSocket2.recv(1024)
	topic2=topic2.decode('utf-8').strip()
	print('The server is ready to receive')
	while(1):
		connectionSocket1, addr = serverSocket1.accept()
		sentence = connectionSocket1.recv(2048)
		topic,message=sentence.decode('utf-8').split(':')
		print(topic)
		print(message)
		topic=topic.strip()	 	
		if topic==topic2: 
			connectionSocket2.send(message.encode('utf-8'))
#connectionSocket2.close()	

schedule.every(10).seconds.do(ping)
schedule.every(1).seconds.do(server)

while True:
    schedule.run_pending()
    time.sleep(1)


