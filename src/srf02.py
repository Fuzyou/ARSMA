import smbus,time,datetime

class srf02:
	
	def __init__(self):
		self.i2c = smbus.SMBus(1)

		self.addr = 0x70

	def getValues(self, numberOfValues):
		startTime = datetime.datetime.now()
		values = []

		for i in range(numberOfValues):
			self.i2c.write_byte_data(self.addr, 0, 81)
			time.sleep(0.08)


			distance = self.i2c.read_word_data(self.addr, 2) / 255
			mindistance = self.i2c.read_word_data(self.addr, 4) / 255
			elapsed = datatime.datatime.now() - startTime
			values.append({"elapsed":elapsed, "distance": distance, "mindistance": mindistance})
			time.sleep(0.12)

		return values
	
	def printValues(self, numberOfValues):
		print("time,range,minRange")
		values = self.getValues(numberOfValues)
		for value in values:

			print(str(value["elapsed"].second) + "." + str(value["elapsed"].microsecond) + str(value["distance"]) + "," + str(value["mindistance"]))
	
