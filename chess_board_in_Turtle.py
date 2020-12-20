# creating a simple chess board
# Each row having 8 columns
# total 4 column black and 4 column white alternativly
import turtle
t1=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('blue violet')
screen.title('***Chess Board***')
t1.hideturtle()
t1.penup()
t1.goto(-20,200)
t1.pendown()
t1.color('pink')
t1.write("CHESS BOARD",align='center',font=("times new roman",24,"bold"))
t1.speed(0)
t1.color('black')
# chess outer boders
def square():
    t1.forward(350)
    t1.right(90)
    t1.forward(350)
    t1.right(90)
    t1.forward(350)
    t1.right(90)
    t1.forward(350)
# changing the position of turtle
t1.penup()
t1.goto(-180,180)
t1.pendown()
t1.pensize(5)
square()
# pensize for inner boders
t1.pensize(3)
###
# loop for creating row

#####################
for i in range(4):
    t1.right(90)
    t1.forward(350/8)
#######################
    # function for small square in row
    def small_square():
        for j in range(4):
            t1.begin_fill()
            t1.fillcolor('white')
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/4)
            t1.end_fill()
            #
            t1.begin_fill()
            t1.fillcolor('black')
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.penup()
            t1.forward(350/4)
            t1.pendown()
            t1.end_fill()
            ####
    small_square()

    ###############################################################
    # move to the initial position

    ####################################################################

    def initial_position():
            t1.penup()
            t1.right(180)
            t1.forward(350/8+350)
            t1.left(90)
            t1.forward(350/8)
            t1.left(180)
            t1.pendown()
    initial_position()

    ####################################################################

    # function for 2nd row square
    ######################################################################
    def small_square2():
        t1.right(90)
        t1.forward(350/8)
        for k in range(4):
            t1.begin_fill()
            t1.fillcolor('black')
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.penup()
            t1.forward(350/4)
            t1.pendown()
            t1.end_fill()
            #
            t1.begin_fill()
            t1.fillcolor('white')
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.forward(350/8)
            t1.right(90)
            t1.penup()
            t1.forward(350/4)
            t1.pendown()
            t1.end_fill()
    small_square2()
    initial_position()
user_input=input('press "y" to continue: ') # for hold the out put screen

##################################################################
        
        
# finally complited !!!!!!!