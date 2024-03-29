from turtle import *

tela = Screen()
tela.title("Jogo de Pong")
tela.bgcolor("black")
tela.setup(width=800, height=600)
tela.tracer(0)

#score
score_a = 0
score_b = 0

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
bola.shape("circle")
bola.speed(0)
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = 2
bola.dy = -2

#placar
placar = Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0,260)
placar.write("Jogador A: 0   Jogador B: 0", align="center", font=("Arial",24))

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

    #movimentando a bola 
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # verificando as bordas 
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1
        score_a += 1
        placar.clear()
        placar.write("Jogador A: {}   Jogador B: {}".format(score_a,score_b), align="center", font=("Arial",24))


    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        score_b += 1
        placar.clear()
        placar.write("Jogador A: {}   Jogador B: {}".format(score_a,score_b), align="center", font=("Arial",24))
    
    if bola.xcor() > 390:
        bola.goto(0,0)
        bola.dx *= -1

    if bola.xcor() < -390:
        bola.goto(0,0)
        bola.dx *= -1

    #colisão da bola com os jogadores

    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < jogador_b.ycor()+ 40 and bola.ycor()>jogador_b.ycor() - 40):
        bola.setx(340)
        bola.dx *=-1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < jogador_a.ycor()+ 40 and bola.ycor()>jogador_a.ycor() - 40):
        bola.setx(-340)
        bola.dx *=-1