#!/usr/bin/python
# -*- coding: utf-8 -*-

from mqtt_lib import MQTT_Client 
import os
import argparse


""" Parse command line arguments. """

parser = argparse.ArgumentParser()

parser.add_argument('-pub', '--publish', action='store_true', help="publisher client mode")
parser.add_argument('-sub', '--subscribe', action='store_true', help="subscriber client mode")
parser.add_argument('-H', '--host', required=False, default="127.0.0.1")
parser.add_argument('-t', '--topic', required=False, default="#")
parser.add_argument('-q', '--qos', required=False, type=int, default=0)
parser.add_argument('-c', '--clientid', required=False, default=None)
parser.add_argument('-u', '--username', required=False, default=None)
parser.add_argument('-d', '--disable-clean-session', action='store_true', help="disable 'clean session' (sub + msgs not cleared when client disconnects)")
parser.add_argument('-p', '--password', required=False, default=None)
parser.add_argument('-P', '--port', required=False, type=int, default=None, help='Defaults to 8883 for TLS or 1883 for non-TLS')
parser.add_argument('-N', '--nummsgs', required=False, type=int, default=1, help='send this many messages before disconnecting') 
parser.add_argument('-m', '--message', required=False, default=None, help='message to send before disconnecting')
parser.add_argument('-S', '--delay', required=False, type=float, default=1, help='number of seconds to sleep between msgs') 
parser.add_argument('-k', '--keepalive', required=False, type=int, default=60)
parser.add_argument('-s', '--use-tls', action='store_true')
parser.add_argument('--insecure', action='store_true')
parser.add_argument('-F', '--cacerts', required=False, default=None)
parser.add_argument('--tls-version', required=False, default=None, help='TLS protocol version, can be one of tlsv1.2 tlsv1.1 or tlsv1\n')
parser.add_argument('-D', '--debug', action='store_true')

args, unknown = parser.parse_known_args()

""" Create client. """
mqttc = MQTT_Client(args)

""" Process according client mode. """
topic = args.topic
qos = args.qos

if args.subscribe and not args.publish:
    #If more than one topic, use the method subscribe as many times as needed
    mqttc.subscribe(topic, qos)
    mqttc.loop_forever()
elif args.publish and not args.subscribe:
    mqttc.loop_start()

    """ Sample messages (through code or command line). """
    for x in range (0, args.nummsgs):
        #msg_txt = '{"msgnum": "'+str(x)+'"}'
        msg_txt = args.message
        print("Publishing: "+msg_txt)
        mqttc.publish(topic, qos, msg_txt)   

    mqttc.disconnect()
else:
    print ("Unknown client mode.")