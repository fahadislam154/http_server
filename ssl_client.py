#!/usr/bin/env python
#
# This script serves as a simple TLSv1 client for 15-441
#
# Authors: Athula Balachandran <abalacha@cs.cmu.edu>,
#          Charles Rang <rang972@gmail.com>,
#          Wolfgang Richter <wolf@cs.cmu.edu>

import pprint
import socket
import ssl

# try a connection
sock = socket.create_connection(('localhost', 4443))  #4949 is old port
#tls = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_REQUIRED,
#                            ca_certs='../certs/signer.crt',
#                            ssl_version=ssl.PROTOCOL_TLSv1)
pprint.pprint('start conn wrap on python socket');

tls = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_REQUIRED,
                            ca_certs='./myca.crt',
                            ssl_version=ssl.PROTOCOL_TLSv1)

# what cert did he present?
pprint.pprint('connected so going to try to get cert DETAILS');
pprint.pprint(tls.getpeercert())

#tls.sendall('this is a test message')
tls.sendall('GET / HTTP/1.1\r\n\r\n')
pprint.pprint(tls.recv(4096).split("\r\n"))
pprint.pprint(tls.recv(4096))
tls.close()



# try another connection!
sock = socket.create_connection(('localhost', 4443))
#tls = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_REQUIRED,
#                            ca_certs='../certs/signer.crt',
#                            ssl_version=ssl.PROTOCOL_TLSv1)
tls = ssl.wrap_socket(sock, cert_reqs=ssl.CERT_REQUIRED,
                            ca_certs='./myca.crt',
                            ssl_version=ssl.PROTOCOL_TLSv1)

#tls.sendall('this is a test message!!!')


tls.sendall('GET /www/cgi/adder.cgi?m=5&n=6 HTTP/1.1\r\n\r\n')
pprint.pprint(tls.recv(4096).split("\r\n"))
pprint.pprint(tls.recv(4096))
tls.close()

exit(0)
