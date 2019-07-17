class Car:
	def __init__(self, color="grey", type="sedan"):
		self.color = color
		self.type = type
		
		self.passengers = []
		
	def addPassenger(self, name="person"):
		self.passengers.append(name)
		
	def removePassenger(self, name="person"):
		if name in self.passengers:
			i = self.passengers.index(name)
			self.passengers.pop(i)
	
	def __str__(self):
		s = self.color.title() + " " + self.type + " containing"
		if self.passengers:
			s += " passenger(s): ["
			for passenger in self.passengers:
				s += passenger + " "
			s += "]"
		else:
			s += "no passengers"
		s += "."
		return s
	