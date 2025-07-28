from fastapi import FastAPI
import pika

app = FastAPI()

@app.get("/")
def read_root():
    connection = pika.BlockingConnection(pika.ConnectionParameters("rabbitmq"))
    channel = connection.channel()
    channel.queue_declare(queue="test")
    channel.basic_publish(exchange="", routing_key="test", body="Hello from FastAPI!")
    connection.close()
    return {"message": "Sent to RabbitMQ"}
