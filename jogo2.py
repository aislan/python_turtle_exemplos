from turtle import *

tela = Screen()
tela.title("Jogo de Pong")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)


#parte principal do jogo
while True:
    tela.update()
    