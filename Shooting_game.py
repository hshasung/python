import pygame
import sys
pygame.init()

#######
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
yellow = (255,255,0)
blue = (0,0,255)
pink = (255,133,215)
orange = (240,155,89)
brown = (78,43,15)
green = (55,126,71)
#######






w=480
h=640

pad=pygame.display.set_mode((w,h)) #화면생성
pygame.display.set_caption("Shooting Game") #제목설정

pad.fill((200,250,200))


'''
pygame.draw.line(pad,red,(240,0),(240,640),5)#선그리기
pygame.draw.line(pad,red,(0,210),(480,210),5)#선그리기
pygame.draw.circle(pad,blue,(120,100),50,0)#원그리기
pygame.draw.circle(pad,blue,(360,100),50,0)#원그리기
pygame.draw.rect(pad,black,(70,400,340,200),0)#사각형그리기
pygame.draw.polygon(pad,pink,((200,100),(230,200),(270,200),(250,90)))
'''
pygame.draw.circle(pad,white,(240,320),200,0)
pygame.draw.polygon(pad,orange,((220,300),(220,340),(350,340)))
pygame.draw.circle(pad,black,(140,280),30,0)
pygame.draw.circle(pad,black,(320,280),30,0)
pygame.draw.rect(pad,black,(90,400,300,5),0)
pygame.draw.rect(pad,red,(70,450,340,100),0)
pygame.draw.rect(pad,green,(100,450,50,100),0)
pygame.draw.rect(pad,green,(200,450,50,100),0)
pygame.draw.rect(pad,green,(300,450,50,100),0)





pygame.display.update() #화면 업데이트

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()




























































