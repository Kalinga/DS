import sys, os, re
import json
import time

from kafka import KafkaConsumer, TopicPartition

topic_name = 'mock-data'
consumer = KafkaConsumer(consumer_timeout_ms=1000)
consumer.assign([TopicPartition(topic_name, 0)])
consumer.seek_to_beginning()

for message in consumer:
  message_bytes = message.value
  message_string = message_bytes.decode()
 
  message_string = message_string.replace("\'", "\"")
 
  ## For plain text below code shall give error
  ## Only to be used for json values
  try:
    message_object = json.loads(message_string)
    time.sleep(.1)
    print("...................................") 
    print("Id: ", message_object["id"])
    print("Name: ", message_object["first_name"] + " " + message_object["last_name"])
    print("Email: ", message_object["email"])
    print("Sex: ", message_object["gender"])
    print("IP: ", message_object["ip_address"])
    print("Date: ", message_object["date"])
    print("Place: ", message_object["country"])
  except json.decoder.JSONDecodeError as e:
    print("Error: ", e)


# if consumer doesn't see any message for 1 second it will close the session.
consumer.close()
exit(0)
