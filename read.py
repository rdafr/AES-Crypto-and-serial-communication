import serial
import time
import json
from Crypto.Cipher import AES

key = 'abcdefghijklmnop'

while 1:
	ser = serial.Serial('/dev/ttyUSB0',115200)


	x = ser.read(16)
#	x = ser.readline()
#	if(x!=0):
#		decipher = AES.new(key, AES.MODE_ECB)
#		print(decipher.decrypt(x))



	#with open('configuracoes_medidor.json','w') as outfile:
        #	json.dump(x, outfile)
	print(x)
	time.sleep(1)
 
