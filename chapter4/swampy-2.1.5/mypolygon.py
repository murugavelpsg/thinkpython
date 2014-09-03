import os
import math
os.chdir('/home/murugavel/learning/thinkpython/chapter4/swampy-2.1.5')

try:
    # see if Swampy is installed as a package
    from swampy.TurtleWorld import *
except ImportError:
    # otherwise see if the modules are on the PYTHONPATH
    from TurtleWorld import *

def draw_square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt()

def draw_polygon(t, sides, length):
    for i in range(sides):
        t.fd(length)
        t.lt(360/sides)

def draw_circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    draw_polygon(t, n, length)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.001
#draw_polygon(bob, 10, 75)
draw_circle(bob, 50)
wait_for_user()
