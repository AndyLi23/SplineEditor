import numpy as np
import pygame
import time

from Spline import *
from rasterize import *

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Beziers :)")
        self.width = 1200
        self.height = 800
        self.screen = pygame.display.set_mode((self.width, self.height))
        
        self.splines = []
        self.splines.append(Spline(100))
        
        self.selected = (-1, -1, -1)
        self.clicked = False
        self.prev_pos = (0, 0)


    def run(self):   
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                pygame.quit()
            
            if(event.type == pygame.MOUSEBUTTONDOWN):
                self.clicked = True
                self.prev_pos = pygame.mouse.get_pos()
                
                for i in range(len(self.splines)):
                    beziers = self.splines[i].get_beziers()
                    for j in range(len(beziers)):
                        s = self.get_selected(beziers[j].get_points(), self.prev_pos, 8)
                        if(s != -1):
                            self.selected = (i, j, s)
                                                    
            
            if(event.type == pygame.MOUSEBUTTONUP):
                self.clicked = False    
                self.selected = (-1, -1, -1)
                
        # math stuff
        if(self.selected != (-1, -1, -1)):
            cur_pos = (min(pygame.mouse.get_pos()[0], 800), min(pygame.mouse.get_pos()[1], 800))
            
            self.splines[self.selected[0]].edit_bezier_point(self.selected[1], self.selected[2], (cur_pos[0]-self.prev_pos[0], cur_pos[1]-self.prev_pos[1]))
            
            self.prev_pos = cur_pos
        
    
        # render stuff                    
        self.screen.fill((10, 10, 10))
        
        
        for i in range(100):
            pygame.draw.line(self.screen, (20, 20, 20), (0, i*8), (800, i*8), 1)
            pygame.draw.line(self.screen, (20, 20, 20), (i*8, 0), (i*8, 800), 1)
            
            
        for i in range(len(self.splines)):
            beziers = self.splines[i].get_beziers()
            for j in range(len(beziers)):
                self.render_bezier(beziers[j], (i == self.selected[0] and j == self.selected[1]), self.selected[2], 1)
                
            for j in range(len(beziers)):
                self.render_bezier(beziers[j], (i == self.selected[0] and j == self.selected[1]), self.selected[2], 0)
                
            for j in range(len(beziers)):
                self.render_bezier(beziers[j], (i == self.selected[0] and j == self.selected[1]), self.selected[2], 2)
        
            
        pygame.display.flip()
        
        time.sleep(0.01)   
        
    def render_bezier(self, bezier, sel, seli, points_):
        curve = bezier.get_curve()
        points = bezier.get_points()
        
        if(points_ == 0):
            for p in range(len(points)):
                if(sel and p == seli):
                    pygame.draw.circle(self.screen, (0, 255, 0), points[p], 8)   
                else:
                    pygame.draw.circle(self.screen, (255, 0, 0), points[p], 8)   
                
        if(points_ == 1):
            prev = points[0]
            for p in range(len(points)):
                r = plotLine(int(prev[0]), int(prev[1]), int(points[p][0]), int(points[p][1]))
                for i in r:
                    self.screen.set_at(i, (80, 80, 80))
                prev = points[p]  
        
        if(points_ == 2):
            prev = curve[0]  
            for p in curve:
                r = plotLine(int(prev[0]), int(prev[1]), int(p[0]), int(p[1]))
                for i in r:
                    self.screen.set_at(i, (255,255,255))
                prev = p
                        
            
    def get_selected(self, points, pos, threshold):
        for i in range(len(points)):
            if((points[i][0]-pos[0])**2 + (points[i][1]-pos[1])**2)<threshold**2:
                return i
        return -1

if __name__ == '__main__':
    game = Game()
    while(True):
        game.run()