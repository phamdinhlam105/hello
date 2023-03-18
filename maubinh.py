import pygame,sys,random
pygame.init()
screen=pygame.display.set_mode((1200,600))
clock=pygame.time.Clock()
bg=pygame.image.load('FileGame/background.png')

card=pygame.image.load('FileGame/card.png')
card3=pygame.transform.chop(card,(40,80,480,400))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    screen.blit(card3,(100,100))
    pygame.display.update()
    clock.tick(120)