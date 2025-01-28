import pygame
pygame.init()
bebas_font = pygame.font.SysFont("Bebas-Regular", 35)


def render_text(text, font, color, x, y, screen):
    text_surface = font.render(text, True, color)  # True enables anti-aliasing
    screen.blit(text_surface, (x, y))


def welcome(logo, screen, index, opacity):
    bg = pygame.image.load("images/welcome_bg.png")
    logo = logo
    bg.set_alpha(opacity)
    logo.set_alpha(opacity)
    screen.blit(bg, (0, 0))
    screen.blit(logo, (445, -500+index))


class LoginPage:
    def __init__(self, screen):
        self.screen = screen
        self.username = ""
        self.password = ""
        self.bg = pygame.image.load("images/login_back.png")
        self.submit_but = pygame.image.load("images/submit_button.png")
        self.logo = pygame.image.load("images/logosafe2.png")
        pygame.display.set_caption('SafeShare')

    def loop(self):
        running = True
        is_user = True
        is_submit = False
        i = 0
        opacity = 255
        tick = 0
        while running:
            self.screen.blit(self.bg, (0, 0))
            self.screen.blit(self.submit_but, (493, 543))
            render_text(self.username, bebas_font, (5, 51, 43), 345, 299, self.screen)  # White text
            render_text(len(self.password) * "*", bebas_font, (5, 51, 43), 345, 456, self.screen)  # White text
            tick += 1
            if opacity > 1:
                if i < 600:
                    i += 50
                elif opacity > 0 and tick > 30:
                    opacity -= 8
                    #   print("lower")
                welcome(self.logo, self.screen, i, opacity)
                #   print("keep welcome")

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1 and not is_submit:  # Left click (button 1 is left click)
                        mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                        #   print(f"Mouse clicked at position: ({mouse_x}, {mouse_y})")
                        if 532 < mouse_x < 532 + 216 and 582 < mouse_y < 582 + 66:
                            is_submit = True
                            print("Password is: " + self.password)
                            print("Username is: " + self.username)
                if not is_submit:
                    if event.type == pygame.KEYDOWN:
                        if is_user:
                            key_name = pygame.key.name(event.key)
                            if str(key_name) == "backspace":
                                if len(self.username) > 0:
                                    self.username = self.username[0:-1]
                            elif str(key_name) == "return":
                                is_user = not is_user
                            else:
                                if len(self.username) < 20:
                                    self.username += event.unicode

                        else:
                            key_name = pygame.key.name(event.key)
                            if str(key_name) == "backspace":
                                if len(self.password) > 0:
                                    self.password = self.password[0:-1]
                            elif str(key_name) == "return":
                                is_user = not is_user
                            else:
                                if len(self.username) < 20:
                                    self.password += event.unicode

                        print(self.username)

                if event.type == pygame.QUIT:
                    running = False

            pygame.display.flip()



