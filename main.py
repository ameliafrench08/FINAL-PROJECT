import pygame


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Petanque")

# set up variables for the display
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 700
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pregame = True
pregame_message = "This is petanque! To play, throw your boule as close to the cochonnet as you can! Press the screen now."
name = "Hit as close to the red ball as you can!"
message = "Collision not detected"
r = 100
g = 0
b = 0

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_screen = my_font.render(pregame_message, True, (200, 200, 200))

# f = Fox(40, 60)
# c = Coin(200, 85)

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()  # checking pressed keys

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if pregame:
            if event.type == pygame.MOUSEBUTTONUP:
                pregame = False
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((r, g, b))
    if pregame:
        screen.blit(display_screen, (50, 200))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()



