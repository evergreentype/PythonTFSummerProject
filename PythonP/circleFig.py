import math

class FigSelec():

	def set_par(self,xFigSelected,xrad,xheight,xbase):
		self.rad=xrad
		self.FigSelected=xFigSelected
		self.height=xheight
		self.base=xbase

	def find_value(self):
		"""Controler method"""
		print(self.FigSelected)
		if self.FigSelected==4:
			return self.find_value4()
		elif self.FigSelected==1:
			return self.find_value1()
		elif self.FigSelected==2:
			return self.find_value2()
		elif self.FigSelected==3:
			return -1

class Area(FigSelec):
	"""compute Area of figures"""

	def find_value(self):
		"""Controler method"""
		print(self.FigSelected)
		if self.FigSelected==4:
			return self.find_value4()
		elif self.FigSelected==1:
			return self.find_value1()
		elif self.FigSelected==2:
			return self.find_value2()
		elif self.FigSelected==3:
			return -1

	def find_value1(self):
		return (self.height*self.base)/2

	def find_value2(self):
		return self.height*self.base
	def find_value3(self):
		return -1
	def find_value4(self):
		return math.pi*(self.rad**2)	

class perimetr(FigSelec):
	"""docstring for perimetr"""

	def find_value(self):
		"""Controler method"""
		print(self.FigSelected)
		if self.FigSelected==4:
			return self.find_value4()
		elif self.FigSelected==1:
			return self.find_value1()
		elif self.FigSelected==2:
			return self.find_value2()
		elif self.FigSelected==3:
			return -1

	def find_value1(self):
		return self.height+self.base+self.rad

	def find_value2(self):
		return 2*(self.height+self.base)
	def find_value3(self):
		return -1
	def find_value4(self):
		return math.pi*2*self.rad	