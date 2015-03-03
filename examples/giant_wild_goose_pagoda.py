from pro import *
from assets.textures import *

offset1 = 0.2
offsetHeight1 = 0.1

mainOffset = param(0)#param(0.3)
mainHeight = param(3.5)

def init():
    global numParts
    numParts = 7


@rule
def Begin():
    init()
    rectangle(25, 25, replace=True)
    Basement()

@rule
def Basement():
    inset2(
        0.5, 5,
        -offset1, 0,
        0, offsetHeight1,
        -offset1, 0,
        0, offsetHeight1,
        offset1, 0,
        0, offsetHeight1,
        1.5, 0,
        cap>>Part()
    )

@rule
def Part():
    global numParts
    numParts -= 1
    
    inset2(
        mainOffset, mainHeight>>Side(),
        cap>>ConnectionBottom(numParts)
    )

@rule
def Side():
    split(x,
        flt(),
        2>>split(y,
            flt()>>WindowSection(),
            rel(0.3)
        ),
        flt()   
    )

@rule
def WindowSection():
    extrude(-0.7,
        top>>extrude2(
            0,1>>delete(), # it's hidden
            0.1, 0.8,
            0.2, 0.6,
            0.5, 0.5,
            cap2>>delete() # it's hidden
        )
    )

@rule
def ConnectionBottom(upperConnection):
    insets = []
    for i in range(12):
        insets.extend((-0.1, 0, 0, 0.1))
    if upperConnection:
        insets.append(cap>>ConnectionUpper())
    
    inset2(
        *insets
    )

@rule
def ConnectionUpper():
    insets = []
    for i in range(12):
        insets.extend((0.2, 0, 0, 0.1))
        
    insets.append(cap>>Part())
    
    inset2(
        *insets
    )