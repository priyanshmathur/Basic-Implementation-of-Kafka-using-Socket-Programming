![image](https://user-images.githubusercontent.com/80464081/204954412-69c07f35-071e-4822-9e9f-5842cf83758c.png)

This project is implemented using Socket Programming to simulate the working of kafka

Apache Kafka is an open-source distributed event streaming platform used by thousands of companies for high-performance data pipelines, 
streaming analytics, data integration, and mission-critical applications.

It consists of a server, which acts as a broker, and some clients that act as either producers or consumers. It is able to dynamically create topics
for the producer whenever he wishes to stream data of some different topic which is not registered with the broker yet. As for the consumer, based
on the topic, data shall be streamed to the same, concurrently. 

As for the zookeper, the server sends heartbeat signal to the zookeeper to get the health information of the server. Incase of failure, the server ports as well as the worker nodes have a replication factor of 3, which gives fault tolerance to the program.

All in all there is low latency and provides real time data streams to the consumer smoothly.
