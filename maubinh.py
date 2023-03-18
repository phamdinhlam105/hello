import pygame,sys,random

def draw_player(sur,rect_x,rect_y,height,weight):
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y),(rect_x+weight,rect_y))
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y),(rect_x,rect_y+height))
    pygame.draw.line(sur,(255,0,0),(rect_x+weight,rect_y),(rect_x+weight,rect_y+height))
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y+height),(rect_x+weight,rect_y+height))
    
pygame.init()
screen=pygame.display.set_mode((1400,700))
clock=pygame.time.Clock()
bg=pygame.image.load('FileGame/background.png')
card=pygame.image.load('FileGame/card.png')
card1=pygame.transform.chop(card,(38,80,404,240))
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg,(0,0))
    draw_player(bg,495,10,190,240)
    draw_player(bg,10,180,190,240)
    draw_player(bg,495,10,190,240)
    draw_player(bg,495,10,190,240)
    pygame.display.update()
    clock.tick(120)