from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print bob
bob.delay = 0.001

def snowflake(t, length):
    for i in range(3):
        Koch(t, length)
        rt(t, 120)

def Koch(t, length):
    if length / 3 >= 3:
        Koch(t, length / 3)
    else:
        fd(t, length)
        
    lt(t, 60)
    
    if length / 3 >= 3:
        Koch(t, length / 3)
    else:
        fd(t, length)

    rt(t, 120)

    if length / 3 >= 3:
        Koch(t, length / 3)
    else:
        fd(t, length)

    lt(t, 60)

    if length / 3 >= 3:
        Koch(t, length / 3)
    else:
        fd(t, length)
        
snowflake(bob, 180)
die(bob)

wait_for_user()
