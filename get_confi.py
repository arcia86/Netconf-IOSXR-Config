#!/usr/bin/env python
"""
retrieve the capability information of the device using  Netconf and save in the 
actual directory as output.txt 

Author: Alfredo Arcia 
"""

from ncclient import manager
import xmltodict
import xml.dom.minidom
import os,sys
import time
import yaml

# open login file for credentials

with open("login.yaml") as f:
    config = yaml.safe_load(f.read())

host_ip = config["host_ip"]
host_port = config["host_port"]
username = config["host_username"]
password = config["host_password"] 


with manager.connect(
        host = host_ip,
        port = host_port,
        username = username,
        password = password,
        hostkey_verify=False,
        device_params={'r1': 'iosxr'},
        allow_agent=False,
        look_for_keys=False
        ) as m:
    netconf_reply = m.get_config(source = 'running')
    with open('output.txt', 'w') as f:
        print(netconf_reply.xml, file=f)
