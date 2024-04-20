import turtle

colors=['red', 'green', 'blue', 'yellow', 'orange', 'purple']

t=turtle.Pen()
t.speed(200)
turtle.bgcolor('black')
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)