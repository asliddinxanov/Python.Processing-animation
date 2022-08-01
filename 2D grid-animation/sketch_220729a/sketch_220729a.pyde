#2D grid animation2D grid animation2D grid animation
pix_size = 50
x_y = 25
ang = 0
def setup():
    size(800,500)
    rectMode(CENTER)
    frameRate(10)
    colorMode(HSB)
    #noStroke()
    
def draw():
    global ang
    background(0)
    for x in range(height/pix_size):
        for y in range(width/pix_size):
            with pushMatrix():
                translate(x_y + y * pix_size,
                          x_y + x * pix_size)
                if int(random(2)):
                    rotate(ang / 3)
                else:
                    rotate(ang / 2)
                fill((ang * (x + 1) * (y + 1)) % 255, 255, 225, 140)
                rect(0,0,75,75)
                ang += 0.001
