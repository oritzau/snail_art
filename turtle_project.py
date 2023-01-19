import turtle

snail = turtle.Turtle()
my_win = turtle.Screen()

def draw_snail():
    counter = 0
    snail.speed(0)
    x = 0
    y = 0
    z = 0
    a = 0
    snail.pu()
    snail.goto(-200, 0)
    snail.pd()
    while counter < 26:
        snail.fd(15 + x)
        snail.lt(40)
        counter += 1
        x += 4
    counter = 0
    snail.goto(-236, -98.91)
    snail.pu()
    snail.goto(-180, -97.5)
    snail.pd()
    snail.lt(38)
    while counter < 55:
        snail.fd(7)
        snail.lt(1 + y)
        y += .05
        counter += 1
    counter = 0
    while counter < 20:
        if counter in range(3, 6):
            snail.pu()
        elif counter in range(15, 18):
            snail.pu()
        else:
            snail.pd()
        snail.fd(4.2)
        snail.lt(6 + z)
        z += .05
        counter += 1
    counter = 0
    snail.fd(30)
    while counter < 9:
        snail.rt(6)
        snail.fd(4)
        counter += 1
    counter = 0
    snail.pu()
    snail.goto(-25, 117)
    snail.pd()
    snail.circle(4)
    snail.pu()
    snail.goto(15, 117)
    snail.pd()
    snail.circle(4)
    snail.pu()
    snail.goto(-15, 102)
    snail.lt(130)
    snail.pd()
    while counter < 12:
        snail.fd(2)
        snail.lt(5)
        counter += 1
    counter = 0
    snail.pu()
    snail.goto(19.33,139.82)
    snail.pd()
    snail.fd(15)
    snail.pu()
    snail.goto(9,145)
    snail.pd()
    snail.fd(20)
    snail.pu()
    snail.goto(37,148)
    snail.pd()
    snail.circle(7)
    snail.pu()
    snail.goto(-27.40,139.72)
    snail.pd()
    snail.lt(90)
    snail.fd(27)
    snail.pu()
    snail.goto(-35.5,131.5)
    snail.pd()
    snail.fd(27)
    snail.pu()
    snail.goto((-41.01,164))
    snail.pd()
    snail.circle(7.5)

if __name__ == '__main__':
    draw_snail()
    snail.hideturtle()
    snail.getscreen().getcanvas().postscript(file = "snowflake.eps")
    my_win.exitonclick()
