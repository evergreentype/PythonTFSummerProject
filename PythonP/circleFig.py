import baseClasses
import math

class FigSelec(baseClasses.MathObject):

	def __init__(self,FigSelected,rad,height,base):
		self.rad=rad
		self.FigSelected=FigSelected
		self.height=height
		self.base=base

	def find_value(self):
		if self.FigSelected==4:
			area=Area(self.FigSelected,self.rad,self.height,self.base)
			return area.find_value()
		elif self.FigSelected==1:
			area=Area(self.FigSelected,self.rad,self.height,self.base)
			return area.find_value()
		elif self.FigSelected==2:
			area=Area(self.FigSelected,self.rad,self.height,self.base)
			return area.find_value()

class Area(FigSelec):
	"""compute Area of figures"""
	def __init__(self,FigSelected,rad,height,base):
		self.rad=rad
		self.height=height
		self.base=base
		self.FigSelected=FigSelected

	def find_value(self, *args):
		"""Controler method"""
		if self.FigSelected==4:
			return self.find_value4()
		elif self.FigSelected==1:
			return self.find_value1()
		elif self.FigSelected==2:
			return self.find_value2()
		elif self.FigSelected==3:
			pass

	def find_value1(self):
		return (self.height*self.base)/2

	def find_value2(self):
		return self.height*self.base
	def find_value3(self):
		pass
	def find_value4(self):
		return math.pi*(self.rad**2)	
