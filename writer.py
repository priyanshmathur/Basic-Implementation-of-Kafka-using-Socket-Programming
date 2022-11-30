#!/usr/bin/python3
 
 
from socket import *
import topic_create 
 
serverName = 'localhost'
serverPortlist = [12001,12002,12003]
topic=input("enter the topic: ")
k=topic_create.search_topic(topic)
if k==0:
	topic_create.create_topic(topic)
for serverPort in serverPortlist:
	try:
		while(1):
			
			clientSocket = socket(AF_INET, SOCK_STREAM)
			clientSocket.connect((serverName, serverPort))
			sentence = input("->")
			sentence=topic+":"+sentence
			clientSocket.send(sentence.encode('utf-8'))
		#modifiedSentence = clientSocket.recv(1024)
		#modifiedSentence=modifiedSentence.decode('utf-8')
		#print('From Server: ', modifiedSentence)
		clientSocket.close()
	except:
		continue
