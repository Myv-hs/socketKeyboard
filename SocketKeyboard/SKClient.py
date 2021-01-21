import sys
import socket               
import keyboard

trgtIP = '192.168.1.9'
port = 12346
toggle = False
toggleKey = 'delete'

if len(sys.argv)>1:
	inputIP = sys.argv[1]
	trgtIP = inputIP
	print("You've chosen to connect to: "+trgtIP)

def sendKey (e):
	global toggle
	global port
	global trgtIP
	s = socket.socket()         

	if e.name == toggleKey and e.event_type == 'down':
		toggle = not toggle
		print("Key Transfer on: "+str(toggle))

	if toggle == True and e.name !=toggleKey:
		keyname = e.name
		key = e.event_type+" "+keyname
		try:
			s.connect((trgtIP, port))
			s.send(key.encode())
		except:
			print("Socket failed, check input IP is correct\nand target SKServer.py is ready")

keyboard.hook(sendKey)
keyboard.wait()