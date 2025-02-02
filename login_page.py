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
        self.is_submit = False
        self.i = 0
        self.tick = 0
        self.opacity = 255
        self.is_user = True
        self.running = True
        pygame.display.set_caption('SafeShare')

    def loop(self, running):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.submit_but, (493, 543))
        render_text(self.username, bebas_font, (5, 51, 43), 345, 299, self.screen)  # White text
        render_text(len(self.password) * "*", bebas_font, (5, 51, 43), 345, 456, self.screen)  # White text
        self.tick += 1
        if self.opacity > 1:
            if self.i < 600:
                self.i += 50
            elif self.opacity > 0 and self.tick > 30:
                self.opacity -= 8
                #   print("lower")
            welcome(self.logo, self.screen, self.i, self.opacity)
            #   print("keep welcome")

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.is_submit:  # Left click (button 1 is left click)
                    mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                    #   print(f"Mouse clicked at position: ({mouse_x}, {mouse_y})")
                    if 532 < mouse_x < 532 + 216 and 582 < mouse_y < 582 + 66:
                        self.is_submit = True
                        print("Password is: " + self.password)
                        print("Username is: " + self.username)
            if not self.is_submit:
                if event.type == pygame.KEYDOWN:
                    if self.is_user:
                        key_name = pygame.key.name(event.key)
                        if str(key_name) == "backspace":
                            if len(self.username) > 0:
                                self.username = self.username[0:-1]
                        elif str(key_name) == "return":
                            self.is_user = not self.is_user
                        else:
                            if len(self.username) < 20:
                                self.username += event.unicode

                    else:
                        key_name = pygame.key.name(event.key)
                        if str(key_name) == "backspace":
                            if len(self.password) > 0:
                                self.password = self.password[0:-1]
                        elif str(key_name) == "return":
                            self.is_user = not self.is_user
                        else:
                            if len(self.username) < 20:
                                self.password += event.unicode

                    print(self.username)

            if event.type == pygame.QUIT:
                self.running = False

        pygame.display.flip()


if __name__ == '__main__':
    lp = LoginPage()
