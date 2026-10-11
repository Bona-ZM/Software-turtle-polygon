import turtle
import math

x = 0
y = 0
size = 50
angle = 10
n = 8

an = 180*(n-2)/n
bn = 180-an

l = size/(2*math.sin(math.radians(bn)/2))
z = l*math.cos(math.radians(angle))
w = l*math.sin(math.radians(angle))

u = z+x
v = w+y

turtle.setposition(u,v)
turtle.left(90+bn/2+angle)

for i in range(n):
    turtle.forward(size)
    turtle.left(bn)
turtle.exitonclick()