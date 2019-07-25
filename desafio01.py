from turtle import * 

def desenha_campo():
  GRAMADO="#149118"
  screen = Screen()
  #tracer tem função parecida com o deley
  screen.tracer(0)
  screen.bgcolor(GRAMADO)
  
  minha_caneta = Turtle()
  minha_caneta.width(1)
  minha_caneta.hideturtle()
  
  minha_caneta.speed(0)
  minha_caneta.color("#FFFFFF")
  
  #definindo o campo
  minha_caneta.penup()
  minha_caneta.goto(-140,195)
  minha_caneta.pendown()
  minha_caneta.goto(140,195)
  minha_caneta.goto(140,-195)
  minha_caneta.goto(-140,-195)
  minha_caneta.goto(-140,195)
  
  #área de penalt de cima
  minha_caneta.penup()
  minha_caneta.goto(0,115)
  minha_caneta.pendown()
  minha_caneta.circle(40)
  minha_caneta.penup()
  minha_caneta.goto(-80,195)
  minha_caneta.pendown()
  minha_caneta.fillcolor(GRAMADO)
  minha_caneta.begin_fill()
  minha_caneta.goto(80,195)
  minha_caneta.goto(80,140)
  minha_caneta.goto(-80,140)
  minha_caneta.goto(-80,195)  
  minha_caneta.end_fill()
 
  #área de penalt de baixo
  minha_caneta.penup()
  minha_caneta.goto(0,-195)
  minha_caneta.pendown()
  minha_caneta.circle(40)
  minha_caneta.penup()
  minha_caneta.goto(-80,-195)
  minha_caneta.pendown()
  minha_caneta.fillcolor(GRAMADO)
  minha_caneta.begin_fill()
  minha_caneta.goto(80,-195)
  minha_caneta.goto(80,-140)
  minha_caneta.goto(-80,-140)
  minha_caneta.goto(-80,-195)  
  minha_caneta.end_fill()

  # gol de baixo 
  minha_caneta.penup()
  minha_caneta.goto(40,-195)
  minha_caneta.pendown()
  minha_caneta.goto(40,-170)
  minha_caneta.goto(-40,-170)
  minha_caneta.goto(-40,-195)  

  # gol de cima
  minha_caneta.penup()
  minha_caneta.goto(40,195)
  minha_caneta.pendown()
  minha_caneta.goto(40,170)
  minha_caneta.goto(-40,170)
  minha_caneta.goto(-40,195)     
  
  #Halfway Line
  minha_caneta.penup()
  minha_caneta.goto(-140,0)
  minha_caneta.pendown()
  minha_caneta.goto(140,0)
  
  #círculo central
  minha_caneta.penup()
  minha_caneta.goto(0,-40)
  minha_caneta.pendown()
  minha_caneta.circle(40)
  
  screen.tracer(1)  


#Função para desenhar jogador
def desenha_jogador(cor,x,y,nome_jogador):
  screen = Screen()
  screen.tracer(0)
  myPen = Turtle()
  myPen.hideturtle()
  myPen.penup()
  myPen.goto(x,y)
  myPen.fillcolor(cor)
  myPen.begin_fill()
  myPen.circle(10)
  myPen.end_fill()
  screen.tracer(1)  
  myPen.penup()
  myPen.goto(x+10,y)
  myPen.color(cor)
  myPen.write(nome_jogador)

#Programa principal começa aqui
desenha_campo()

desenha_jogador("blue",-0,-194,"Goleriro") 
desenha_jogador("yellow",-50,-120,"Zagueiro") 
desenha_jogador("yellow",50,-120,"Zagueiro") 
#forma e escalação de todo o timme

done()
