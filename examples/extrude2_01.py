from pro import *

erkerDepth = param(1.5)

@rule
def Lot():
    color("#000099")
    extrude(5)
    Building()

@rule
def Building():
    decompose(
        front>>Front(),
        left>>Left()
    )

@rule
def Front():
    texture("MarekSeamlessBrick003.jpg", 0.5, 0.5)
    split(x,
        flt(1),
        5>>Erker(),
        flt(1),
        flt(3)>>Entrance(),
        flt(1),
        5>>Erker(),
        flt(1)
    )

@rule
def Left():
    texture("MarekSeamlessBrick003.jpg", 0.5, 0.5)
    split(x,
        flt(1),
        flt(1)>>Erker(),
        flt(1)
    )
    
@rule
def Entrance():
    extrude2(
        0.1, 3,
        0.2, 4>>texture("MarekBrick002.jpg", 0.5, 0.5),
        0.3, 6,
        last>>color("#ff69b4"),
        middle>>Door(),
        #cap2>>extrude(2, all>>color("#00ee00")),
        cap1>>delete(),
        section>>texture("MarekSeamlessBrick003.jpg", 0.5, 0.5)
    )

@rule
def Erker():
    extrude2(
        0.3, erkerDepth,
        cap2>>color("#00ee00"),
        cap1>>delete(),
        section>>Face()
    )

@rule
def Face():
    texture("MarekSeamlessBrick003.jpg", 0.5, 0.5)
    split(x,
        rel(0.1),
        flt()>>split(y,
                1,
                flt()>>texture("MarekPlainWindow00003.jpg"),
                1
            ),
        rel(0.1)
    )

@rule
def Door():
    texture("MarekSeamlessBrick003.jpg", 0.5, 0.5)
    split(x,
        flt(),
        2>>split(y,
                flt()>>texture("431px-PL20F1SzczecinPlasticDoorRed.jpg"),
                1
            ),
        flt()
    )