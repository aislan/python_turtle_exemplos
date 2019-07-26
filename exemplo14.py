'''
Exemplo de interação com a tela 
com uso do teclado
'''
from turtle import *

def up():
    setheading(90)
    forward(100)

def down():
    setheading(270)
    forward(100)

def left():
    setheading(180)
    forward(100)

def right():
    setheading(0)
    forward(100)
    
#o listen ativa o modo 'escuta' para levar em consideração os comandos 
listen()
#onkey dispara uma função depois de digitado uma determinada tela
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')

onkey(up, 'w')
onkey(down, 's')
onkey(left, 'a')
onkey(right, 'd')

done()