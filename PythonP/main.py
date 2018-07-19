import funClasses
import rectangularFigures

print('Choose figure')
fig=('rectangle','square','cube','circle')

for x in range(1,5):
	print(str(x)+'-'+fig[x-1])
FigSelected=input()
print(fig[int(FigSelected)-1]+' was choosen')