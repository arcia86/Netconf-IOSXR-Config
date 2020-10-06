#!/usr/bin/env python
"""
Generate a file name confi_file.txt with a fixed quantity of EVI on a IOS-XR device

Author: Alfredo Arcia

"""

from ncclient import manager
import xmltodict
import xml.dom.minidom
import os,sys
import time

netconf_head = """
<config>    
  <evpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2vpn-cfg">
   <enable></enable>
   <evpn-tables>
    <evpn-instances>"""
netconf_template = """     
     <evpn-instance>
      <vpn-id>{vlan}</vpn-id>   
      <encapsulation>evpn-encapsulation-mpls</encapsulation>
      <side>evpn-side-regular</side>
      <evpn-evi-cw-disable></evpn-evi-cw-disable>
      <evpn-instance-advertise-mac>
       <enable></enable>
      </evpn-instance-advertise-mac>
     </evpn-instance>"""
netconf_footer = """     
    </evpn-instances>
   </evpn-tables>
  </evpn>
</config>"""



qty = int(input("How many EVI do you want to create? "))
start = int(input("starting from ? "))


start_time = time.time()

with open('confi_file.txt', 'a') as f:
        print(netconf_head, end='' ,file=f)

for i in range(start,qty+start):
    netconf_data = netconf_template.format(
        vlan = str(i)
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