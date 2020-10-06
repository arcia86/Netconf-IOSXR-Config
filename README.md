# Netconf-IOSXR-Config
configuration Cisco IOS-XR device using Netconf

## Getting Started

you need to perform the following steps: 
	create your virtual environment:
			python3 -m venv venv
			pip install ncclient, xmltodict, xml.dom.minidom
	modify the login file with your device credentials
	execute the config_file_*.py that you desired created.
	this script will create a file name config:file.txt
	execute the edit_config.py to applied the config on the device.

