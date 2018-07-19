import baseClasses
import math

class FigSelec(baseClasses.MathObject):

	def __init__(self):
		pass

	def find_value(self,FigSelected,rad):
		print('FigSele2323232c')	
		return Area.find_value()
		if FigSelected==4:
			Area=circleFig.Area(rad)
			print('12312')
			return Area.find_value()

class Area(FigSelec):
	"""compute Area of figures"""
	def __init__(self,rad):
		self.rad=rad

	def find_value(self):
		print('asdFigSelec')
		print(math.pi*(self.rad**2))
		return math.pi*(self.rad**2)