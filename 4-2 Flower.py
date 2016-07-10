from swampy.TurtleWorld import *

from math import pi
world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.01

def square(t, length):
    for i in range(4):
        fd(t, length)
        lt(t)

def polygon(t, length, n):
    for i in range(360/n):
        fd(t, length)
        lt(t, n)

def circle(t, r):
    for i in range(100):
        fd(t, 2*pi*r/100)
        lt(t, 3.6)

def arc(t, r, angle):
    arc_length = 2 * pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range (n):
        fd(t, step_length)
        lt(t, step_angle)

def flower(t, length, Num_of_Pedal, Angle_of_Pedal):
    '''Draws several pedals depends on givens.
    
    t: Turtle
    length: The distance from the peak of pedal to the center
    Num_of_Pedal: Total number of pedals
    Angle_of_Pedal: Define the widness of each pedal
    '''
    
    angle = 360 / Num_of_Pedal
    for i in range(Num_of_Pedal):
        arc(t, length, Angle_of_Pedal)
        lt(t, 180 - Angle_of_Pedal)
        arc(t, length, Angle_of_Pedal)
        lt(t, 180 - Angle_of_Pedal + angle)
    
Input_Length = int(raw_input("length: "))
Input_Num_of_Pedal = int(raw_input("Number of Pedal: "))
Input_Angle_of_Pedal = int(raw_input("Angle of Pedal: "))
flower(bob, Input_Length, Input_Num_of_Pedal, Input_Angle_of_Pedal)
die(bob)

wait_for_user()
