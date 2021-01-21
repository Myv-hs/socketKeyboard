import socket
import keyboard     

s = socket.socket()         
port = 12346                

s.bind(('', port))        
s.listen(5)     

while True:
	c, addr = s.accept()     
	instring = c.recv(4096).decode()
	print('Got keyevent from', addr, instring)