#pixel size
p_size = 100
#x,y zahyo
x_y = 12.5
ang = 0

def setup():
    size(1000,1000)
    frameRate(10) #speed
    
def draw():
    global ang
    background(255)
    for x in range(height/p_size):
        for y in range(width/p_size):
            with pushMatrix():
                translate(x_y + y * p_size,
                          x_y + x * p_size)
                if int(random(50)):
                    rotate(ang == 100)
                else:
                    rotate(ang / 1)
                fill(0, 0, 0, 130)
                rect(0, 0, 75, 75)
                ang += 0.001
