"""import socket
#socket is used for connecting to a server , getting a response and sending a request
#managing network in python uses protocols like TCP and UDP

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#creating an object mysock
#socket.AF_INET specifies that it will be using IPv4
#socket.SOCK_STREAM specifies that it will be using TCP protocol

mysock.connect(('data.pr4e.org', 80))
#establishes a connection to the server data.pr4e.org at port 80(port nnumber for http)

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
#preparres the HTTP GET request AT the URL specified above
#HTTP/1.0 is the HTTP version being used
#\r\n: Indicates the end of the request line.
#\r\n: A second blank line, signaling the end of the HTTP headers.
#.encode(): Converts the string into bytes because the socket requires binary data to send over the network.

mysock.send(cmd)
#sends the request 

while True:
    data = mysock.recv(512)
    #Reads up to 512 bytes of data from the socket.
    #The recv method receives data from the server. 

    if len(data) < 1:
        break
    print(data.decode(),end='')
    #data.decode(): Converts the received bytes into a string using the default encoding (UTF-8).

    
mysock.close()"""

import urllib.request  ,urllib.parse, urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts[word],counts)
