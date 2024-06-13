import pygame
import math
import time
from cochonnet import Cochonnet
from blueboulle import Blueboulle
from redarrow import RedArrow
from scale import Scale
from scalerline import ScaleLine


def round_number(x, base=5):
    return base * round(x / base)


def degrees_to_radians(degrees):
    degrees = 5 * round(degrees / 5)
    radians = degrees * (math.pi / 180)
    return radians


def find_coordinates(radians):
    num_ratio = round(add_length / math.sin(radians))
    x_coord = num_ratio * math.cos(radians)
    bb.move_direction(speed, x_coord + 375, add_length)


def find_distance(boulle_x, boulle_y, coch_x, coch_y):
    distance = round(math.sqrt(((coch_x - boulle_x) ** 2) + ((coch_y - boulle_y) ** 2)))
    return distance


# set up pygame modules
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Times New Roman', 20)
pygame.display.set_caption("Petanque")

# set up variables for the display
SCREEN_HEIGHT = 445
SCREEN_WIDTH = 750
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)

pregame = True
pregame_message = "To play, move the arrow and hit space to throw! Press enter to end. Press the screen now."
name = "Hit as close to the red ball as you can!"
message = "Collision not detected"
postgame_message = ""
r = 100
g = 0
b = 0
playerone_pts = 0
playertwo_pts = 0
speed_shoot = 2
direction = 0
speed = 0
swap_sign = 1
space_ball = 0
first_time = 0
is_over = False
bb_distance = 0

# render the text for later
display_name = my_font.render(name, True, (255, 255, 255))
display_message = my_font.render(message, True, (255, 255, 255))
display_screen = my_font.render(pregame_message, True, (200, 200, 200))
display_distance = my_font.render("", True, (200, 200, 200))
display_postgame = my_font.render("", True, (200, 200, 200))
image = pygame.image.load('redarrow.png')
DEFAULT_IMAGE_SIZE = (150, 150)
image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
image = pygame.transform.rotate(image, 270)
real_angle = 270

c = Cochonnet(375, 175)
a = RedArrow(320, 275)
bb = Blueboulle(375, 430)
s = Scale(0, 2)
sl = ScaleLine(20, 220)
bg = pygame.image.load("PetanqueBackground.png")
full_angle = 90
change_goto = 1
add_length = 0
highscore_bool = False
h = open("highscores", "r")
highscore = h.readline().strip()
highscore_achieved = "You got a new highscore!"
highscore_not = "You didn't achieve a new highscore"
display_highscore = my_font.render(highscore_achieved, True, (255, 255, 255))
display_not_high = my_font.render(highscore_not, True, (255, 255, 255))

# The loop will carry on until the user exits the game (e.g. clicks the close button).
run = True
# -------- Main Program Loop -----------
while run:
    if space_ball == 1 and speed_shoot == 1 and not is_over:
        coord_input = degrees_to_radians(full_angle)
        find_coordinates(coord_input)
        # # SPEED SHOOT MAKES THE BALL NOT MOVE!!!!!!!!!
        real_angle_round = round_number(full_angle)
        bb_distance = str(find_distance(bb.x, bb.y, 375, 175))
        display_distance = my_font.render("Distance: " + bb_distance, True, (0, 0, 0))
        postgame_message = "You got " + str(bb_distance) + " away from the cochonnet!"
        display_postgame = my_font.render(postgame_message, True, (200, 200, 200))


        # REAL ANGLE IS ALWAYS 90::::: FIX THAT
        # FOR NEXT TIME: Fix the math for the boulle bleu. Keeps going to kinda random coordinates.

    keys = pygame.key.get_pressed()  # checking pressed keys
    if not pregame:
        c.move(375, 175)
        if 2 <= sl.y <= 438 and direction == 0:
            sl.move_direction("down")
        if sl.y >= 438:
            direction = 1
            sl.move_direction("up")
        if direction == 1:
            sl.move_direction("up")
        if sl.y <= 2:
            direction = 0
        if direction == 0:
            sl.move_direction("down")

        # !!!CHANGING DIRECTION OF THE ARROW!!!
        if keys[pygame.K_LEFT]:
            # a.change_direction("left")
            image = pygame.image.load('redarrow.png')
            DEFAULT_IMAGE_SIZE = (150, 150)
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            image = pygame.transform.rotate(image, (full_angle + 1))
            bbimage = pygame.image.load('blueboulle.png')
            bbimage = pygame.transform.rotate(bbimage, (full_angle + 1))
            full_angle += 1
            if full_angle > 360:
                full_angle = full_angle / 360
                full_angle = round(full_angle)
            print(full_angle)
            a.move(320, 275)
            # if swap_sign == 1:
            #     full_angle = full_angle * -1
            #     swap_sign = 0

        if keys[pygame.K_RIGHT]:
            image = pygame.image.load('redarrow.png')
            DEFAULT_IMAGE_SIZE = (150, 150)
            image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)
            image = pygame.transform.rotate(image, (full_angle - 1))
            bbimage = pygame.image.load('blueboulle.png')
            bbimage = pygame.transform.rotate(bbimage, (full_angle - 1))
            full_angle -= 1
            if full_angle > 360:
                full_angle = full_angle / 360
                full_angle = round(full_angle)
            print(full_angle)
            a.move(320, 275)
            # if swap_sign == 1:
            #     full_angle = full_angle * -1
            #     swap_sign = 0

        # !!!SPEED!!!
        if keys[pygame.K_SPACE] and speed_shoot == 1:
            speed_shoot = 2
            direction = 2  # SAYS THE THING SHOULDN'T MOVE
            if 2 <= sl.y <= 32:
                # TOO FAST
                speed = 0.6
            elif 32.1 <= sl.y <= 190:
                # FAST
                speed = 0.4
            elif 190.1 <= sl.y <= 250:
                # GREEN
                speed = 0.3
            elif 250.1 <= sl.y <= 338:
                # SLOW
                speed = 0.2
            elif 338.1 <= sl.y <= 438:
                # VERY SLOW
                speed = 0.1

        # !!!SHOOTING BLUE BALL!!!
        if keys[pygame.K_SPACE] and speed_shoot == 2:
            speed_shoot = 1
            if speed == 0.1:
                add_length = 160
            elif speed == 0.2:
                add_length = 170
            elif speed == 0.3:
                add_length = 180
            elif speed == 0.4:
                add_length = 190
            elif speed == 0.6:
                add_length = 200
            space_ball = 1

        if keys[pygame.K_RETURN]:
            is_over = True
            h = open("highscores", "r")
            highscore = h.readline().strip()
            h.close()
            if int(bb_distance) < int(highscore):
                highscore = bb_distance
                h = open("highscores", "w")
                h.write(str(highscore))
                h.close()
                highscore_bool = True

    # --- Main event loop
    for event in pygame.event.get():  # User did something

        if pregame:
            if event.type == pygame.MOUSEBUTTONUP:
                pregame = False
        if event.type == pygame.QUIT:  # If user clicked close
            run = False

    screen.fill((0, 0, 0))
    if not pregame:
        if not is_over:
            screen.blit(bg, (0, 0))
            screen.blit(c.image, c.rect)
            screen.blit(bb.image, bb.rect)
            screen.blit(image, a.rect)
            screen.blit(s.image, s.rect)
            screen.blit(sl.image, sl.rect)
            screen.blit(display_distance, (40, 15))
        if is_over:
            screen.fill((101, 0, 11))
            screen.blit(display_postgame, (275, 200))
            if highscore_bool:
                screen.blit(display_highscore, (275, 250))
            else:
                screen.blit(display_not_high, (275, 250))
    if pregame:
        screen.blit(display_screen, (10, 200))
    pygame.display.update()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
