import turtle

def draw_square(turt):
    for i in range(1,5):
        turt.forward(100)
        turt.right(90)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("red")
    brad=turtle.Turtle()
    brad.speed(0)
    brad.color("yellow")
    for i in range(0,180):
        draw_square(brad)
        brad.right(2)
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)
    window.exitonclick()
    
draw_art()
