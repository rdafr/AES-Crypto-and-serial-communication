import serial
import time
import json
from Crypto.Cipher import AES

key = 'abcdefghijklmnop'
cipher = AES.new(key, AES.MODE_ECB)

ser = serial.Serial(
	port = '/dev/ttyS0',
	baudrate = 115200
)

j={"oi":"abcdef"}


print(ser.name)

while 1:
	
	#cm = raw_input('Digite a string: \n')
	msg = json.dumps(j)
	cm = cipher.encrypt(msg)
	ser.write(cm)
	time.sleep(1)



