"""indian Flag creation
@author=dataseeker"""
import turtle
import time
time.sleep(5)
turtle.screensize(canvwidth=100, canvheight=100, bg=None)
orr= turtle.Turtle()
grn=turtle.Turtle()
wh=turtle.Turtle()
blu=turtle.Turtle()

def draw_rectangle(length, height,pos):
    for i in range(0,2):
       if i % 2 == 0:
            orr.fillcolor("orange")
            orr.begin_fill()
    
            orr.forward(length)
            orr.left(90)
            orr.forward(height)
            orr.left(90)
            orr.forward(length)
            orr.left(90)
            orr.forward(height)
##            orr.fillcolor("red")
            orr.end_fill()
            orr.forward(240)
       else :
            blu.color('blue')
            blu.up()
            blu.setpos(100,-38)
            blu.down()
            blu.circle(18)
            blu.up()
            blu.setpos(100,-20)
            blu.down()
            for a in range(24):
               blu.left(15)
               blu.forward(18)
               blu.backward(18)
            blu.hideturtle()
            wh.forward(length)
            wh.right(90)
            wh.forward(height)
            wh.right(90)
            wh.forward(length)
            wh.left(90)
            wh.forward(200)
            grn.fillcolor('green')
            grn.begin_fill()
            grn.right(90)
            grn.forward(height*2)
            grn.left(90)
            grn.forward(length)
            grn.left(90)
            grn.forward(height)
            grn.left(90)
            grn.forward(length)
            grn.end_fill()
            grn.left(90)
            grn.forward(height*5)
            tt1=turtle.Turtle()
            tt1.color("orange")
            tt1.up()
            tt1.setpos(20,-120)
            
            tt1.write("Happy",font=("Chiller",
                                    20, "normal"))
            tt1.hideturtle()
            tt2=turtle.Turtle()
            tt2.color("blue")
            tt2.up()
            tt2.setpos(40,-160)
            
            tt2.write("Independence",font=("Chiller",
                                    20, "normal"))
            tt2.hideturtle()
            tt3=turtle.Turtle()
            tt3.color("green")
            tt3.up()
            tt3.setpos(60,-200)
            
            tt3.write("Day",font=("Chiller",
                                    20, "normal"))
            time.sleep(2)
            tt3.hideturtle()
	
            
####            
                  

draw_rectangle(200,40,10)
