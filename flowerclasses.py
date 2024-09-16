import pygame
pygame.init

#constants for colors
RED = (250,0,0)
ORANGE = (200, 100, 0)
GREEN = (0,150, 0)
GREEN2 = (0,150,85)
GREEN3 = (85,150,0)

### class definition--------------------------------------------
class flower:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.rect(screen, (GREEN), (self.xpos-10, self.ypos+20, 20, 100)) #(190, 330) is my top left corner
        pygame.draw.circle(screen, (RED), (self.xpos-20, self.ypos+20), 20) 
        pygame.draw.circle(screen, (RED), (self.xpos-20, self.ypos-20), 20) 
        #add missing petals here
        pygame.draw.circle(screen, (RED), (self.xpos+20, self.ypos-20), 20)
        pygame.draw.circle(screen, (RED), (self.xpos+20, self.ypos+20), 20)
        pygame.draw.circle(screen, (ORANGE), (self.xpos, self.ypos), 20) 
        

# end of class definition-----------------------------------------
class clover:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        
    def draw(self):
        pygame.draw.rect(screen, (GREEN), (self.xpos-10, self.ypos+20, 20, 100)) #(190, 330) is my top left corner
        pygame.draw.rect(screen, (GREEN), (self.xpos-20, self.ypos-20, 50, 50))
        pygame.draw.circle(screen, (GREEN), (self.xpos-20, self.ypos+20), 20) 
        pygame.draw.circle(screen, (GREEN2), (self.xpos-20, self.ypos-20), 20) 
        pygame.draw.circle(screen, (GREEN3), (self.xpos+20, self.ypos-20), 20)
        pygame.draw.circle(screen, (GREEN2), (self.xpos+20, self.ypos+20), 20)
        

#stamp (aka instantiate) flowers
flower1 = flower(200, 200)
flower2 = flower(400, 400)
flower3 = flower(100, 400)
clover1 = clover(400, 200)
clover2 = clover(400, 600)
clover3 = clover(300, 200)

#creates game screen and caption
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("flower class demo")

#game variables
doExit = False #variable to quit out of game loop
clock = pygame.time.Clock() #sets up a game clock to regulate game speed


#BEGIN GAME LOOP######################################################
while not doExit:
   
    clock.tick(60) #FPS (frames per second)
   
    #pygame's way of listening for events (key presses, mouse clicks, etc)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           doExit = True #lets you quit program

    #keyboard input-----------------------------------
  
     
    #render section-----------------------------------
 

    #draw class objects
    flower1.draw()
    flower2.draw()
    flower3.draw()
    clover1.draw()
    clover2.draw()
    clover3.draw()
  

    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()
