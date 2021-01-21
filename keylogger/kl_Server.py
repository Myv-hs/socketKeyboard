import socket
import keyboard     

shift_state = False

def down(key):
	try:
		#if not keyboard.is_pressed(key):
		if key == '?':
			keyboard.write('?', delay=0, restore_state_after=True, exact=True)
			print("write ?")
		elif key =='asciicircum':
			keyboard.write('^', delay=0, restore_state_after=True, exact=True)
			print("^")
		else :	
			keyboard.press(key)
	except:
		print("Key Invalid")

def up(key):
	try:
		#if keyboard.is_pressed(key):
		keyboard.release(key)
	except:
		print("Invalid Key releaed")

s = socket.socket()         
port = 12346                

s.bind(('', port))        
print("socket binded to %s" %(port))
s.listen(5)     
print("socket is listening")            

while True:
	c, addr = s.accept()     
	print('Got keyevent from', addr)

	instring = c.recv(4096).decode()
	#instring = int(instring)
	#keyboard.press(instring)
	if instring:
		print(type(instring))
		print(instring)
		if len(instring.split(' '))>1:
			eventtype = instring.split(' ')[0]
			if eventtype == 'down':
				down(instring.split(' ')[1])
			elif eventtype == 'up':
				up(instring.split(' ')[1])