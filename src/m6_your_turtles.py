"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Caleb Shen.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()

leonardo = rg.SimpleTurtle('turtle')
leonardo.pen = rg.Pen('green', 2)
leonardo.speed = 15

size = 150

for k in range(20):

        leonardo.draw_circle(size)

        leonardo.pen_up()
        leonardo.forward(20)
        leonardo.right(60)
        leonardo.pen_down()
        size = size - 4

window.tracer(100)
michaelangelo = rg.SimpleTurtle('square')
michaelangelo.pen = rg.Pen('blue', 2)
michaelangelo.forward(25)

for k in range(450):
    michaelangelo.right(65)
    michaelangelo.forward(k)
window.close_on_mouse_click()