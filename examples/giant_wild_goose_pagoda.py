from pro import *
from assets.textures import *

offset1 = 0.2
offsetHeight1 = 0.1

mainOffset = 0.3
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
        mainOffset, mainHeight,
        cap>>ConnectionBottom(numParts)
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
        insets.extend((0.15, 0, 0, 0.1))
        
    insets.append(cap>>Part())
    
    inset2(
        *insets
    )