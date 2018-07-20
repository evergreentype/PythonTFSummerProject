import circleFig
import baseClasses

print('Choose figure')
fig=('triangle','parallelogram','cube','circle')


for x in range(1,5):
	print(str(x)+'-'+fig[x-1])

FigSelected=int(input())
print(fig[int(FigSelected)-1]+' was choosen')
radius=0
base=0
height=0
if FigSelected==4:
	print('input radius ')
	radius=int(input())
elif FigSelected==1:
	print('input height ')
	height=int(input())
	print('input base ')
	base=int(input())
elif FigSelected==2:
	print('input height ')
	height=int(input())
	print('input base1 ')
	base=int(input())
	print('input base2')
	base+=int(input())
circleFig=circleFig.FigSelec(FigSelected,radius,base,height)
print("{:.1f} cm^2".format(circleFig.find_value()))