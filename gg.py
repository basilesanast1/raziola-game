import pygame
pygame.init()

win = pygame.display.set_mode((650,500))
pygame.display.set_caption('Η ΡΑΖΙΟΛΑ ΑΠΕΧΕΙ 5 ΜΕΤΡΑ ΜΑΚΡΙΑ ΣΟΥ. ΚΑΝΕ ΚΛΙΚ ΕΔΩ ΓΙΑ ΝΑ ΜΑΘΕΙΣ')
sq = pygame.Rect(0,0,50,50)
imm = pygame.image.load('2065.jpg')
im = pygame.transform.scale(imm,(650,500))
red = (255,0,0)
vel = 15
fps = 60
white = (255,255,255)
run = True
while run:
    clock = pygame.time.Clock()
    clock.tick(fps)
    win.fill(white)
    win.blit(im,(0,0))
    pygame.draw.rect(win,red,sq)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and sq.y >=15:
        sq.y -= vel
    if keys[pygame.K_s] and sq.y <=435:
        sq.y += vel
    if keys[pygame.K_d] and sq.x <=595:
        sq.x += vel
    if keys[pygame.K_a] and sq.x >=15:
        sq.x -= vel
