import pygame
from login_page import LoginPage

if __name__ == '__main__':
    screen = pygame.display.set_mode((1280, 720))

    lp = LoginPage(screen)
    lp.loop()

