import pygame
import random

class Slither10_game:


    def __init__(self,w=640,h=480):
        self.w = w
        self.h = h
        # init display
       
        #init gamestate 
    def play_step(self):
        pass

if __name__ == '__main__':
    game = Slither10_game()

    #game loop
    while True:
        game.play_step()

        # break if game over


    pygame.quit()