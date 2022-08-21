x = 280
y = 130
z = 5
e = 0.05
def setup():
    size (640, 320)

# draw pixel(black)
def draw():
    global x, y

    background(160)

    targetX = mouseX
    dx = targetX - x
    if(abs(dx) > 1):
        x += dx * e

    targetY = mouseY
    dy = targetY - y
    if(abs(dy) > 1):
        y += dy * e
        
    #background(255) #orqa fon
    fill(0) #kubni ichini rangi
    stroke(0) #kubni atrof chizig'ini rangi
    rect(x+z*5, y, z*6, z) # (x1,y1, dan boshlab, kube size)
    rect(x+z*3, y+z, z*2, z)
    rect(x+z*11, y+z, z*2, z)
    rect(x+z*2, y+z*2, z, z)
    rect(x+z*13, y+z*2, z, z)
    rect(x+z, y+z*3, z, z)
    rect(x+z*14, y+z*3, z, z)
    rect(x+z, y+z*4, z, z)
    rect(x+z*14, y+z*4, z, z)
    rect(x+z*7, y+z*4, z*2, z)
    rect(x, y+z*5, z, z)
    rect(x+z*6, y+z*5, z, z)
    rect(x+z*9, y+z*5, z, z)
    rect(x+z*15, y+z*5, z, z)
    rect(x, y+z*6, z*7, z)
    rect(x+z*9, y+z*6, z*7, z)
    rect(x, y+z*7, z, z)
    rect(x+z*6, y+z*7, z, z)
    rect(x+z*9, y+z*7, z, z)
    rect(x+z*15, y+z*7, z, z)
    rect(x, y+z*8, z, z)
    rect(x+z*7, y+z*8, z*2, z)
    rect(x+z*15, y+z*8, z, z)
    rect(x, y+z*9, z, z)
    rect(x+z*15, y+z*9, z, z)
    rect(x, y+z*10, z, z)
    rect(x+z*4, y+z*10, z*8, z)
    rect(x+z*15, y+z*10, z, z)
    rect(x+z, y+z*11, z*3, z)
    rect(x+z*6, y+z*11, z, z)
    rect(x+z*9, y+z*11, z, z)
    rect(x+z*12, y+z*11, z*3, z)
    rect(x+z*2, y+z*12, z, z)
    rect(x+z*6, y+z*12, z, z)
    rect(x+z*9, y+z*12, z, z)
    rect(x+z*13, y+z*12, z, z)
    rect(x+z*2, y+z*13, z, z)
    rect(x+z*13, y+z*13, z, z)
    rect(x+z*3, y+z*14, z, z)
    rect(x+z*12, y+z*14, z, z)
    rect(x+z*4, y+z*15, z*8, z)
    
# draw pixel(red)
    fill(255,0,0)
    stroke(255,0,0)
    rect(x+z*5, y+z, z*6, z)
    rect(x+z*3, y+z*2, z*10, z)
    rect(x+z*2, y+z*3, z*12, z)
    rect(x+z*2, y+z*4, z*5, z)
    rect(x+z*9, y+z*4, z*5, z)
    rect(x+z, y+z*5, z*5, z)
    rect(x+z*10, y+z*5, z*5, z)

    
# drew pixel(white)
    fill(255)
    stroke(255)
    rect(x+z*7, y+z*5, z*2, z)
    rect(x+z*7, y+z*6, z*2, z)
    rect(x+z*7, y+z*7, z*2, z)
    rect(x+z, y+z*7, z*5, z)
    rect(x+z*10, y+z*7, z*5, z)
    rect(x+z, y+z*8, z*6, z)
    rect(x+z*9, y+z*8, z*6, z)
    rect(x+z, y+z*9, z*14, z)
    rect(x+z, y+z*10, z*3, z)
    rect(x+z*12, y+z*10, z*3, z)
    
# drew pixel(yellow)
    fill(245,225,155)
    stroke(245,225,155)
    rect(x+z*4, y+z*11, z*2, z)
    rect(x+z*7, y+z*11, z*2, z)
    rect(x+z*10, y+z*11, z*2, z)
    rect(x+z*3, y+z*12, z*3, z)
    rect(x+z*7, y+z*12, z*2, z)
    rect(x+z*10, y+z*12, z*3, z)
    rect(x+z*3, y+z*13, z*10, z)
    rect(x+z*4, y+z*14, z*8, z)
