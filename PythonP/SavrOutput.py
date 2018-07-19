import circleFig
import baseClasses

print('Choose figure')
fig=('rectangle','square','cube','circle')


for x in range(1,5):
	print(str(x)+'-'+fig[x-1])
FigSelected=input()
print(fig[int(FigSelected)-1]+' was choosen')
print('input radius')
radius=input()
circleFig=circleFig.FigSelec()
print(circleFig.find_value(FigSelected,radius))
