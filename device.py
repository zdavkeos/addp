#!/usr/bin/env python

"""
Emulate a device running the ADDP service

Device is discoverable by the "Digi Device Discovery" program
"""

import sys
import struct
import socket

from addp import parse_frame, build_response

if __name__ == "__main__":
	HOST, PORT = "224.0.5.128", 2362

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	try:
		sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
	except AttributeError:
		pass
	mreq = struct.pack("4sI", socket.inet_aton(HOST),
					   socket.INADDR_ANY)
	sock.setsockopt(socket.IPPROTO_IP,
						   socket.IP_ADD_MEMBERSHIP, mreq)

	sock.bind(("", PORT))

	sys.stderr.write('Listening for ADDP requests on port {0}, Ctrl-C to stop.\n'.format(PORT))
	while True:
		try:
			data, addr = sock.recvfrom(2048)
		except KeyboardInterrupt:
			print 'Exiting...'
			sys.exit(0)

		if data is None or data == '':
			break

		info = parse_frame(data)

		if info:
			print 'Responing to discover from', addr
			ret = build_response(info)
			if ret and ret != "":
				sock.sendto(ret, addr)

