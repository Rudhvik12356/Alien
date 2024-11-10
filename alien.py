import pgzrun,random

WIDTH = 750
HEIGHT = 750

TITLE = "Alien Shooting"

alien = Actor("alien.png", (WIDTH/2, HEIGHT/2))
message = "Shoot the Alien to save the planet!"

def draw():
    screen.fill(color = "black")
    alien.draw()
    screen.draw.text(message, center = (375, 25), fontsize = 30)
    
    alien.x = random.randint(50, WIDTH-50)
    alien.y = random.randint(50, HEIGHT-50)
    
def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Good Shot!"
    else:
        message = "You Missed!"    
            
pgzrun.go()