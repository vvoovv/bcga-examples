from pro import *

# lib directory must be in sys.path
import os, sys
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
if SCRIPT_DIR not in sys.path:
    sys.path.append(SCRIPT_DIR)

from lib.stairs import SimpleStairs as Stairs

stairsHeight = param(7.5)
stepHeight = param(0.5)
stepWidth = param(0.3)

@rule
def Lot():
    texture("MarekSeamlessBrick003.jpg", 0.5, 0.5)
    extrude(14, front>>Front(), side>>Side(), inheritMaterialAll=True)

@rule
def Front():
    split(y,
        stairsHeight>>split(x,
            flt(),
            2>>Stairs(stepWidth, stepHeight, texture("MarekBrick002.jpg", 0.5, 0.5)),
            flt()
        ),
        2>>split(x,
            flt(),
            1.5>>texture("431px-PL20F1SzczecinPlasticDoorRed.jpg"),
            flt()
        ),
        flt(),
        0.5,
        2.5>>Window()
    )

@rule
def Side():
    split(y,
        flt(),
        2.5>>Window()
    )

@rule
def Window():
    extrude(0.5,
        front>>split(y,
            flt(),
            1.5>>split(x,
                flt(),
                1.5>>texture("MarekPlainWindow00003.jpg"),
                flt()
            ),
            flt()
        ),
        inheritMaterialAll=True
    )
