import pygame,sys,random

def draw_card(sur,card_id,player_pos_x,player_pos_y,card_pos):
    if card_id<13:
        sur.blit(pygame.transform.chop(card,(38,80,480-38*card_id,240)),(player_pos_x,player_pos_y))

def draw_player(sur,rect_x,rect_y,height,weight):
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y),(rect_x+weight,rect_y))
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y),(rect_x,rect_y+height))
    pygame.draw.line(sur,(255,0,0),(rect_x+weight,rect_y),(rect_x+weight,rect_y+height))
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y+height),(rect_x+weight,rect_y+height))
    
pygame.init()
screen=pygame.display.set_mode((1350,700))
clock=pygame.time.Clock()
bg=pygame.image.load('FileGame/background.png')
card=pygame.image.load('FileGame/card.png')
card1=pygame.transform.chop(card,(76,80,404,240))
card2=pygame.transform.chop(card,(0,80,404,240))
pygame.Surface.subsurface
all_card= [0]
for i in range(1,52):
    all_card+=[i]
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type==pygame.MOUSEBUTTONDOWN:
            
    screen.blit(bg,(0,0))
    draw_player(screen,580,10,240,190)
    draw_player(screen,10,230,240,190)
    draw_player(screen,580,450,240,190)
    draw_player(screen,1150,230,240,190)
    #draw_card(bg,all_card[3],580,10,1)
    bg.blit(card2,(580,10))

    #mouse_pos=pygame.mouse.get_pos()
    
    pygame.display.update()
    clock.tick(120)