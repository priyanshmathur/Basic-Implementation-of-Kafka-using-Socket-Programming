#!/usr/bin/python3
def create_topic():
    f=open('topic.txt','r+')
    topic=input("Enter topic: ") 
    k=0
    for line in f.readlines():
        if(line.strip() == topic):           
            k+=1
            break
    if(k==0):
        f.write(topic+'\n')
    else:
        print("No same topic pls")
        create_topic()

def delete_topic():
    f=open('topic.txt','r+')
    topic=input('Enter topic to delete: ')
    with open("topic.txt", "r") as f:
        lines = f.readlines()
    with open("topic.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != topic:
                f.write(line)
                
def search_topic(topic):
    k=0
    with open("topic.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        if line.strip("\n") == topic:
            print("Topic subscribed!")
            k=1
            return k
    if k==0:
        print("Cannot subscribe to uncreated topics")
        return k
"""
i=int(input('Enter 1 to insert and 0 to delete and -1 to exit '))

while(i!=-1):
    if (i==1) :
        create_topic()
        i=int(input('Enter 1 to insert and 0 to delete and -1 to exit '))
    if (i==0):
        delete_topic()
        i=int(input('Enter 1 to insert and 0 to delete and -1 to exit '))
"""

             
 



