import pygame
from cochonnet import Cochonnet
from blueboulle import Blueboulle
from pinkblueboulle import Pinkblue
from pinkpurple import Pinkpurple
from pinkyellow import Pinkyellow
from redpurple import Redpurple
from redarrow import RedArrow

# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Arial', 15)
pygame.display.set_caption("Petanque")

# set up variables for the display
SCREEN_HEIGHT = 445
SCREEN_WIDTH = 750
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pregame = True
pregame_message = "This is petanque! To play, throw your boule as close to the cochonnet as you can! Press the screen now."
name = "Hit as close to the red ball as you can!"
message = "Collision not detected"
r = 100
g = 0
b = 0
playerone_pts = 0
playertwo_pts = 0

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_screen = my_font.render(pregame_message, True, (200, 200, 200))
image = pygame.image.load('redarrow.png')
DEFAULT_IMAGE_SIZE = (150, 150)
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
image = pygame.transform.rotate(image, 265)

c = Cochonnet(375, 175)
a = RedArrow(320, 275)
bb = Blueboulle(375, 430)
pb = Pinkblue(200, 430)
pp = Pinkpurple(300, 430)
py = Pinkyellow(450, 430)
rp = Redpurple(550, 430)
bg = pygame.image.load("PetanqueBackground.png")

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True

# -------- Main Program Loop -----------
while run:

    keys = pygame.key.get_pressed()  # checking pressed keys
    if not pregame:
        c.move(375, 175)
        if keys[pygame.K_LEFT]:
            a.change_direction("left")
            print("ITS LEFT")

    # --- Main event loop
    for event in pygame.event.get():  # User did something

        if pregame:
            if event.type == pygame.MOUSEBUTTONUP:
                pregame = False
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    if not pregame:
        screen.blit(bg, (0, 0))
        screen.blit(c.image, c.rect)
        screen.blit(bb.image, bb.rect)
        screen.blit(pb.image, pb.rect)
        screen.blit(pp.image, pp.rect)
        screen.blit(py.image, py.rect)
        screen.blit(rp.image, rp.rect)
        screen.blit(image, a.rect)
    if pregame:
        screen.blit(display_screen, (50, 200))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
