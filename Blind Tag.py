import pygame as pg
import random
pg.init()
screen = pg.display.set_mode((1000, 600))
pg.display.set_caption("Blind Tag")
x = 50
y = 50
width = 60
height = 60
vel = 5
x2 = 500
y2 = 500
width2 = 60
height2 = 60
vel2 = 5
pause = False
run = True
while run:   
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    keys = pg.key.get_pressed()
    if keys[pg.K_p]:
        pause = True
    if keys[pg.K_f]:
        pause = False
    if pause == False:
        if keys[pg.K_a] and x > vel:
            x -= vel
        if keys[pg.K_d] and x < 1000 - width - vel:
            x += vel
        if keys[pg.K_w] and y > vel:
            y -= vel
        if keys[pg.K_s] and y < 600 - height - vel:
            y += vel
        if keys[pg.K_LEFT] and x > vel:
            x -= vel
        if keys[pg.K_RIGHT] and x < 1000 - width - vel:
            x += vel
        if keys[pg.K_UP] and y > vel:
            y -= vel
        if keys[pg.K_DOWN] and y < 600 - height - vel:
            y += vel
        if run == True:
            pg.time.delay(100)
            y2 -= 100
            x2 += random.uniform(-50, 50)
            y2 += random.uniform(-50, 50)
            if y2 < vel2:
                y2 += 250
            if x2 < vel2:
                x2 += 250
            if x2 > 1000 - width2 - vel2:
                x2 -= 250
            if y2 > 600 - height2 - vel2:
                y2 += 250
        screen.fill(('White'))
        player = pg.draw.rect(screen, (0, 0, 0), (x, y, width, height)) 
        tagger = pg.draw.rect(screen, (255, 0, 0), (x2, y2, width2, height2))
        if player.colliderect(tagger):
            run = False    
        pg.display.update()
pg.quit()