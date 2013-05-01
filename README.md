
# Python ADDP library and utilities

## About

The Advanced Device Discovery Protocol (ADDP) is used to discover ADDP
aware devices on the local network.

This module provides both a library for using ADDP in your own
applications, as well as two test utilities -- one to discover ADDP
devices and one to respond to ADDP discovery requests.

## Example

Running `python discover.py` on a network with the
`device.py` script and a Digi ConnectPort X4:

    > python discover.py
	Sending discover message...
    [{'addp_ip': '192.168.1.102',
     'code': 1,
     'mac': (255, 255, 255, 255, 255, 255),
     'message': 'Discovery Request',
     'msg_len': 6,
     'msg_type': 'request'},
    {'Encrypted Real Port number': 1027,
     'Firmware': 'V.1 04-25-2013',
     'HW Revision': 0,
     'IP Gateway': (1, 1, 1, 1),
     'IP address': (1, 1, 1, 1),
     'MAC address': (0, 0, 0, 0, 0, 0),
     'Netmask': (255, 255, 255, 0),
     'Network Name': 'test',
     'Real Port number': 771,
     'Serial Port Count': 1,
     'addp_ip': '192.168.1.102',
     'code': 2,
     'device name': 'ADDP Emulator',
     'message': 'Discovery Response',
     'msg_len': 81,
     'msg_type': 'response'},
    {'DNS IP address': (0, 0, 0, 0),
     'Device-ID': '00000000-00000000-00409DFF-FF300000',
     'Encrypted Real Port number': 1027,
     'Firmware': 'Version 82001536_K 10/18/2011',
     'HW Revision': 0,
     'IP Gateway': (192, 168, 1, 3),
     'IP address': (192, 168, 1, 7),
     'MAC address': (0, 64, 157, 00, 000, 000),
     'Netmask': (255, 255, 255, 0),
     'Real Port number': 771,
     'Serial Port Count': 1,
     'UNKNOWN16': 1,
     'UNKNOWN19': 1,
     'addp_ip': '192.168.100.7',
     'code': 2,
     'device name': 'ConnectPort X4',
     'message': 'Discovery Response',
     'msg_len': 139,
     'msg_type': 'response'}]
