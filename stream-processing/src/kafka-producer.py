from confluent_kafka import Producer
import json

kafka_brokers='localhost:9092'
topic='mock-data'
data = './mock_data.json'

# read mock_data
with open(data, 'r') as datafile:
    json_data=datafile.read()
    
# parse file
items = json.loads(json_data)

p = Producer({
               'bootstrap.servers': kafka_brokers,
               'queue.buffering.max.messages': 100000,
               'queue.buffering.max.ms': 500, #
               'batch.num.messages': 100 #
             }) if kafka_brokers else None

for item in items:
    try:        
        if p is not None:
            print("No of msg waiting to be delivered to broker:" + str(p.__len__()))
            # produce() is asynchronous
            # enqueue the message on an internal queue
            # flush() after each produce() effectively a sync producer 
            p.produce(topic, str(item).encode('utf-8'))

            # flush() is not used! flush() will block until the previously sent 
            #messages have been delivered (or errored), effectively making the producer synchronous
            p.poll(0) 
        else:
            print("Producer is not created!!!")
            exit(1)
    except KeyboardInterrupt:
            if p is not None:
                p.flush()
    except BufferError as e:
        print(e, file=sys.stderr)
        print("POLL for 1 seconds")

        # putting the poll() block until there is queue space available. blocks for 1 seconds
        # block for as long as makes sense depending on the application 
        # (preferably longer) since message delivery can take some time if there are temporary errors on the broker (e.g., leader failover)
        p.poll(1)
        # data for which there was exception, not yet added to the internal Queue
        p.produce(topic, str(item).encode('utf-8'))
    finally:
        if p is not None:
            p.flush()