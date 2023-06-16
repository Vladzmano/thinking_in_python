import turtle

# Configuración inicial
screen = turtle.Screen()
screen.bgcolor("white")
turtle.speed(0)  # Configura la velocidad más rápida

# Dibujar la espiral
for i in range(500):
    turtle.forward(i)
    turtle.right(91)

# Mantener la ventana abierta
turtle.done()