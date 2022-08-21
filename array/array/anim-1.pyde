# x,y zahyo
x_y = 12.5
def setup():
    size(1000,1000 )
    
def draw():
    background(255)
    for x in range(0, width, 100):
        for y in range(0, height, 100):
            fill(0, 0, 0, 130)
            rect(x+x_y, y+x_y, 75, 75)
