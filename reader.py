#!/usr/bin/python3
 

from socket import *
from topic_create import search_topic

serverName = 'localhost'
serverPortlist = [12004,12005,12006]
#connecting to server
for serverport in serverPortlist:
	try:
		clientSocket = socket(AF_INET, SOCK_STREAM)
		clientSocket.connect((serverName, serverport))
		break
	except:
		continue		
topic=input("enter topic: ") 
k=search_topic(topic)
while(k==0):
                print("the topic does not exist")
                topic=input("enter topic") 
                k=search_topic(topic)
clientSocket.send(topic.encode('utf-8'))
#sending message based on the topic
while(1):
	message = clientSocket.recv(1024)
	modifiedSentence=message.decode('utf-8')
	print(modifiedSentence)
clientSocket.close()
