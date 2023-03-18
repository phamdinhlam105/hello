import pygame,sys,random,time

def drawfloor(x_pos,floor):
    
    screen.blit(floor,(x_pos,272))
    screen.blit(floor,(x_pos+216,272))
def drawpipe(x,y,pipe,tao_cot):
    if tao_cot>=1:
            screen.blit(pipe,(x,y))


pygame.init()
screen=pygame.display.set_mode((216,384))
clock=pygame.time.Clock()

bg=pygame.image.load('FileGame/assets/background-night.png')
floor=pygame.image.load('FileGame/assets/floor.png')
floor_x_pos = 0

bird_anim1=pygame.image.load('FileGame/assets/yellowbird-midflap.png')
bird_anim2=pygame.image.load('FileGame/assets/yellowbird-upflap.png')
bird_anim3=pygame.image.load('FileGame/assets/yellowbird-downflap.png')
bird=bird_anim1
bird_rect=bird.get_rect(center=(80,172))

game_over=pygame.image.load('FileGame/assets/gameover.png')

flag=0
gravity=0.08
bird_movement=0
tao_cot=1
bird_anim=0
pipe=pygame.image.load('FileGame/assets/pipe-green.png')
pipe_rect=pipe.get_rect(center=(216,140))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement=-2

   
    screen.blit(bg,(0,0))
    if (bird_rect.right >= pipe_rect.centerx) &  (bird_rect.left<= pipe_rect.centerx+41):
        if (bird_rect.bottom >=pipe_rect.centery) | (bird_rect.top <= pipe_rect.centery-80):
            flag=1
    else:
        flag=0
    if flag==1:
        bg.blit(game_over,(12,68))
    else:
        bird_movement+=gravity
        bird_rect.centery+=bird_movement
        
        floor_x_pos -= 1.25
        if floor_x_pos <= -216:
            floor_x_pos=0
        drawfloor(floor_x_pos,floor)
        bird_anim+=1
        if bird_anim==2:
            bird_anim=0
            bird=bird_anim1
        if bird_anim==1:
            bird=bird_anim2
        if bird_anim==2:
            bird=bird_anim3
        screen.blit(bird,(bird_rect))
        pipe_rect.centerx-=1

        drawpipe(pipe_rect.centerx,pipe_rect.centery,pipe,tao_cot)
        if pipe_rect.centerx<=0:
            pipe_rect.centery=random.randint(140,272)
            pipe_rect.centerx=216
        
        up_pipe=pipe_rect.centery-253-80
        drawpipe(pipe_rect.centerx,up_pipe,pygame.transform.flip(pipe,False,True),tao_cot)

    pygame.display.update()
    clock.tick(120)

            