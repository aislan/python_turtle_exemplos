from turtle import *

tela = Screen()
tela.title("Jogo de Pong")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

# jogador a
jogador_a = Turtle()
jogador_a.speed(0)
jogador_a.shape("square")
jogador_a.color("white")
jogador_a.shapesize(stretch_wid=5, stretch_len=1)
jogador_a.penup()
jogador_a.goto(-350,0)

# jogador b
jogador_b = Turtle()
jogador_b.speed(0)
jogador_b.shape("square")
jogador_b.color("white")
jogador_b.shapesize(stretch_wid=5, stretch_len=1)
jogador_b.penup()
jogador_b.goto(350,0)

#bola
bola = Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)

#funções
def jogador_a_sobe():
    y = jogador_a.ycor()
    y += 20
    jogador_a.sety(y)

def jogador_a_desce():
    y = jogador_a.ycor()
    y -= 20
    jogador_a.sety(y)

def jogador_b_sobe():
    y = jogador_b.ycor()
    y += 20
    jogador_b.sety(y)

def jogador_b_desce():
    y = jogador_b.ycor()
    y -= 20
    jogador_b.sety(y)

#comandos teclado
tela.listen()
tela.onkeypress(jogador_a_sobe,"w")
tela.onkeypress(jogador_a_desce,"s")
tela.onkeypress(jogador_b_sobe,"Up")
tela.onkeypress(jogador_b_desce,"Down")

#parte principal do jogo
while True:
    tela.update()
