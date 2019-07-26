'''
Neste exemplo temos a espiral novamente só que com as cores e a 
largura do pincel variando
'''
from turtle import *
speed(0)
colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']

for x in range(360):
    pencolor(colors[x % 6]) #alterna as cores entre a primeira e a última
    width(x / 100 + 1) # mesmo comando do pensize() (largura do pincel)
    forward(x)
    left(59)

done()