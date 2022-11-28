#!/usr/bin/python3
 
 
from socket import *

 
serverName = 'localhost'
serverPortlist = [12001,12002]
topic=input("enter the topic")

for serverPort in serverPortlist:
	try:
		while(1):
			
			clientSocket = socket(AF_INET, SOCK_STREAM)
			clientSocket.connect((serverName, serverPort))
			sentence = input()
			sentence=topic+":"+sentence
			clientSocket.send(sentence.encode('utf-8'))
		#modifiedSentence = clientSocket.recv(1024)
		#modifiedSentence=modifiedSentence.decode('utf-8')
		#print('From Server: ', modifiedSentence)
		clientSocket.close()
	except:
		continue
