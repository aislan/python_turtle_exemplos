'''
Desenhando flores azuis de forma aleatória na tela 
'''
from turtle import *
import random
#acelera a velocidade do desenho
speed(0.1)
for n in range(60):
    #goto(x,y) serve para levar o cursor de um ponto a outro da tela
    #esse código sever para possicionar o cursor em um local aleatório da tela
    penup()
    goto(random.randint(-400, 400), random.randint(-400, 400))
    pendown()

    #escolhe tons de azul aleatório 
    red_amount   = random.randint( 0,  30) / 100.0
    blue_amount  = random.randint(50, 100) / 100.0
    green_amount = random.randint( 0,  30) / 100.0
    pencolor((red_amount, green_amount, blue_amount))

    #escolhe tamanhos dos círcula aleatórios 
    circle_size = random.randint(10, 40)
    pensize(random.randint(1, 5))

    #desenhando a flor
    for i in range(6):
        circle(circle_size)
        left(60)

done()