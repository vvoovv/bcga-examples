from pro import *

height = param(random(20, 40))
groundFloorHeight = param(4)
floorHeight = param(3.5)
tileWidth = param(3)
windowColor = param("#0000ff")
wallColor = "#fefefe"


@rule
def Lot():
	extrude(height)
	Building()

@rule
def Building():
	decompose().into(
		front>>FrontFacade(),
		side>>SideFacade(),
		top>>Roof()
	)

@rule
def FrontFacade():
	split(y).into(
		groundFloorHeight>>GroundFloor(),
		repeat(flt(floorHeight)>>Floor())
	)

@rule
def SideFacade():
	split(y).into(
		groundFloorHeight>>Floor(),
		repeat(flt(floorHeight)>>Floor())
	)

@rule
def Roof():
	color("#eeeeee")

@rule
def GroundFloor():
	split(x).into(
		1>>Wall(),
		repeat(flt(tileWidth)>>Tile()),
		flt(tileWidth)>>EntranceTile(),
		1>>Wall()
	)

@rule
def Floor():
	split(x).into(
		1>>Wall(),
		repeat(flt(tileWidth)>>Tile()),
		1>>Wall()
	)

@rule
def Tile():
	split(x).into(
		flt(1)>>Wall(),
		2>>split(y).into(1>>Wall(), 1.5>>Window(), flt(1)>>Wall()),
		flt(1)>>Wall()
	)

@rule
def EntranceTile():
	split(x).into(
		flt(1)>>SolidWall(),
		2>>split(y).into(2.5>>Door(), flt(2)>>SolidWall()),
		flt(1)>>SolidWall()
	)

@rule
def Window():
	color(windowColor)
	size(rel(1), rel(1), 0.4)
	translate(0,0,-0.25)
	insert("window.blend")

@rule	
def Door():
	color("#ff0000")
	size(rel(1), rel(1), 0.1)
	translate(0, 0, -0.5)
	insert("cube")

@rule
def Wall():
	color(wallColor)

@rule
def SolidWall():
	color(wallColor)
	size(rel(1), rel(1), 0.4)
	translate(0, 0, -0.4)
	insert("cube")
