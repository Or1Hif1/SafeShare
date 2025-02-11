import pygame
from login_page import LoginPage
import threading
import socket


if __name__ == '__main__':
    screen = pygame.display.set_mode((1280, 720))
    lp = LoginPage(screen)
    while lp.running:
        if not lp.login_check and not lp.account:
            lp.login()
        else:
            lp.signup()
        print(lp.is_submit)


