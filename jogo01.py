#exemplo de jogo
from turtle import *
from math import *
from random import *

#carregando a tela principal
Screen()
bgcolor('lightgreen')

#desenhando os limites/bordas do jogo
arena = Turtle()
arena.penup()
arena.setposition(-300,-300)
arena.pendown()
arena.pensize(3)
for lado in range(4):
    arena.fd(600)
    arena.left(90)
arena.hideturtle()

#criando o jogador
jogador = Turtle()
jogador.color('blue')
jogador.shape('triangle')
jogador.penup()
jogador.speed(0)

#velocidade
velocidade = 1

#ações dos comandos
def vira_a_esquerda():
    jogador.left(30)

def vira_a_direita():
    jogador.right(30)

def aumenta_velocidade():
    global velocidade
    velocidade += 1

#comandos do jogo
listen()
onkey(vira_a_esquerda,"Left")
onkey(vira_a_direita,"Right")
onkey(aumenta_velocidade,"Up")

#pilulas de energia 
pilula = Turtle()
pilula.color("red")
pilula.shape("circle")
pilula.penup()
pilula.speed(0)
pilula.setposition(randint(-300,300),randint(-300,300))


#principal
while True:
    jogador.forward(velocidade)

    #verificação de limite/borda
    if jogador.xcor() > 300 or jogador.xcor() < -300:
        jogador.right(100)
    
    if jogador.ycor() > 300 or jogador.ycor() < -300:
        jogador.right(100)

    #verificar colisão
    distancia = sqrt(pow(jogador.xcor()-pilula.xcor(),2)+pow(jogador.ycor()-pilula.ycor(),2))
    if distancia<20:
        pilula.setposition(randint(-300,300),randint(-300,300))

done()