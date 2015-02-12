__author__ = 'talluri'
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind('localhost')

s.listen(1)

request, clientAddress = s.accept()

print request, clientAddress
