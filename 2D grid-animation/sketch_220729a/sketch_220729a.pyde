#2D grid animation2D grid animation2D grid animation
pix_size = 50

def setup():
    size(500,500)
    rectMode(CENTER)
    frameRate(10)
    colorMode(RGB)
    #noStroke()
    
def draw():
    background(0)
    for x in range(height/pix_size):
        for y in range(width/pix_size):
            with pushMatrix():
                translate(x_y + y * pix_size,
                          x_y + x * pix_size)
