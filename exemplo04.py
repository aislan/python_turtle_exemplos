'''
Desenhando flores azuis de forma aleatória na tela 
'''
from turtle import *
import random
speed(0.1)
for n in range(60):
    #levanta o pincel para não riscar
    penup()
    #goto(x,y) serve para levar o cursor de um ponto a outro da tela
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    pencolor((red_amount, green_amount, blue_amount))

    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    for i in range(6):
        circle(circle_size)
        left(60)

done()