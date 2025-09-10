import turtle
v = turtle.Screen()
t = turtle.Turtle() 
t.shape("turtle") # forma de tortuga
t.color("green") #color de tortuga
t.pensize(7) # grosor
v.bgcolor("black") #color de hoja
t.forward(100)#avanza hacia adelante
t.right(180)  # Gira la tortuga hacia abajo #media vuelta por el 180 
t.circle(50,180) #radio es de 50 y el 180 grados osea medio circulo  
t.up()#levanta el lapiz
t.down()#baja el lapiz
t.begin_fill() #inicio para poder rellenar el color
t.color("#DDE0EB") #color
t.circle(70) #circulo que sera pintado por dentro
t.end_fill()#termina de pintar el interior 
