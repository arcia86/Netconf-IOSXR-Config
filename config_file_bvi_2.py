#!/usr/bin/env python
"""
Generate a file name confi_file.txt with a fixed quantity of BVI Interfaces on a IOS-XR device

Author: Alfredo Arcia

"""

from ncclient import manager
import xmltodict
import xml.dom.minidom
import os,sys
import time

netconf_head = """
<config>    
  <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">"""
netconf_template = """    
   <interface-configuration>
    <active>act</active>
    <interface-name>{BVI}</interface-name>
    <interface-virtual></interface-virtual>
    <description>{description}</description>
    <ipv4-network xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-io-cfg">
     <addresses>
      <primary>
       <address>154.2.39.217</address>
       <netmask>255.255.255.252</netmask>
      </primary>
     </addresses>
    </ipv4-network>
    <ipv4arp xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ipv4-arp-cfg">
     <purge-delay>120</purge-delay>
    </ipv4arp>
   </interface-configuration>"""
netconf_footer = """   
  </interface-configurations>
</config>"""


new_bvi = {}
qty = int(input("How many BVI interface do you want to create? "))
start = int(input("starting from ? "))
new_bvi["description"] = input("What description to use? ")


start_time = time.time()

with open('confi_file.txt', 'a') as f:
        print(netconf_head, end='' ,file=f)

for i in range(start,qty+start):
    netconf_data = netconf_template.format(
        BVI = 'BVI' + str(i),
        description = new_bvi["description"]
    )
    with open('confi_file.txt', 'a') as f:
        print(netconf_data, end='' ,file=f)

with open('confi_file.txt', 'a') as f:
        print(netconf_footer, end='' ,file=f)

# delete the first line of the file 

with open('confi_file.txt', 'r') as fin:
    data = fin.read().splitlines(True)
    
with open('confi_file.txt', 'w') as fout:
    fout.writelines(data[1:])

print("configure file is generate in --- execution %s seconds ---" % (time.time() - start_time))