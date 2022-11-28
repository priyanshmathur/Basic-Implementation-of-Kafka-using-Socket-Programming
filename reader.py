#!/usr/bin/python3
 
 
from socket import *

serverName = 'localhost'
serverPortlist = [12003,12004]

for serverport in serverPortlist:
	try:
		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect((serverName, serverport))
		break
	except:
		continue		
topic=input("enter topic")
clientSocket.send(topic.encode('utf-8'))

while(1):
	message = clientSocket.recv(1024)
	modifiedSentence=message.decode('utf-8')
	print(modifiedSentence)
clientSocket.close()
