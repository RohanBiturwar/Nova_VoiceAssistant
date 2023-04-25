import pygame
import math
import time
from threading import *


class gui(Thread):

    clock = pygame.time.Clock()
    canvas_width = 640
    canvas_height = 480
    RED = (255, 0, 0)
    color_r = [ pygame.Color(x , 0, 0) for x in range(255)  ]
    color_b = [ pygame.Color(0 , 0, x) for x in range(255)  ]
    color_g = [ pygame.Color(0 , x, 0) for x in range(255)  ]
    background_color = pygame.Color(0, 0, 0, 0)


    pygame.init()
    #set the window title
    pygame.display.set_caption("Nova Ai")

    # make a screen to see
    screen = pygame.display.set_mode((canvas_width, canvas_height))
    screen.fill(background_color)


    font = pygame.font.SysFont(None, 25)
    surface = pygame.Surface((canvas_width, canvas_height))
    surface.fill(background_color)

    wave = False
    circle = True

    z = 70
    change =1
    running = True

    def stopper(self):
        self._stop_event.set()


    def run(self):
        while self.running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            self.surface.fill(self.background_color)


            
            if self.circle:
                if self.z == 200:
                    self.change = -1
                elif self.z == 70:
                    self.change = 1
                self.z+=self.change
                pygame.draw.circle(self.surface , self.color_r[self.z] , (320,240), self.z , 1)
                pygame.draw.circle(self.surface , self.color_b[self.z] , (320,240), self.z-3 , 2)
                pygame.draw.circle(self.surface , self.color_g[self.z] , (320,240), self.z-2 , 1)
                message = self.font.render('Recognizing', True, self.RED)
                self.surface.blit(message, [self.canvas_width / 2 - 40, self.canvas_height / 2 - 5])
                pygame.display.update()

        



            if self.wave:
                frequency = 2
                amplitude = 50
                speed = 1
                cl=0
                for x in range(0, self.canvas_width):
                    y = int((self.canvas_height/2)+ amplitude*math.sin(frequency*((float(x)/self.canvas_width)*(2*math.pi) + (speed*time.time()))))
                   
                    if cl == 240:
                        change= -1
                    elif cl == 0:
                        change = 1
                    cl=cl+change
                    self.surface.set_at((x,y), self.color_g[cl])

            self.screen.blit(self.surface, (0, 0))
            pygame.display.flip()
            if self.circle:
                self.clock.tick(50)







