import pygame,sys,random,time

all_card=[]
for i in range(0,52):
    all_card.append(i)
score_player=[]
for i in range(0,12):
    score_player.append(0)
def draw_card(sur,card,card_id):
    if card_id<=12:
        i=card_id
        player=1
    elif card_id<=25:
        i=card_id-13
        player=2
    elif card_id<=38:
        i=card_id-26
        player=3
    else:
        i=card_id-39
        player=4
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
def find_card_id(mousepos):
    card_id=-1
    mouseposx=mousepos[0]
    mouseposy=mousepos[1]
    if (mouseposx > 580) & (mouseposx <780):
        if (mouseposy>10) & (mouseposy<250):
            if (mouseposy<90) & (mouseposx<700):
                card_id=round((mouseposx-580)//40)
            elif mouseposy>90:
                card_id=round((mouseposx-580)//40)+3+round((mouseposy-110)//80)*5
        elif (mouseposy>450) & (mouseposy<690):
            if (mouseposy<530) & (mouseposx<700):
                card_id=round((mouseposx-580)//40) +26
            elif mouseposy>700:
                card_id=round((mouseposx-580)//40)+3+round((mouseposy-110)//80)*5 + 26
    if (mouseposy >230) & (mouseposy<470):
        if mouseposy<310:
            if (mouseposx>10) & (mouseposx<130):
                card_id=round((mouseposx-190)//40)+13
            elif(mouseposx>1140) & (mouseposx<1260):
                card_id=round((mouseposx-190)//40)+39
        else:
            if (mouseposx>10) & (mouseposx < 210):
                card_id=round((mouseposx-10)//40)+3+round((mouseposy-390)//80)*5 + 13
            elif (mouseposx>1140) & (mouseposx<1340):
                card_id=round((mouseposx-10)//1140)+3+round((mouseposy-390)//80)*5 + 39
    return card_id
def updatewindow(randomed_card):
    draw_player(screen,580,10,240,200)
    draw_player(screen,10,230,240,200)
    draw_player(screen,580,450,240,200)
    draw_player(screen,1140,230,240,200)
    for count in range(0,52):
        if count<52:
            if count<13:
                draw_card(bg,get_card(randomed_card[count]),count)
                
            elif count<26:
                draw_card(bg,get_card(randomed_card[count]),count)
                
            elif count<39:
                draw_card(bg,get_card(randomed_card[count]),count)
                
            else:
                draw_card(bg,get_card(randomed_card[count]),count)
    screen.blit(fulltime,(520,300))
    screen.blit(pygame.transform.scale_by(time_run,(time_count,1)),(530,310))
    pygame.display.flip()
def boichung(x,y):
    if ((x==0) & (y%13==0)) | ((y==0) & (x%13==0)):
        return 13
    if x==y:
        return x
    elif x>y:
        return boichung(x-y,y)
    else:
        return boichung(x,y-x)
        
def kiemtra(chi,sochi):
    chi.sort()
    if(sochi<3):
    #tps
        if chi[0]+4==chi[1]+3==chi[2]+2==chi[3]+1==chi[4]:
            return 9
        #thung
        if chi[4]-chi[0]<13:
            return 6
        #sanh
        if chi[0]%13+4==chi[1]%13+3==chi[2]%13+2==chi[3]%13+1==chi[4]%13:
            return 5 
    #doi,xam,culu,tuquy
    doi=0
    trung_doi=0
    for i in range(0,len(chi)):
        for j in range(i+1,len(chi)):
            if boichung(chi[i]-chi[i]%13,chi[j+1]-chi[i]%13)==13:
                doi+=1
    if doi==1:
        return 2 #doi
    if doi==2:
        return 3 #thu
    if doi==3:
        return 4 #xam
    if doi==4:
        return 7 #culu
    if doi==6:
        return 8 #tuquy
    return 1
        

def Score(card_list):
    for i in range(0,4):
        chi1= [card_list[i*13+8],card_list[i*13+9],card_list[i*13+10],card_list[i*13+11],card_list[i*13+12]]
        score_player[i*3]=kiemtra(chi1)
        chi2= [card_list[i*13+3],card_list[i*13+4],card_list[i*13+5],card_list[i*13+6],card_list[i*13+7]]
        score_player[i*3+1]=kiemtra(chi2)
        chi3= [card_list[i*13],card_list[i*13+1],card_list[i*13+2]]
        score_player[i*3+2]=kiemtra(chi3)
pygame.init()
global screen
global bg
screen=pygame.display.set_mode((1350,700))
clock=pygame.time.Clock()
bg=pygame.image.load('FileGame/background.png')
fulltime=pygame.image.load('FileGame/time.png')
time_run=pygame.image.load('FileGame/time_run.png')
time_count=0.1
count=0
mouse_pos=(0,0)
anim=1
card_need_to_change=-1
start_time=time.time()

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            card_id_before=find_card_id(mouse_pos)
            if card_id_before==-1:
                mouse_pos=(0,0)
            else:
                anim=0
                card_need_to_change=card_id_before
        if event.type==pygame.MOUSEBUTTONUP:
            anim=1
            if mouse_pos!=(0,0):
                mouse_pos_after=pygame.mouse.get_pos()
                card_id_after=find_card_id(mouse_pos_after)
                if card_id_after!=-1:
                    x=randomed_card[card_id_before]
                    randomed_card[card_id_before]=randomed_card[card_id_after]
                    randomed_card[card_id_after]=x
                    card_id_after=-1
                mouse_pos=(0,0)

    screen.blit(bg,(0,0))
    #initialize all card random
    if count==0:
        randomed_card=random_card(all_card)
        count+=1
    #drag a card
    if (anim==0) & (card_need_to_change!=-1):
        updatewindow(randomed_card)
        pos=pygame.mouse.get_pos()
        screen.blit(get_card(randomed_card[card_need_to_change]),(pos[0]-20,pos[1]-40))
        pygame.display.update(pos[0]-20,pos[1]-40,40,80)
    else:
        updatewindow(randomed_card)
    #time running
    if time_count<3.2:
        if time.time()-start_time>0.1:
            time_count+=0.01
            start_time=time.time()
    
    clock.tick(120)