'''
onkeypess(f,'t') faz algo enquanto uma tecla é pressionada
okey(f,'t') faz algo apens quando a mesma é pressionada
'''
from turtle import *

def blue_screen():
    bgcolor(0.7, 1.0, 1.0) #azul claro

def white_screen():
    bgcolor(1.0, 1.0, 1.0) #branco

listen()
onkeypress(blue_screen, 'space')
onkey(white_screen, 'space')
done()