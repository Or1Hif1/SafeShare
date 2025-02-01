import pygame
import threading

class MyGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.screen.fill((255, 255, 255))
            pygame.display.flip()

# Creating two instances in different threads
game1 = MyGame()
game2 = MyGame()

thread1 = threading.Thread(target=game1.run)
thread2 = threading.Thread(target=game2.run)

thread1.start()
thread2.start()