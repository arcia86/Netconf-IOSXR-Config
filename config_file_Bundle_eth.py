#!/usr/bin/env python
"""
Generate a file name confi_file.txt with a fixed quantity of  sub Bundle eth on a IOS-XR device

all over Bundle-Ether1.x 

Author: Alfredo Arcia 
"""

from ncclient import manager
import xmltodict
import xml.dom.minidom
import os,sys
import time

netconf_head = """
<config>    
  <interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg">
   <interface-configuration>
    <active>act</active>
    <interface-name>Bundle-Ether1</interface-name>
    <interface-virtual></interface-virtual>
   </interface-configuration>"""
netconf_template = """
   <interface-configuration>
    <active>act</active>
    <interface-name>{subintvlan}</interface-name>
    <interface-mode-non-physical>l2-transport</interface-mode-non-physical>
    <description>{description}</description>
    <ethernet-service xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2-eth-infra-cfg">
     <encapsulation>
      <outer-tag-type>match-dot1q</outer-tag-type>
      <outer-range1-low>{vlan}</outer-range1-low>
      <exact></exact>
     </encapsulation>
     <rewrite>
      <rewrite-type>pop1</rewrite-type>
     </rewrite>
    </ethernet-service>
   </interface-configuration>""" 
netconf_footer = """  
  </interface-configurations> 
</config>"""


new_bundle = {}
qty = int(input("How many bundle ethernet do you want to create? "))
start = int(input("starting from ? "))
new_bundle["description"] = input("What description to use? ")

start_time = time.time()

with open('confi_file.txt', 'a') as f:
        print(netconf_head, end='' ,file=f)

for i in range(start,qty+start):
    netconf_data = netconf_template.format(
        subintvlan = 'Bundle-Ether1.' + str(i),
        vlan = str(i),
        description = new_bundle["description"]
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