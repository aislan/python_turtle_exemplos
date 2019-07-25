from turtle import *

screen = Screen()
screen.tracer(0)

largura_labirinto=150

labirinto = Turtle()
labirinto.width(5)
labirinto.hideturtle()

labirinto.speed(0)

labirinto.penup()
labirinto.goto(-largura_labirinto,190)


def desenhar_sessao_labirinto(cor):
  labirinto.color(cor)
  labirinto.pendown()
  labirinto.forward(largura_labirinto)
  labirinto.penup()
  labirinto.forward(40)
  labirinto.pendown()
  labirinto.forward(largura_labirinto)
  labirinto.right(90)
  labirinto.forward(100)
  labirinto.right(90)
  labirinto.forward(largura_labirinto)
  labirinto.penup()
  labirinto.forward(40)
  labirinto.pendown()
  labirinto.forward(largura_labirinto)
  labirinto.right(90)
  labirinto.forward(100)
  labirinto.right(90)
  x,y = labirinto.pos()
  labirinto.penup()  
  labirinto.goto(x, y-50)
  labirinto.pendown()
  labirinto.forward(30)
  labirinto.penup()
  labirinto.forward(40)
  labirinto.pendown()
  labirinto.forward(200)
  labirinto.penup()
  labirinto.forward(40)
  labirinto.pendown()
  labirinto.forward(30)
  labirinto.penup()
  labirinto.goto(x,y-110)

for cor in ["#FF0000","#0000FF","#00FF00"]:
  desenhar_sessao_labirinto(cor)

screen.tracer(1) 

# parte principal do programa 

jogador=Turtle()
jogador.penup()
jogador.goto(20,-180)
jogador.pendown()
jogador.shape('turtle')
jogador.color("#DB148E")
jogador.width(5)
jogador.left(90)

#saia do labirinto
jogador.forward(70)
jogador.right(90)

#fim
done()



