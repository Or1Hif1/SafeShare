import pygame

# import the pygame module
import pygame
pygame.init()
bebas_font = pygame.font.SysFont("Bebas-Regular", 35)


def render_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)  # True enables anti-aliasing
    screen.blit(text_surface, (x, y))


background_colour = (217, 217, 217)
screen = pygame.display.set_mode((1280, 720))

bg = pygame.image.load("images/login_back.png")
submit_but = pygame.image.load("images/submit_button.png")

pygame.display.set_caption('SafeShare')

screen.fill(background_colour)

running = True
username = ""
is_user = True
password = ""
is_submit = False
while running:
    screen.blit(bg, (0, 0))
    screen.blit(submit_but, (493,543))
    render_text(username, bebas_font, (5, 51, 43), 345, 299)  # White text
    render_text(len(password)*"*", bebas_font, (5, 51, 43), 345, 456)  # White text

    # for loop through the event queue
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not is_submit:  # Left click (button 1 is left click)
                mouse_x, mouse_y = pygame.mouse.get_pos()  # Get mouse position
                #   print(f"Mouse clicked at position: ({mouse_x}, {mouse_y})")
                if 532 < mouse_x < 532+216 and 582 < mouse_y < 582+66:
                    is_submit = True
                    print("Password is: "+password)
                    print("Username is: "+username)
        if not is_submit:
            if event.type == pygame.KEYDOWN:
                if is_user:
                    key_name = pygame.key.name(event.key)
                    if str(key_name) == "backspace":
                        if len(username) > 0:
                            username = username[0:-1]
                    elif str(key_name) == "return":
                        is_user = not is_user
                    else:
                        if len(username) < 20:
                            username += event.unicode

                else:
                    key_name = pygame.key.name(event.key)
                    if str(key_name) == "backspace":
                        if len(password) > 0:
                            password = password[0:-1]
                    elif str(key_name) == "return":
                        is_user = not is_user
                    else:
                        if len(username) < 20:
                            password += event.unicode

                print(username)

        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
