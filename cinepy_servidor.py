from socket import *

HOST = 'localhost'
PORT = 8010
BUFSIZ = 1024
ADDR = (HOSTPORT)

tcpSerSock = socket(AF_INETSOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while 1:
    print "esperando ligacao"
    tcpCliSockaddr = tcpSerSock.accept()
    print "ligado a: "addr

while 1:
    data = tcpCliSock.recv(BUFSIZ)
    if not data: break
    tcpCliSock.send("recebendo... >" + data)

tcpCliSock.close()
tcpSerSock.close()