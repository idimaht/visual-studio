from socket import *

port = 9999

soc = socket(AF_INET, SOCK_STREAM)
soc.bind(('0.0.0.0', port))
soc.listen()

client, clientAddr = soc.accept()


msg = client.recv(1024)
msgDecoded = msg.decode()

print('{}:{} => {}'.format(clientAddr[0], clientAddr[1], msgDecoded))

client.send(msgDecoded[::-1].encode())