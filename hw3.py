import pgzrun
import random

WIDTH = 300
HEIGHT = 300
def draw():
    r = 0
    g = 255
    b = random.randint(100, 255)
    radius = WIDTH // 2
   
    for i in range(20):
        screen.draw.circle((150, 150), radius, (r, g, b))
        radius -= 10  
        g -= 10
        r += 10
pgzrun.go()