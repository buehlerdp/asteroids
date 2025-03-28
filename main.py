import pygame

from constants import *

pygame.init()

def main():
    print ("Starting Asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

while True:
    for event in pygame.event.get():
    if event.type == pygame.QUIT:
        return
    pygame.surface.fill(0,0,0)
    pygame.displacy.flip()
