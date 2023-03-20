import pygame,sys,random

all_card=[]
for i in range(0,52):
    all_card.append(i)

def draw_card(sur,player,card,card_id):
    if card_id<=12:
        i=card_id
    elif card_id<=25:
        i=card_id-13
    elif card_id<=38:
        i=card_id-26
    else:
        i=card_id-39
    if player==1:
        if i<3:
            sur.blit(card,((580+40*i),10))
        elif i<8:
            sur.blit(card,((580+40*(i-3),90)))
        else:
            sur.blit(card,((580+40*(i-8),170)))
    if(player==2):
        if i<3:
            sur.blit(card,(10+40*i,230))
        elif i<8:
            sur.blit(card,(10+40*(i-3),310))
        else:
            sur.blit(card,(10+40*(i-8),390))    
    if(player==3):
        if i<3:
            sur.blit(card,(580+40*i,450))
        elif i<8:
            sur.blit(card,(580+40*(i-3),530))
        else:
            sur.blit(card,(580+40*(i-8),610))
    if(player==4):
        if i<3:
            sur.blit(card,(1140+40*i,230))
        elif i<8:
            sur.blit(card,(1140+40*(i-3),310))
        else:
            sur.blit(card,(1140+40*(i-8),390))
def random_card(card):
    get_card = []
    for i in range (0,52):
        rd=random.randint(0,(51-i))
        get_card.append(card[rd])
        card.remove(card[rd])
    return get_card

def get_card(card_id):
    if card_id<13:
        card=pygame.image.load("FileGame/poker/spade/"+str(card_id+1)+".jpg")
    elif card_id<26:
        card=pygame.image.load("FileGame/poker/club/"+str(card_id-12)+".jpg")
    elif card_id<39:
        card=pygame.image.load("FileGame/poker/diamond/"+str(card_id-25)+".jpg")
    else:
        card=pygame.image.load("FileGame/poker/heart/"+str(card_id-38)+".jpg")
    return card
def draw_player(sur,rect_x,rect_y,height,weight):
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y),(rect_x+weight,rect_y))
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y),(rect_x,rect_y+height))
    pygame.draw.line(sur,(255,0,0),(rect_x+weight,rect_y),(rect_x+weight,rect_y+height))
    pygame.draw.line(sur,(255,0,0),(rect_x,rect_y+height),(rect_x+weight,rect_y+height))

pygame.init()
screen=pygame.display.set_mode((1350,700))
clock=pygame.time.Clock()
bg=pygame.image.load('FileGame/background.png')
# card=pygame.image.load('FileGame/poker/spade/A.jpg')
# card1=card
count=0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        #if event.type==pygame.MOUSEBUTTONDOWN:
            
    #draw_card(bg,all_card[3],580,10,1)
    mouse_pos=pygame.mouse.get_pos()
    # if (mouse_pos[0]>=580) & (mouse_pos[0]<=580+240):
    #     screen.blit(bg,(0,0))
    #     bg.blit(pygame.transform.scale_by(card,1.5),(580,10))
        
    # else:
    #     screen.blit(bg,(0,0))
    #     bg.blit(card,(580,10))
    screen.blit(bg,(0,0))
    draw_player(screen,580,10,240,200)
    draw_player(screen,10,230,240,200)
    draw_player(screen,580,450,240,200)
    draw_player(screen,1140,230,240,200)
    if count==0:
        randomed_card=random_card(all_card)
    if count<52:
        if count<13:
            draw_card(bg,1,get_card(randomed_card[count]),count)
            count+=1
        elif count<26:
            draw_card(bg,2,get_card(randomed_card[count]),count)
            count+=1
        elif count<39:
            draw_card(bg,3,get_card(randomed_card[count]),count)
            count+=1
        else:
            draw_card(bg,4,get_card(randomed_card[count]),count)
            count+=1
    pygame.display.update()
    clock.tick(120)