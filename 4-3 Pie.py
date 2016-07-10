from swampy.TurtleWorld import *

from math import *
world = TurtleWorld()
bob = Turtle()
bob.delay = 0.005
pu(bob)
bk(bob, 130)
pd(bob)

def mult_poly(t, Num_of_Tri, r):
    for i in range(4):
        Top_Angle = 360.0 / Num_of_Tri
        Half_Angle = Top_Angle / 2
        
        pd(t)
        polygon(t, Num_of_Tri, r)
        lt(t, Half_Angle)
        pu(t)
        fd(t, r*2 + 10)
        Num_of_Tri += 1

def polygon(t, Num_of_Tri, r):
    Top_Angle = 360.0 / Num_of_Tri
    Half_Angle = Top_Angle / 2
    Base_Angle = (180.0 - Top_Angle) / 2
    Base = 2 * r * sin(Half_Angle / 180 * pi)

    rt(t, Half_Angle)
    for i in range(Num_of_Tri):
        isoscele(t, Base_Angle, r, Base)  

def isoscele(t, Base_Angle, r, Base):
    fd(t, r)
    lt(t, 180 - Base_Angle)
    fd(t, Base)
    lt(t, 180 - Base_Angle)
    fd(t, r)
    lt(t, 180)

Num_of_Tri = int(raw_input("Number of Triangle: "))
r = int(raw_input("Radians: "))
mult_poly(bob, Num_of_Tri, r)
die(bob)

wait_for_user()

###########Original code provided by the book###########

##"""This module contains code from
##Think Python by Allen B. Downey
##http://thinkpython.com
##
##Copyright 2012 Allen B. Downey
##License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
##
##"""
##
##import math
##
##try:
##    # see if Swampy is installed as a package
##    from swampy.TurtleWorld import *
##except ImportError:
##    # otherwise see if the modules are on the PYTHONPATH
##    from TurtleWorld import *
##
##def draw_pie(t, n, r):
##    """Draws a pie, then moves into position to the right.
##    t: Turtle
##    n: number of segments
##    r: length of the radial spokes
##    """
##    polypie(t, n, r)
##    pu(t)
##    fd(t, r*2 + 10)
##    pd(t)
##    
##def polypie(t, n, r):
##    """Draws a pie divided into radial segments.
##    t: Turtle
##    n: number of segments
##    r: length of the radial spokes
##    """
##    angle = 360.0 / n
##    for i in range(n):
##        isosceles(t, r, angle/2)
##        lt(t, angle)
##
##def isosceles(t, r, angle):
##    """Draws an icosceles triangle.
##    The turtle starts and ends at the peak, facing the middle of the base.
##    t: Turtle
##    r: length of the equal legs
##    angle: peak angle in degrees
##    """
##    y = r * math.sin(angle * math.pi / 180)
##
##    rt(t, angle)
##    fd(t, r)
##    lt(t, 90+angle)
##    fd(t, 2*y)
##    lt(t, 90+angle)
##    fd(t, r)
##    lt(t, 180-angle)
##
### create the world and bob
##world = TurtleWorld()
##bob = Turtle()
##bob.delay = 1
##pu(bob)
##bk(bob, 130)
##pd(bob)
##
### draw polypies with various number of sides
##size = 40
##draw_pie(bob, 5, size)
##draw_pie(bob, 6, size)
##draw_pie(bob, 7, size)
##draw_pie(bob, 8, size)
##die(bob)
##
##wait_for_user()
##
##
