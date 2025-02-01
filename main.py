import pygame
from login_page import LoginPage
import threading


if __name__ == '__main__':
    screen = pygame.display.set_mode((1280, 720))
    lp = LoginPage(screen)
    loop = threading.Thread(target=lp.loop, args=())
    lp2 = LoginPage(screen)
    loop2 = threading.Thread(target=lp2.loop, args=())
    loop.start()
    loop2.start()



