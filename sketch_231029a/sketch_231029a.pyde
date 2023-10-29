x=2500
y=1
p=255
e=0
o=0
def setup ():
    size (2000,1000)
    frameRate (101123131)
def draw():
    global x
    global y
    global p
    global e
    global o
    x=x-y
    p=p-0.2
    e=e+0.2
    stroke (p,e,o)
    fill (p,e,o)
    ellipse (1000,500,x,x)
    if x == 0:
        noLoop()
    if e == 127.2:
        x=x-y
        p=p-0.2
        o=o+0.2
        stroke (p,e,o)
        fill (p,e,o)
        ellipse (1000,500,x,x)
