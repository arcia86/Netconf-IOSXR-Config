#!/usr/bin/env python
"""
Generate a file name confi_file.txt with a fixed quantity of L2VPN on a IOS-XR device

Author: Alfredo Arcia

"""

from ncclient import manager
import xmltodict
import xml.dom.minidom
import os,sys
import time

netconf_head = """
<config>    
  <l2vpn xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-l2vpn-cfg">
   <tcn-propagation></tcn-propagation>
   <enable></enable>
   <load-balance>source-dest-ip</load-balance>
   <database>"""
netconf_template = """    
    <bridge-domain-groups>
     <bridge-domain-group>
      <name>{name}</name>
      <bridge-domains>
       <bridge-domain>
        <name>{evpn}</name>
        <bd-attachment-circuits>
         <bd-attachment-circuit>
          <name>{subintvlan}</name>
         </bd-attachment-circuit>
        </bd-attachment-circuits>
        <bridge-domain-evis>
         <bridge-domain-evi>
          <vpn-id>{vlan}</vpn-id>
         </bridge-domain-evi>
        </bridge-domain-evis>
       </bridge-domain>
      </bridge-domains>
     </bridge-domain-group>
    </bridge-domain-groups>"""
netconf_footer = """
   </database>
  </l2vpn>
</config>"""


new_evpn = {}
qty = int(input("How many L2VPN do you want to create? "))
start = int(input("starting from ? "))
new_evpn["name"] = input("What bridge group name to add? ")


start_time = time.time()

with open('confi_file.txt', 'a') as f:
        print(netconf_head, end='' ,file=f)

for i in range(start,qty+start):
    netconf_data = netconf_template.format(
        name = new_evpn["name"] + str(i),
        subintvlan = 'Bundle-Ether4.' + str(i),     
        vlan = str(i),
        evpn = 'evpn_' + str(i)
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