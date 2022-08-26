# Click the mouse.

from PokePix import PokeBall

balls = []
ballWidth = 3

def setup():
    size(640, 360)
    noStroke()
    balls.append(PokeBall(width / 2, 0, ballWidth))

def draw():
    background(160)
    for ball in balls:
        ball.move()
        ball.display()
        if ball.finished():
            # poke can be deleted with remove()
            balls.remove(ball)

def mousePressed():
    balls.append(PokeBall(mouseX, mouseY, ballWidth))
