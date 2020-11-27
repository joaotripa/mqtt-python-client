# MQTT Python Client Example (Eclipse Paho) 

A MQTT client example based on Eclipse Paho MQTT Python examples.

For more information see (https://github.com/eclipse/paho.mqtt.python)

## Prerequisites

MQTT broker running:   
* on a local machine   
* in a cloud environment

Paho MQTT python library  
```pip install paho-mqtt```

## Command Line Options

[-h] - Help  
[-pub] - Publisher mode  
[-sub] - Subscriber mode  
[-H HOST] - MQTT broker host (Defaults to 127.0.0.1)  
[-t TOPIC] - Topic to publish/subscribe (Defaults to #)  
[-q QOS] - Quality of Service (QOS) (Defaults to 0)  
[-c CLIENTID] - Client ID  
[-u USERNAME] - username for client authentication on the broker  
[-p PASSWORD] - password for client authentication on the broker  
[-d] - Disable clean session (Subscriptions and messages are not cleared when client disconnects)  
[-P PORT] - Port number used to communicate with broker (Defaults to 8883 for TLS or 1883 for non-TLS)  
[-N NUMMSGS] - Number of messages to send (Defaults to 1)  
[-m MESSAGE] - Message to publish  
[-S DELAY] - Number of seconds to sleep between messages (Defaults to 1)  
[-k KEEPALIVE] - Maximum length of time that the broker and client may not communicate with each other before sending a ping request.  
[-s] - Use Transport Layer Security (TLS)  
[--tls-version TLS_VERSION] - Transport Layer Security (TLS) version.  
[--insecure] - Disables host-name verification in the certificates presented by the broker.  
[-F CACERTS] - Provide a CA (Certificate Authority) certificate.  
[-D] - Debug mode.  

## Running as Subscriber

If running mqtt locally use the 127.0.0.1 address, else use the correct mqtt broker address
```python3 mqtt_cli.py -sub -H 127.0.0.1 -t test/topic```

## Running as Publisher

If running mqtt locally use the 127.0.0.1 address, else use the correct mqtt broker address
```python3 mqtt_cli.py -pub -H 127.0.0.1 -t test/topic -m "Hello World!" ```

