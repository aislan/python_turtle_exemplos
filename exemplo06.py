'''
Girando o cursor para um "ângulo fixo" com o comando setheading(a) 
'''
from turtle import *

speed(0)

for angulo in range(0, 360, 15):
    setheading(angulo)
    forward(100)
    write(str(angulo) + '°')
    backward(100)

done()