from pro import *

import math

@rule
def SimpleStairs(stepWidth, stepHeight, materialOperator):
    """
    Generates a simple stairs
    
    Args:
        stepWidth (float): A width of a single step
        stepHeight (float): A height of a single step
        materialOperator (): An operator (e.g. texture(...)) or a rule that defines a material
    """
    stairs = []
    # total height of the stairs
    totalHeight = shape().size()[1]
    numSteps = math.floor(totalHeight/stepHeight)
    extraStepHeight = totalHeight-stepHeight*numSteps
    coord = 0
    if extraStepHeight>0:
        relStepHeight = extraStepHeight/totalHeight
        stairs.extend((0, (numSteps+1)*stepWidth, relStepHeight, (numSteps+1)*stepWidth))
        coord += relStepHeight
    relStepHeight = stepHeight/totalHeight
    while numSteps>0:
        stairs.extend((coord, numSteps*stepWidth,  coord+relStepHeight, numSteps*stepWidth))
        coord += relStepHeight
        numSteps -= 1
    stairs.append(section>>materialOperator)
    stairs.append(cap>>materialOperator)
    extrude2(*stairs, symmetric=False, axis=y)