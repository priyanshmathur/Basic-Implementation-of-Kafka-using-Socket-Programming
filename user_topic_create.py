#!/usr/bin/python3

import topic_create

i=int(input('Enter 1 to insert and 0 to delete and -1 to exit '))

while(i!=-1):
    if (i==1):
        topic_create.create_topic()
        i=int(input('Enter 1 to insert and 0 to delete and -1 to exit '))
    if (i==0):
        topic_create.delete_topic()
        i=int(input('Enter 1 to insert and 0 to delete and -1 to exit '))
