import pygame as py
import random as r

py.init()
screen = py.display.set_mode((1000, 1000))

py.display.set_caption('PacMan!')

PacmanUp = py.image.load("C:\ComputerScience\PacMan!\PacmanUp.png")
PacmanUp = py.transform.scale(PacmanUp, (330, 300))

PacmanDown = py.image.load("C:\ComputerScience\PacMan!\PacmanDown.png")
PacmanDown = py.transform.scale(PacmanDown, (330, 300))

PacmanLeft = py.image.load("C:\ComputerScience\PacMan!\PacmanLeft.png")
PacmanLeft = py.transform.scale(PacmanLeft, (330, 300))

PacmanRight = py.image.load("C:\ComputerScience\PacMan!\PacmanRight.png")
PacmanRight = py.transform.scale(PacmanRight, (330, 300))

PacmanNeutral = py.image.load("C:\ComputerScience\PacMan!\PacmanNeutral.png")
PacmanNeutral = py.transform.scale(PacmanNeutral, (330, 300))


Bg = py.image.load("C:\ComputerScience\PacMan!\Pacbg.png")
Bg = py.transform.scale(Bg, (1000, 1000))

GameSurface = py.surface.Surface((1280, 720))

Cherry = py.image.load("C:\ComputerScience\PacMan!\CherryMousekey.png")
Cherry = py.transform.scale(Cherry, (150,150))

circle_pos = (1280/2, 720/2)

# p_rect = py.Rect(0, 0, 100, 100) 

# x and y are height and width pygame. draw. circle(screen, (r,g,b), (x, y), R, w) #(r, g, b) is color, (x, y) is center, R is radius and w is the thickness of the circle border

p_rect = py.draw.circle(screen, "yellow", circle_pos, 50, 100)
e_rect = py.Rect(500, 500, 100, 100)

score = 0
boom = 0

py.font.init()
font = py.font.Font(None, 50)  

clock = py.time.Clock()

while True:
    screen.fill('black')

    py.font.init()
    font = py.font.Font(None, 50)   

    Bg_rect = Bg.get_rect(topleft=(0, 0))
    #screen.blit(Bg, Bg_rect)

    for event in py.event.get():
        if event.type == py.QUIT:
            py.QUIT
            exit()

    mouse_pos = py.mouse.get_pos()

    py.mouse.set_visible(False)

    py.draw.rect(screen, (0, 0, 0), p_rect)
    py.draw.rect(screen, 'black', e_rect)

    keys = py.key.get_pressed()

    if keys[py.K_UP]:
        p_rect.y -= 5
        screen.blit(PacmanUp, p_rect)
    elif keys[py.K_DOWN]:
        p_rect.y += 5
        screen.blit(PacmanDown, p_rect)
    elif keys[py.K_LEFT]:
        p_rect.x -= 5
        screen.blit(PacmanLeft, p_rect)
    elif keys[py.K_RIGHT]:
        p_rect.x += 5
        screen.blit(PacmanRight, p_rect)
    else:
        screen.blit(PacmanNeutral, p_rect)

    if p_rect.colliderect(e_rect):
        e_rect.x = r.randint(0,900)
        e_rect.y = r.randint(0,900)
        score +=1
        #boom +=1
    score_text = font.render(str(score), True, (255, 255, 255), None)
    score_rect = score_text.get_rect(center = (500, 50))
    screen.blit(score_text, score_rect)
    
    #time_taken = 0
    #clock.tick(60)
    #time_taken += 1/60

    #if boom ==5:
        #font = py.font.Font(None, 32)
        #clear = '#00000000'
        #average = time_taken
        #text = font.render(str(average), True, (0, 0, 0))
        #text_rect = text.get_rect()
        #text_rect.center = (500, 400)
        #screen.blit(text, text_rect)
        #screen.blit(score_text, score_rect)

    screen.blit(Cherry, e_rect)

    py.display.update()
