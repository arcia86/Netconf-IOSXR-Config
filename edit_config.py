#!/usr/bin/env python
"""
Load configuration based on confi_file.txt file in xlm 

Using Netconf for a IOS-XR device. 

Author: Alfredo Arcia.
"""

from ncclient import manager
import xmltodict
import xml.dom.minidom
import os,sys
import time
import yaml

# set initial time
start_time = time.time()

# open login file for credentials

with open("login.yaml") as f:
    config = yaml.safe_load(f.read())

host_ip = config["host_ip"]
host_port = config["host_port"]
username = config["host_username"]
password = config["host_password"] 

# open configuration file in the same directory

with open('confi_file.txt', 'r', newline=None) as file:
    netconf_template = file.read()

# open conection and edit configuration on the device.

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
    netconf_reply = m.edit_config(config=netconf_template, target='candidate', default_operation='merge')
    m.commit()
    print('**** configuration merged successfully ****')

print("--- execution %s seconds ---" % (time.time() - start_time))