from socket import *

# alterar abaixo para o IP do servidor
HOST = '192.168.0.10'
PORT = 8010
BUFSIZ = 1024
ADDR = (HOSTPORT)

tcpCliSock = socket(AF_INETSOCK_STREAM)
tcpCliSock.connect(ADDR)

while 1:
    data = raw_input('>')
    if not data: break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data: break
    print "ligado a "ADDR" - dados - "data

tcpCliSock.close()