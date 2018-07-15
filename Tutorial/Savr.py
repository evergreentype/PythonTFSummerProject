


#list as matrix
dec=[2,3,4,5,6]
print(dec)
#-----------------------


#list processing
dec=[x**2 for x in dec]
#----------------------



#tuples
v = ([1, 2, 3], [3, 2, 1])
#tuples can contain mutable objects
#----------------------

#deal with element of matrix 
v[1][1]=5
print(v[1][1])
print(v)


#**
#Modules

#A module is a file containing Python definitions and statements.
#Module can contain other module
#
import sys
print('------------------------------------------------------------------------------')
#dir() is a function that explore to us all defined names
print(dir(sys))
print('==============================================================================')
print(dir())

#**
#Packages
#Packages are a way of structuring Python’s module namespace by using “dotted module names”
#For Example. import sound.effects.echo
#--------------------------------------
#Now what happens when the user writes from sound.effects import *?
#it will add all moudles that contains in __all__ of __init__ file
#but it also is a bad practice, because it can bring more other problems
#--------------------------------------


#**Input & Output
x='hello world'
print(str(x))
print(repr(x))

#str() and repr() are functions for command promt
#str() is showing human-readable information
#repr() is showing for debagging
import math
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
	print(str(name) + ' ==> '+ str(phone))
#we can use str() func for convert number type to str

yes_votes = 42
no_votes = 43
percentage = (yes_votes/(yes_votes+no_votes))
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))
#----------------------------------------

animals = 'eels'
people="peopls"
print('My hovercraft is full of {:.2f} and {}.'.format(math.pi,people))


year = 2016 ; event = 'Referendum'
print(f'Results of the {year} {event}')


#-----------------------------------------
pr=input()
