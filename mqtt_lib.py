#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import os
import ssl
import time

class MQTT_Client(object):
    """
    Creates MQTT Client Instance.

    Args:
        args (argparse): Command Line Arguments.
    """
    def __init__(self, args):
        self.args = args
        self.mqttc = create_MQTT_Client(args)

    def loop_start(self):
        """ Starts a new thread to process network traffic. """
        self.mqttc.loop_start()

    def disconnect(self):
        """ Disconnects MQTT client from broker. """
        self.mqttc.disconnect()

    def loop_forever(self):
        """ Infinite blocking loop to process network traffic. """
        self.mqttc.loop_forever()
    
    def publish(self, msg):
        """
        Publish message to broker.

        Args:
            msg (str): message to send.
        
        Returns:

        """
        infot = self.mqttc.publish(self.args.topic, msg, qos=self.args.qos)
        infot.wait_for_publish()

        time.sleep(self.args.delay)
    
    def subscribe(self):
        """ Subscribe to a given topic. """
        self.mqttc.subscribe(self.args.topic, self.args.qos)

def on_connect(mqtcc, obj, flags, rc):
    """ Called when the broker responds to our connection request. """
    print("connect rc: " + str(rc))


def on_message(mqtcc, obj, msg):
    """ Called when a message has been received on a topic that the client subscribes to. """
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqtcc, obj, mid):
    """ Called when a message that was to be sent using the publish method has completed transmission to the broker. """
    print("mid: " + str(mid))


def on_subscribe(mqtcc, obj, mid, granted_qos):
    """ Called when the broker responds to a subscribe request. """
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqtcc, obj, level, string):
    """ Called when the client has log information. Defined to allow debugging. """
    print(string)

def create_MQTT_Client(args):
    """
        Creates an MQTT client based on given arguments and establishes a connection with the broker.

        Args:
            args (argparse): Command Line Arguments.
        
        Returns: 
            mqttc : MQTT client
    """

    usetls = args.use_tls

    if args.cacerts:
        usetls = True

    port = args.port    
    if port is None:
        if usetls:
            port = 8883
        else:
            port = 1883

    mqttc = mqtt.Client(args.clientid,clean_session = not args.disable_clean_session)

    if usetls:
        if args.tls_version == "tlsv1.2":
            tlsVersion = ssl.PROTOCOL_TLSv1_2
        elif args.tls_version == "tlsv1.1":
            tlsVersion = ssl.PROTOCOL_TLSv1_1
        elif args.tls_version == "tlsv1":
            tlsVersion = ssl.PROTOCOL_TLSv1
        elif args.tls_version is None:
            tlsVersion = None
        else:
            print ("Unknown TLS version - ignoring")
            tlsVersion = None

        if not args.insecure:
            cert_required = ssl.CERT_REQUIRED
        else:
            cert_required = ssl.CERT_NONE
            
        mqttc.tls_set(ca_certs=args.cacerts, certfile=None, keyfile=None, cert_reqs=cert_required, tls_version=tlsVersion)

        if args.insecure:
            mqttc.tls_insecure_set(True)

    if args.username or args.password:
        mqttc.username_pw_set(args.username, args.password)

    mqttc.on_message = on_message
    mqttc.on_connect = on_connect
    mqttc.on_publish = on_publish
    mqttc.on_subscribe = on_subscribe

    if args.debug:
        mqttc.on_log = on_log

    print("Connecting to "+args.host+" port: "+str(port))
    mqttc.connect(args.host, port, args.keepalive)

    return mqttc
