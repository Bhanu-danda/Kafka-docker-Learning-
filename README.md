Kafka + Docker + Spark — Learning Notes
1. Kafka Producer

A Producer is an application that creates and sends messages/data to Kafka.

For example, our Python producer generates orders:

{
  "order_id": 1234,
  "amount": 2500,
  "city": "Bangalore"
}

and sends them to a Kafka topic.

In simple words:

Producer = The application that sends data to Kafka.

Example:

Python Program
     ↓
   Producer
     ↓
    Kafka
2. Kafka Consumer

A Consumer is an application that reads/receives messages from Kafka topics.

Our Python consumer listens to the orders topic and receives the orders produced by the producer.

In simple words:

Consumer = The application that reads data from Kafka.

Example:

Kafka
  ↓
orders topic
  ↓
Consumer
  ↓
Python Program
Kafka
3. What is Apache Kafka?

Apache Kafka is a distributed event streaming platform used to publish, store, and process streams of data in real time.

Kafka allows applications to send data to Kafka and other applications to consume that data independently.

Example:

        Producer
           │
           ▼
        ┌───────┐
        │ Kafka │
        └───────┘
           │
     orders topic
           │
           ▼
        Consumer

In simple words:

Kafka is a system that allows applications to reliably send, store, and receive streams of data.

4. Kafka Broker

A Kafka Broker is a Kafka server that receives, stores, and serves messages.

When we ran Kafka in Docker, our Kafka container was running a Kafka broker.

Python Producer
      ↓
Kafka Broker
      ↓
Kafka Topic
      ↓
Python Consumer

A Kafka cluster can contain multiple brokers:

Kafka Cluster


┌─────────────┐
│   Broker 1  │
├─────────────┤
│   Broker 2  │
├─────────────┤
│   Broker 3  │
└─────────────┘

In simple words:

Broker = A Kafka server responsible for storing and serving Kafka data.

Kafka Topic
5. Kafka Topic

A Topic is a named category/feed where Kafka stores messages.

For example, we created:

orders

Our producer sends order messages to the orders topic:

Producer
   │
   │ order data
   ▼
orders topic

Consumers can then read messages from that topic.

In simple words:

Topic = A named stream/category where Kafka messages are stored.

Examples:

orders
payments
users
transactions
logs
Our example
Producer
   │
   │
   ▼
orders topic
   │
   │
   ▼
Consumer
Docker
6. Docker

Docker is a platform used to package and run applications in isolated environments called containers.

Instead of installing everything directly on our computer, we can run applications inside containers.

For example, we ran:

Kafka → Docker container
Python → Docker container

In simple words:

Docker allows us to package applications with their dependencies and run them consistently in containers.

Docker Image
7. Docker Image

A Docker Image is a read-only template/package used to create Docker containers.

For example:

python:3.12

is a Python Docker image.

We also created our own image:

python-kafka-producer

The image contains things our application needs, such as:

Python
Python libraries
Application code
Configuration

In simple words:

Docker Image = Blueprint/package used to create a container.

Think:

Docker Image
     ↓
  creates
     ↓
Docker Container
Docker Container
8. Docker Container

A Docker Container is a running instance of a Docker image.

For example:

Image:
python-kafka-producer


        ↓ docker run


Container:
python-producer

We also ran:

kafka
python-producer
python-consumer

as containers.

In simple words:

Container = A running instance of a Docker image.

A useful analogy:

Image      = Class / Blueprint
Container  = Running Object / Instance
Dockerfile
9. Dockerfile

A Dockerfile is a text file containing instructions for building a Docker image.

For example:

FROM python:3.12


WORKDIR /app


COPY requirements.txt .


RUN pip install -r requirements.txt


COPY producer.py .


CMD ["python", "producer.py"]

Each instruction tells Docker how to create the environment for our application.

In simple words:

Dockerfile = Instructions/recipe used to build a Docker image.

Think:

Dockerfile
    ↓
docker build
    ↓
Docker Image
    ↓
docker run
    ↓
Container
Docker Build
10. docker build

docker build is a Docker command used to create a Docker image from a Dockerfile.

We used:

docker build -t python-kafka-producer .

Here:

docker build

means build an image.

-t python-kafka-producer

gives the image a name.

.

means use the current directory as the build context.

In simple words:

docker build = Build a Docker image using a Dockerfile.

Docker Run
11. docker run

docker run is a Docker command used to create and start a container from an image.

For example:

docker run python-kafka-producer

Docker takes:

python-kafka-producer

image and creates a running container from it.

We also used:

docker run --rm --name python-producer --network kafka-network python-kafka-producer

Here:

--rm

automatically removes the container after it stops.

--name python-producer

gives the container a name.

--network kafka-network

connects the container to our Docker network.

In simple words:

docker run = Create and start a container from a Docker image.

Dockerization
12. What is Dockerization?

Dockerization is the process of packaging an application, its dependencies, configuration, and runtime environment into a Docker image so that it can run consistently inside containers.

For example, our Python Kafka producer originally ran directly on Windows:

Windows
   ↓
Python
   ↓
producer.py
   ↓
Kafka

We Dockerized it:

Docker
   │
   └── Python Kafka Producer Container
             │
             ▼
           Kafka

We created:

producer.py
requirements.txt
Dockerfile

then:

docker build

created:

python-kafka-producer

and:

docker run

started the application inside a container.

In simple words:

Dockerization = Making an application ready to run inside Docker.

Apache Spark
13. Apache Spark

Apache Spark is a distributed data processing engine designed to process large amounts of data quickly.

Spark can process data from sources such as:

Kafka
Databases
Files
Cloud storage
APIs

For our future project, the architecture will look something like:

Python Producer
       ↓
     Kafka
       ↓
   Spark
       ↓
 Data Processing
       ↓
 Database / Output

For example, Kafka might continuously receive:

Order 1
Order 2
Order 3
Order 4
...

Spark can consume that data and perform operations such as:

Filter orders
Calculate total sales
Group by city
Calculate averages
Detect unusual transactions

In simple words:

Apache Spark = A distributed engine used to process and analyze large amounts of data.

Scala
14. Scala

Scala is a programming language that runs on the Java Virtual Machine (JVM).

Apache Spark was originally developed using Scala, and Scala is one of the primary languages used with Spark.

For example, Spark applications can be written using:

Scala
Python (PySpark)
Java
R

You don't need to become an expert in Scala before learning Spark.

For our learning path, we can primarily use Python + PySpark.

In simple words:

Scala = A JVM programming language that is closely associated with Apache Spark and is commonly used to build Spark applications.
