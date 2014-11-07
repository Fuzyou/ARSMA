import smbus, time
import datetime, locale
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

dt = datetime.datetime.now()
time_start = str(dt)

while True:

	f = open(time_start, 'a')

	i2c= smbus.SMBus(1)
	i2c.write_byte_data(0x70, 0, 81)
	time.sleep(0.07)
	dist = i2c.read_word_data(0x70, 2) /255
	print (dist)

	time_now = datetime.datetime.now() - dt
	data = str(dist) + " elapsed:" + str(time_now) + "\n"


	f.write(data),'\n'
	status = GPIO.input(4)
	if status == False:
		break

f.close()
