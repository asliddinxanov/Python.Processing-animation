class PokeBall():

    def __init__(self, tempX, tempY, tempZ):
        self.x = tempX
        self.y = tempY
        self.z = tempZ
        self.speed = 0
        self.gravity = 0.1
        self.life = 255

    def move(self):
        self.speed = self.speed + self.gravity
        self.y = self.y + self.speed
        
        if self.y > height:
            self.speed = self.speed * -0.8
            self.y = height

    def finished(self):
        self.life -= 1
        return self.life < 0

    def display(self):
        
        # Dispaly the Pokeball pixels
        # draw pixel(black)
        fill(0)
        stroke(0)
        rect(self.x+self.z*5, self.y, self.z*6, self.z) # (x1,y1, dan boshlab, kube size)
        rect(self.x+self.z*3, self.y+self.z, self.z*2, self.z)
        rect(self.x+self.z*11, self.y+self.z, self.z*2, self.z)
        rect(self.x+self.z*2, self.y+self.z*2, self.z, self.z)
        rect(self.x+self.z*13, self.y+self.z*2, self.z, self.z)
        rect(self.x+self.z, self.y+self.z*3, self.z, self.z)
        rect(self.x+self.z*14, self.y+self.z*3, self.z, self.z)
        rect(self.x+self.z, self.y+self.z*4, self.z, self.z)
        rect(self.x+self.z*14, self.y+self.z*4, self.z, self.z)
        rect(self.x+self.z*7, self.y+self.z*4, self.z*2, self.z)
        rect(self.x, self.y+self.z*5, self.z, self.z)
        rect(self.x+self.z*6, self.y+self.z*5, self.z, self.z)
        rect(self.x+self.z*9, self.y+self.z*5, self.z, self.z)
        rect(self.x+self.z*15, self.y+self.z*5, self.z, self.z)
        rect(self.x, self.y+self.z*6, self.z*7, self.z)
        rect(self.x+self.z*9, self.y+self.z*6, self.z*7, self.z)
        rect(self.x, self.y+self.z*7, self.z, self.z)
        rect(self.x+self.z*6, self.y+self.z*7, self.z, self.z)
        rect(self.x+self.z*9, self.y+self.z*7, self.z, self.z)
        rect(self.x+self.z*15, self.y+self.z*7, self.z, self.z)
        rect(self.x, self.y+self.z*8, self.z, self.z)
        rect(self.x+self.z*7, self.y+self.z*8, self.z*2, self.z)
        rect(self.x+self.z*15, self.y+self.z*8, self.z, self.z)
        rect(self.x, self.y+self.z*9, self.z, self.z)
        rect(self.x+self.z*15, self.y+self.z*9, self.z, self.z)
        rect(self.x, self.y+self.z*10, self.z, self.z)
        rect(self.x+self.z*4, self.y+self.z*10, self.z*8, self.z)
        rect(self.x+self.z*15, self.y+self.z*10, self.z, self.z)
        rect(self.x+self.z, self.y+self.z*11, self.z*3, self.z)
        rect(self.x+self.z*6, self.y+self.z*11, self.z, self.z)
        rect(self.x+self.z*9, self.y+self.z*11, self.z, self.z)
        rect(self.x+self.z*12, self.y+self.z*11, self.z*3, self.z)
        rect(self.x+self.z*2, self.y+self.z*12, self.z, self.z)
        rect(self.x+self.z*6, self.y+self.z*12, self.z, self.z)
        rect(self.x+self.z*9, self.y+self.z*12, self.z, self.z)
        rect(self.x+self.z*13, self.y+self.z*12, self.z, self.z)
        rect(self.x+self.z*2, self.y+self.z*13, self.z, self.z)
        rect(self.x+self.z*13, self.y+self.z*13, self.z, self.z)
        rect(self.x+self.z*3, self.y+self.z*14, self.z, self.z)
        rect(self.x+self.z*12, self.y+self.z*14, self.z, self.z)
        rect(self.x+self.z*4, self.y+self.z*15, self.z*8, self.z)
        
        # draw pixel(red)
        fill(255,0,0)
        stroke(255,0,0)
        rect(self.x+self.z*5, self.y+self.z, self.z*6, self.z)
        rect(self.x+self.z*3, self.y+self.z*2, self.z*10, self.z)
        rect(self.x+self.z*2, self.y+self.z*3, self.z*12, self.z)
        rect(self.x+self.z*2, self.y+self.z*4, self.z*5, self.z)
        rect(self.x+self.z*9, self.y+self.z*4, self.z*5, self.z)
        rect(self.x+self.z, self.y+self.z*5, self.z*5, self.z)
        rect(self.x+self.z*10, self.y+self.z*5, self.z*5, self.z)
    
        
        # drew pixel(white)
        fill(255)
        stroke(255)
        rect(self.x+self.z*7, self.y+self.z*5, self.z*2, self.z)
        rect(self.x+self.z*7, self.y+self.z*6, self.z*2, self.z)
        rect(self.x+self.z*7, self.y+self.z*7, self.z*2, self.z)
        rect(self.x+self.z, self.y+self.z*7, self.z*5, self.z)
        rect(self.x+self.z*10, self.y+self.z*7, self.z*5, self.z)
        rect(self.x+self.z, self.y+self.z*8, self.z*6, self.z)
        rect(self.x+self.z*9, self.y+self.z*8, self.z*6, self.z)
        rect(self.x+self.z, self.y+self.z*9, self.z*14, self.z)
        rect(self.x+self.z, self.y+self.z*10, self.z*3, self.z)
        rect(self.x+self.z*12, self.y+self.z*10, self.z*3, self.z)
        
        # drew pixel(yellow)
        fill(245,225,155)
        stroke(245,225,155)
        rect(self.x+self.z*4, self.y+self.z*11, self.z*2, self.z)
        rect(self.x+self.z*7, self.y+self.z*11, self.z*2, self.z)
        rect(self.x+self.z*10, self.y+self.z*11, self.z*2, self.z)
        rect(self.x+self.z*3, self.y+self.z*12, self.z*3, self.z)
        rect(self.x+self.z*7, self.y+self.z*12, self.z*2, self.z)
        rect(self.x+self.z*10, self.y+self.z*12, self.z*3, self.z)
        rect(self.x+self.z*3, self.y+self.z*13, self.z*10, self.z)
        rect(self.x+self.z*4, self.y+self.z*14, self.z*8, self.z)
