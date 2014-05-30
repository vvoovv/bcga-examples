from cga import *

height = 25
groundFloorHeight = 4
floorHeight = 3.5

@rule
def Lot():
	extrude(height)
	Building()

@rule
def Building():
	comp(f).into(
		front>>Facade() |
		side>>Facade()
	)

@rule
def Facade():
	split(y).into(
		groundFloorHeight>>Floor() |
		repeat(flt(floorHeight)>>Floor())
	)

@rule
def Floor():
	pass
