import classes
import math


print('input name of figure (circle,parallelogram, triangle)')
name=input()
figure=classes.Math_Obj()
print(f'{figure.area(name):.2f} cm^2')
print(f'{figure.perimetr(name):.2f} cm')