import pygame
from login_page import LoginPage
import threading


if __name__ == '__main__':
    screen = pygame.display.set_mode((1280, 720))
    lp = LoginPage(screen)
    while lp.running:
        lp.loop(True)
        print(lp.is_submit)


