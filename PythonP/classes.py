import math

class Math_Obj:
	""" Main Class """
	name="figure"

	def area(self,name):
		print('find area')
		return self.identify(True,name)


	def perimetr(self,name):
		print('find perimetr')
		return self.identify(False,name)

	def identify(self,switch,nameFig):
		if nameFig=="Circle" or nameFig=="circle":
			circle=Circle()
			if switch:
				return circle.area()
			else:
				return circle.perimetr()
			#print(f'{circle.area():.2f} cm^2')
			#print(f'{circle.perimetr():.2f} cm')
		elif nameFig=="Parallelogram" or nameFig=="parallelogram":
			parallelogram=Parallelogram()
			if switch:
				return parallelogram.area()
			else:
				return parallelogram.perimetr()
			#print(f'{parallelogram.area():.2f} cm^2')
			#print(f'{parallelogram.perimetr():.2f} cm')
		elif nameFig=="Triangle" or nameFig=="triangle":
			triangle=Triangle()
			if switch:
				return triangle.area()
			else:
				return triangle.perimetr()
			#print(f'{triangle.area():.2f} cm^2')
			#print(f'{triangle.perimetr():.2f} cm')


class Circle(Math_Obj):
	name="Circle"
	radius=0

	def area(self):
		print('input radius: ')
		Circle.radius=int(input())
		return math.pi*Circle.radius**2

	def perimetr(self):
		return 2*math.pi*Circle.radius

class Parallelogram(Math_Obj):
	name="Paralellogram"
	base=0
	height=0

	def area(self):
		print('input base: ')
		Parallelogram.base=int(input())
		print('input height: ')
		Parallelogram.height=int(input())
		return Parallelogram.base*Parallelogram.height

	def perimetr(self):
		return 2*(Parallelogram.base+Parallelogram.height)

class Triangle(Math_Obj):
	name="Triangle"
	height=0
	side1=0
	side2=0
	side3=0

	def area(self):
		print('input base: ')
		Triangle.side1=int(input())
		print('input height: ')
		Triangle.height=int(input())
		return Triangle.side1*Triangle.height/2

	def perimetr(self):
		switch=True
		while switch:
			print('input side2: ')
			Triangle.side2=int(input())
			print('input side3: ')
			Triangle.side3=int(input())
			if Triangle.side1+Triangle.side2>Triangle.side3 and Triangle.side2+Triangle.side3>Triangle.side1 and Triangle.side1+Triangle.side3>Triangle.side2:
				switch=False
			else:
				switch=True
				print('You etered incorrect data, pls try again')
		return self.side1+self.side2+self.side3