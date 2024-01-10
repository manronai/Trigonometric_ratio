import sys
import pygame
import math

pygame.init()

Pi = math.pi
screen = pygame.display.set_mode()
FPSCLOCK = pygame.time.Clock()
RED = pygame.Color("red")
WHITE = pygame.Color("white")
BLUE = pygame.Color('blue')
GREEN = pygame.Color('green')
YELLOW = pygame.Color('yellow')
startpoint = pygame.math.Vector2(320, 240)
endpoint = pygame.math.Vector2(170, 0)
angle = 0
font = pygame.font.Font('freesansbold.ttf', 32)

done = False
def degree(h, o):
    return round(math.degrees(math.asin(o/h)), 2)
def ratio(h, o):
    return round(o/h, 2)
def length(a, b, name):
    c = a[0]-b[0]
    d = a[1]-b[1]
    r = math.sqrt(math.pow(c, 2)+math.pow(d, 2))
    if('o'==name):
        if (b[1]>240):
            return -1*r
        else:
            return r
    if 'a'==name:
        if (b[0]<320):
            return -1*r
        else:
            return r
    return r
flag = 0
pygame.display.set_caption('Trigonometric Ratio')
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                flag = 1
            if event.key == pygame.K_c:
                flag = 0

    # % 360 to keep the angle between 0 and 360.
    if flag == 0:
        angle = (angle-0.1) % 360
    # The current endpoint is the startpoint vector + the
    # rotated original endpoint vector.
    current_endpoint = startpoint + endpoint.rotate(angle)

    screen.fill((0, 0, 0))

    hypotenuse = length(startpoint, current_endpoint, 'h')
    opposite = length((current_endpoint[0], 240), current_endpoint, 'o')
    adjacent = length(startpoint, (current_endpoint[0], 240), 'a')

    pygame.draw.line(screen, RED, startpoint, current_endpoint, 2) #hypotenius
    pygame.draw.line(screen, WHITE, (startpoint[0], 0), (startpoint[0], 2*startpoint[1]), 2)
    pygame.draw.line(screen, WHITE, (0, startpoint[1]), (2*startpoint[0], startpoint[1]), 2)
    pygame.draw.line(screen, GREEN, (current_endpoint[0], 240), current_endpoint, 2) #opposite

    pygame.draw.line(screen, BLUE, startpoint, (current_endpoint[0], 240), 2) #adjacent

    text = font.render(str(round(opposite, 2)), True, GREEN)
    screen.blit(text, (700, 9))
    pygame.draw.line(screen, WHITE, (700, 9+32), (800, 9+32), 2)
    text = font.render(str(round(hypotenuse, 2)), True, RED)
    screen.blit(text, (700, 18+32))
    text = font.render(str(round(adjacent, 2)), True, BLUE)
    screen.blit(text, (700, 27+32+32))
    pygame.draw.line(screen, WHITE, (700, 27+32 + 32+32), (800, 27+32 + 32+32), 2)
    text = font.render(str(round(hypotenuse, 2)), True, RED)
    screen.blit(text, (700, 36+32 + 32+32))

    #screen.blit(font.render('sin'+str(degree(hypotenuse, opposite))+'°', True, WHITE), (530, 32))
    screen.blit(font.render('sin'+str(round(360-angle, 2))+'°', True, WHITE), (530, 32))
    screen.blit(font.render(str(ratio(hypotenuse, opposite)), True, WHITE), (850, 32))
    screen.blit(font.render('=', True, WHITE), (670, 32))
    screen.blit(font.render('=', True, WHITE), (820, 32))

    #cos
    screen.blit(font.render('cos' + str(round(360 - angle, 2)) + '°', True, WHITE), (530, 18+32 + 32+32))
    screen.blit(font.render(str(ratio(hypotenuse, adjacent)), True, WHITE), (850, 18+32 + 32+32))
    screen.blit(font.render('=', True, WHITE), (670, 18+32 + 32+32))
    screen.blit(font.render('=', True, WHITE), (820, 18+32 + 32+32))
    #negative or positive mark condition
    if current_endpoint[0]>320:
        screen.blit(font.render('+', True, WHITE), (current_endpoint[0]-20, 250))

    else:
        screen.blit(font.render('-', True, WHITE), (current_endpoint[0]-20, 250))
    if current_endpoint[1]<240:
        screen.blit(font.render('+', True, WHITE), (current_endpoint[0]+10, current_endpoint[1]+10))

    else:
        screen.blit(font.render('-', True, WHITE), (current_endpoint[0]+10, current_endpoint[1]+10))

    #arc
    pygame.draw.arc(screen, WHITE, [320-50, 240-50, 100, 100], 0, math.radians(360-angle), 2)

    pygame.display.flip()
    FPSCLOCK.tick(30)



pygame.quit()
sys.exit()