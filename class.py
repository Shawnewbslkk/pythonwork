class Car():
	def __init__(self,length,color,weigh):
		self.length=length
		self.color=color
		self.weigh=weigh

	def car_use(self):
		caruse=str(self.length) + self.color + str(self.weigh)
		return caruse

first_car=Car(1,'red',1)
print(first_car.car_use())

