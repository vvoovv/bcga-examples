from pro import *


# extrude(...) with subsequent decompose(...)

@rule
def Lot():
	extrude(10)
	Building()

@rule
def Building():
	decompose(
		side>>SideFacade(),
		top>>Roof()
	)

@rule
def SideFacade():
	color("#00ff00")
	split(x,
		rel(0.3)>>Side(),
		flt()>>Middle(),
		rel(0.3)>>Side()
	)

@rule
def Roof():
	pass

@rule
def Side():
	pass

@rule
def Middle():
	color("#0000ff")
	extrude(2)
	decompose(
		left>>color("#ee1100"),
		front>>color("#00ffff"),
		right>>color("#0011ee"),
		bottom>>delete()
	)