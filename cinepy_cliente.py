# -*- coding: utf-8 -*-
### KEY WORDS
# list
# sections
# confirm
# pay
 
### PARAMETERS
# typelist
# moviename
# choice
# myname mycard mycpf
# -- coding: utf-8 --
import socket

print('Informe o Cinema') # Endereço IP do Servidor
HOST = raw_input()
PORT = 5000                 # Porta que o servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('CTRL + X para sair')
while True:
    data = tcp.recv(1024)       # recebe até 1024 bytes do servidor (qualquer número >0)
    if(data):
        print repr(data)# exibe os dados recebidos do servidor
    
    msg = raw_input() 
    if (msg == '\x18'):
        break
    tcp.send (msg)

print('Obrigado pela Preferencia')
tcp.close