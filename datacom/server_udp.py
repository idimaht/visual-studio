from socket import *

port = 9999
soc = socket(AF_INET, SOCK_DGRAM)
soc.bind(('0.0.0.0', port))

msg, addr = soc.recvfrom(1024)
msgDecoded = msg.decode()

print('{}:{} => {}'.format(addr[0], addr[1], msgDecoded))

soc.sendto(msgDecoded[::-1].encode(), addr)