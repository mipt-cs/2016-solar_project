import pygame
import sys
import random
import threading                        #from threading import Thread, Lock
from time import sleep
from time import time

#import numpy as np

#import file as fl

FPS=120
#h=int(input())
#w=int(input())
h=1920//2
w=1080//2
intXboard=100
intYboard=10
Positions_list=[(i*10**len(str(max(intXboard,intYboard)-1))+j) for i in range(intXboard) for j in range(intYboard)]
#Positions_List=[(i*10**len(str(max(intXboard,intYboard)-1))+j) for i in range(intXboard) for j in range(intYboard)]

#print(Positions_list)
a=2 #для того чтобы влезла всякая хуйня по горизонтали

d=2   
MaxPalubn=4
Dforx0=h/(2*intXboard+a)
D=h//(2*intXboard+a)

y0=(w-intYboard*D)//2
x0=int(a*Dforx0/2)
y1=y0#только для отрисовки интерфейса далее y1=y0 
x1=3*x0+intXboard*D#отступы у карты противника
y2=y0
x2=x0


D1=(w-y1)/(3*(MaxPalubn)-1)
if h/2-2*x0 - MaxPalubn*int(3/2*D1)-4*D1-D1-2*D1>0:correctmasshtab=1
else:
         D1=(h/2-2*x0)/(MaxPalubn*3/2+7)
         y1=2*(w-3*MaxPalubn*D1+D1)//2
print(D1)

SEA=(56,177,194)
FIRE=(123,0,0)
pygame.init()
pygame.display.set_caption('Sea BOY')
screen = pygame.display.set_mode((2*(intXboard*D+2*x0), intYboard*D+2*y0)) 
#r=pygame.Rect(0,0,2*(intXboard*D+2*x1), intYboard*D+2*y1)
#pygame.draw.rect(screen,(56,177,194),r,0)
screen.fill(SEA)

#defs

#For all

def modul(mod):
    if mod>=0: return  mod
    else :     return -mod
    
def sign(sig):#int
    if sig==0: return 0
    else:      return int(sig/modul(sig))


#Specific

def shipplacementcorrectchecker():
    sleep(10)
    if popitshipplacement==0:
        print("Crash")
        shipplacement.stop()
        shipplacement.start()


###Полная расстановка

def shipplacement(Positions_List,deltaX,ShipsPositions): #Positions_List

  global  popitshipplacement #, Positions_list
  for m in range(MaxPalubn-1,-1,-1):
    n=0
    #Spawn (m+1)-x
    while n<=MaxPalubn-1-m:
        position=random.randint(0,len(Positions_list)-1)
    
        x=Positions_list[position]//(10**len(str(max(intXboard,intYboard)-1)))
        y=Positions_list[position]-10**len(str(max(intXboard,intYboard)-1))*x

        #print(x,y)
    
        popit=0
        while popit==0:
            rot1=random.randint(1,4)                     #Change rotation 1-up,2-right,3-down,4-left
            rot2=random.randint(0,1)
            rotY=int((1-(-1)**rot1)*(0.5-rot2))
            rotX=int((1-(-1)**(rot1-1))*(0.5-rot2))
            popit=1
            if 0<=(x+m*rotX)<=intXboard-1 and 0<=(y+m*rotY)<=intYboard-1:

                try:
                    Positions_list.index((x+m*rotX)*(10**len(str(max(intXboard,intYboard)-1)))+(y+m*rotY))
                except ValueError:
                    popit=0
                    #print("исключения есть")
                else:
                    popit=1
                    #print("исключений нет")

            else:
                popit=0
                #print("исключения есть")
    
        twopRect=pygame.Rect(deltaX+D*x-m*((1-rotX)//2)*D,y0+D*y-m*((1-rotY)//2)*D,D+m*D*modul(rotX),D+m*D*modul(rotY))
        pygame.draw.ellipse(screen,(0,0,0),twopRect, width=0)
    
    
  

        Yaround=-1-m*(1-sign(rotY+0.5))//2
        Xaround=-1-m*(1-sign(rotX+0.5))//2

        #print(Xaround,Yaround)


        #print(rotX,rotY)

        Del_list=[-1 for i in range(3*(3+m))]
        i=0
        while Xaround<=1+(1+(m-1)*modul(rotX))*(1+sign(rotX))//2:               #Что удаляем из возможных позиций
                while Yaround<=1+(1+(m-1)*modul(rotY))*(1+sign(rotY))//2 and i<=3*(3+m)-1:
                    print(x+Xaround,y+Yaround)
                    if 0<=x+Xaround<=intXboard-1 and 0<=y+Yaround<=intYboard-1:
                        Del_list[i]=(x+Xaround)*(10**len(str(max(intXboard,intYboard)-1)))+y+Yaround
                        Yaround+=1
                        i+=1
                    else:
                        Del_list[i]=-1
                        Yaround+=1
                        i+=1
                Xaround+=1
                Yaround=-1-m*(1-sign(rotY+0.5))//2

        Yaround=-m*(1-sign(rotY+0.5))//2
        Xaround=-m*(1-sign(rotX+0.5))//2
        i=0
        while Xaround<=(1+(m-1)*modul(rotX))*(1+sign(rotX))//2:               #Что добавляем в позиции вражеских кораблей
                while Yaround<=(1+(m-1)*modul(rotY))*(1+sign(rotY))//2:
                        ShipsPositions[MaxPalubn-1-m][n][i]=(x+Xaround)*(10**len(str(max(intXboard,intYboard)-1)))+y+Yaround
                        Yaround+=1
                        i+=1
                Xaround+=1
                Yaround=-m*(1-sign(rotY+0.5))//2

    
        print(Del_list)
        i=0
        while i<=(len(Del_list)-1):
            if Del_list[i]!=-1:
                try:
                    Positions_list.remove(int(Del_list[i]))
                    i+=1
                except ValueError:i+=1
            else: i+=1
        #print(Positions_list)
        n+=1
  #end of Spawn (m+1)-x
  popitshipplacement=1
  #print(Positions_list)
  #Positions_List[:]=Positions_list
  ShipsPositions[:]=ShipsPositions
  
  
 #"""if PlayersshipplasmentStage==True:
    #  sleep(0.2)
    #  MenuAutoRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-5*D1,2*D1,2*D1)
    #  pygame.draw.rect(screen,(0,0,0),MenuAutoRectSelect, width=2)"""

###Конец полной расстановки


def makeBoards(x0,y0):
    n=0
    while n<=intXboard: #       для игрока
        pygame.draw.line(screen,(0,0,0),(   x0+D*n-d//2,   y0-d//2       ),(   x0+D*n-d//2        ,   y0+intYboard*D-d//2)   ,d)
        n+=1
    n=0
    while n<=intYboard: #       для игрока
        pygame.draw.line(screen,(0,0,0),(   x0-d//2    ,   y0+D*n-d//2   ),(   x0+intXboard*D-d//2,   y0+D*n-d//2)           ,d)
        n+=1


#def TIMERknopka(x,y,h,w):
    #sleep(1)
    #MenuAutoRectSelect=pygame.Rect(x,y,h,w)
    #pygame.draw.rect(screen,(0,0,0),MenuAutoRectSelect, width=2)
                    

#end defs



#4 - 1 3 - 2 2 - 3 1 - 4




#расстановка кораблей игрока

makeBoards(x2,y2)


playerspositions=[[0 for i in range(intYboard)]for i in range(intXboard)]

print(playerspositions)

PlayersShips=[[[0 for j in range(MaxPalubn-i)] for k in range(i+1)] for i in range(MaxPalubn)]
OppShips    =[[[0 for j in range(MaxPalubn-i)] for k in range(i+1)] for i in range(MaxPalubn)]
PlayersshipplasmentStage=True #True ;FALSE ONLY FOR SPEED TEST!!!
PlayersshipplasmentInProcessOne=0
PlayersshipplasmentInProcessTwo=0
rotX=0
rotY=0
TIMER='stop'
TIMER1=0
Palubn=1 #сколькипалубный корабль изначально? 
i=0
CountOstShips=[i for i in range(MaxPalubn,0,-1)]

#Рисуем кнопки
for i in range(MaxPalubn):        
    MenuRect=pygame.Rect(x1,y1//2+int(3*D1*i),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
    pygame.draw.rect(screen,(0,0,0),MenuRect, width=2)
    MenuShipRect=pygame.Rect(x1+D1//4,y1//2+int(3*D1*i)+D1//4,(i+1)*int(3/2*D1),int(3/2*D1))
    pygame.draw.ellipse(screen,(0,0,0),MenuShipRect, width=0)
 
MenuNextRect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-2*D1,2*D1,2*D1)
pygame.draw.rect(screen,(0,0,0),MenuNextRect, width=2)
pygame.draw.polygon(screen,(0,0,0), 
                    [[x1+int(3/2*D1)*MaxPalubn+13*D1//2-D1//4     ,   w-y1//2-  D1         ], 
                     [x1+int(3/2*D1)*MaxPalubn+9*D1//2+D1//4      ,   w-y1//2-2*D1+D1//4   ], 
                     [x1+int(3/2*D1)*MaxPalubn+9*D1//2+D1//4      ,   w-y1//2     -D1//4   ]])

MenuAutoRect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-5*D1,2*D1,2*D1)
pygame.draw.rect(screen,(0,0,0),MenuAutoRect, width=2)

MenuCleanRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-8*D1,2*D1,2*D1)
pygame.draw.rect(screen,(0,0,0),MenuCleanRectSelect, width=2)

MenuRectSelected=pygame.Rect(x1,y1//2+int(3*D1*(Palubn-1)),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
pygame.draw.rect(screen,(255,0,0),MenuRectSelected, width=2)

#перестали рисовать кнопки

#Игрок и его интерфейс во время расстановки
while PlayersshipplasmentStage:
    pygame.time.Clock().tick(FPS)
    pygame.display.update()
    if TIMER=='start':
        TIMER1+=1
        if TIMER1==FPS//10:
            MenuAutoRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-5*D1,2*D1,2*D1)
            pygame.draw.rect(screen,(0,0,0),MenuAutoRectSelect, width=2)
            TIMER1=0
            TIMER='stop'
            if TIMERtype=='Autoshipplacement':
                MenuAutoRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-5*D1,2*D1,2*D1)
                pygame.draw.rect(screen,(0,0,0),MenuAutoRectSelect, width=2)
                TIMER1=0
            elif TIMERtype=='Clean':
                MenuAutoRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-8*D1,2*D1,2*D1)
                pygame.draw.rect(screen,(0,0,0),MenuAutoRectSelect, width=2)
                TIMER1=0
            


    i=0
    for i in range(MaxPalubn):
        MaskRect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+D1-D1//4,y1//2+int(3*D1*i)+D1//4,2*int(3/2*D1),int(3/2*D1))
        pygame.draw.rect(screen,SEA,MaskRect,width=0)
        font = pygame.font.SysFont('comicsansms',int(D1),bold=False, italic=False)
        text = font.render(str(CountOstShips[i]), True, (0,0,0))
        screen.blit(text, (x1+int(3/2*D1)*MaxPalubn+2*D1, y1//2+int(3*D1*i+D1//4)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            #PlayersshipplasmentStage=False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if   x1<=event.pos[0]<=x1+MaxPalubn*int(3/2*D1)+4*D1 and y1//2<=event.pos[1]<=y1//2+int(3*D1*MaxPalubn):           #блок кнопок
                for m in range(MaxPalubn):
                    if   y1//2+int(3*D1*m)<=event.pos[1]<y1//2+int(3*D1*(m+1)-D1):
                        Palubn=m+1
                MenuRectSelected=pygame.Rect(x1,y1//2+int(3*D1*(Palubn-1)),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
                pygame.draw.rect(screen,(255,0,0),MenuRectSelected, width=2)
                for i in range(MaxPalubn):
                    if i!=Palubn-1:
                        MenuRectUnSelected=pygame.Rect(x1,y1//2+int(3*D1*i),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
                        pygame.draw.rect(screen,(0,0,0),MenuRectUnSelected, width=2)
            elif x1+int(3/2*D1)*MaxPalubn+9*D1//2<=event.pos[0]<=x1+int(3/2*D1)*MaxPalubn+9*D1//2+D1*2 and w-y1//2-2*D1<=event.pos[1]<=w-y1//2-2*D1+2*D1:
                if CountOstShips==[0 for i in range(MaxPalubn)]:
                    MenuNextRect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-2*D1,2*D1,2*D1)
                    pygame.draw.rect(screen,(255,0,0),MenuNextRect, width=2)
                    pygame.draw.polygon(screen,(255,0,0),
                                       [[x1+int(3/2*D1)*MaxPalubn+13*D1//2-D1//4     ,   w-y1//2-  D1         ], 
                                        [x1+int(3/2*D1)*MaxPalubn+9*D1//2+D1//4      ,   w-y1//2-2*D1+D1//4   ], 
                                        [x1+int(3/2*D1)*MaxPalubn+9*D1//2+D1//4      ,   w-y1//2     -D1//4   ]])

                    PlayersshipplasmentStage=False
                else:
                    font = pygame.font.SysFont('comicsansms',int(D1),bold=False, italic=False)
                    text = font.render("СНАЧАЛА ВСЕ РАССТАВЬТЕ КОРАБЛИ!!!", True, (0,0,0))
                    screen.blit(text, (x1-D1*10, -y0//4+y0//16-y0//32))
                    #print сначала расставьте все корабли!
            elif x1+int(3/2*D1)*MaxPalubn+9*D1//2<=event.pos[0]<=x1+int(3/2*D1)*MaxPalubn+9*D1//2+2*D1 and w-y1//2-5*D1<=event.pos[1]<=w-y1//2-5*D1+2*D1:
                    #PlayersShips=[[[0 for j in range(MaxPalubn-i)] for k in range(i+1)] for i in range(MaxPalubn)]
                    ZarisRect=pygame.Rect(0,0,x0*2+D*intXboard,w)
                    pygame.draw.rect(screen,SEA,ZarisRect, width=0)
                    makeBoards(x2,y2)
                    MenuAutoRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-5*D1,2*D1,2*D1)
                    pygame.draw.rect(screen,(255,0,0),MenuAutoRectSelect, width=2)
                    shipplacement(Positions_list,x2,PlayersShips)
                    CountOstShips=[0 for i in range(MaxPalubn)]
                    print(PlayersShips)
                    #TIMER=threading.Thread(target=TIMERknopka(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-5*D1,2*D1,2*D1))
                    TIMER='start'
                    TIMERtype='Autoshipplacement'
                    Positions_list=[(i*10**len(str(max(intXboard,intYboard)-1))+j) for i in range(intXboard) for j in range(intYboard)]

            elif x1+int(3/2*D1)*MaxPalubn+9*D1//2<=event.pos[0]<=x1+int(3/2*D1)*MaxPalubn+9*D1//2+2*D1 and w-y1//2-8*D1<=event.pos[1]<=w-y1//2-8*D1+2*D1:
                    #PlayersShips=[[[0 for j in range(MaxPalubn-i)] for k in range(i+1)] for i in range(MaxPalubn)]
                    ZarisRect=pygame.Rect(0,0,x0*2+D*intXboard,w)
                    pygame.draw.rect(screen,SEA,ZarisRect, width=0)
                    makeBoards(x2,y2)
                    MenuCleanRectSelect=pygame.Rect(x1+int(3/2*D1)*MaxPalubn+9*D1//2,w-y1//2-8*D1,2*D1,2*D1)
                    pygame.draw.rect(screen,(255,0,0),MenuCleanRectSelect, width=2)
                    CountOstShips=[i for i in range(MaxPalubn,0,-1)]
                    TIMER='start'
                    TIMERtype='Clean'

            else:
              if CountOstShips[Palubn-1]>0:
                if PlayersshipplasmentInProcessOne==0:
                    if (x2<=event.pos[0]<=h//2) and (y2<=event.pos[1]<=h//2-y2):
                        x=(event.pos[0]-x2)//D
                        y=(event.pos[1]-y2)//D
                        print(x,y)
                        if playerspositions[x][y]==0:#занято ли место?
                            PlayersshipplasmentInProcessOne=1
                            #Playersrect=pygame.Rect(x2+x*D,y2+y*D,D,D)
                            #pygame.draw.ellipse(screen,(255,0,0),Playersrect, width=2)
                            pygame.draw.rect(screen,(255,0,0),(x2+x*D-1,y2+y*D-1,D+1,D+1),d)
                            #playerspositions[x][y]=1#с этих пор место занято

                    
                elif PlayersshipplasmentInProcessTwo==0:
                    if (x2<=event.pos[0]<=h//2) and (y2<=event.pos[1]<=w-y2):
                        xEnd=(event.pos[0]-x2)//D
                        yEnd=(event.pos[1]-y2)//D
                        #print(xEnd,yEnd)
                        if (modul(xEnd-x)>=modul(yEnd-y)) and (x2<=event.pos[0]<=h//2) and (y2<=event.pos[1]<=w-y2):
                            rotX=sign(xEnd-x)
                            rotY=0
                        else:
                            rotY=sign(yEnd-y)
                            rotX=0
                        if 0<=x+(Palubn-1)*rotX<intXboard and (0<=y+(Palubn-1)*rotY<intYboard):
                            if (playerspositions[x+(Palubn-1)*rotX][y+(Palubn-1)*rotY]==0) and ((rotY+rotX+rotX*rotY!=0) or Palubn==1):#занято ли место?
                                PlayersshipplasmentInProcessTwo=1
                                Playersrect=pygame.Rect(x2+(x-modul(rotX)*(Palubn-1)*(1-sign(rotX))//2)*D,y2+(y-modul(rotY)*(Palubn-1)*(1-sign(rotY))//2)*D,D*(1+(Palubn-1)*modul(rotX)),D*(1+(Palubn-1)*modul(rotY)))
                                pygame.draw.rect(screen,(0,0,0),(x2+x*D-1,y2+y*D-1,D+1,D+1),d)
                                pygame.draw.ellipse(screen,(255,0,0),Playersrect,0)
                                PlayersshipplasmentInProcessTwo=0
                                PlayersshipplasmentInProcessOne=0
                                
                            
                                Xdelit=-(1-rotX)//2*(Palubn-1)*modul(rotX)-1
                                Ydelit=-(1-rotY)//2*(Palubn-1)*modul(rotY)-1


                                while Xdelit<=(1+rotX)//2*(Palubn-1)*modul(rotX)+1:
                                    while Ydelit<=(1+rotY)//2*(Palubn-1)*modul(rotY)+1:
                                        if (0<=x+Xdelit<intXboard) and (0<=y+Ydelit<intYboard):
                                            playerspositions[x+Xdelit][y+Ydelit]=1
                                        print(x+Xdelit,y+Ydelit)
                                        Ydelit+=1
                                    Xdelit+=1
                                    Ydelit=-(1-rotY)//2*(Palubn-1)*modul(rotY)-1
                                CountOstShips[Palubn-1]+=-1
                                print(playerspositions)



                                Yaround=-(Palubn-1)*(1-sign(rotY+0.5))//2
                                Xaround=-(Palubn-1)*(1-sign(rotX+0.5))//2

                                i=0
                                while Xaround<=(1+2*modul(rotX))*(1+sign(rotX))//2:               #Что добавляем в позиции  кораблей player's
                                    while Yaround<=(1+2*modul(rotY))*(1+sign(rotY))//2 and i<Palubn:
                                        PlayersShips[MaxPalubn-Palubn][CountOstShips[Palubn-1]][i]=(10**len(str(max(intXboard,intYboard)-1)))*(x+Xaround)+y+Yaround
                                        Yaround+=1
                                        i+=1
                                    Xaround+=1
                                    Yaround=-(Palubn-1)*(1-sign(rotY+0.5))//2

                                print(PlayersShips)

                            else:
                                PlayersshipplasmentInProcessOne=0
                                PlayersshipplasmentInProcessTwo=0
                                pygame.draw.rect(screen,(0,0,0),(x2+x*D-1,y2+y*D-1,D+1,D+1),d)


                        

                  
                    else:
                        PlayersshipplasmentInProcessOne=0
                        pygame.draw.rect(screen,(0,0,0),(x2+x*D-1,y2+y*D-1,D+1,D+1),d)
              else: 
                   if CountOstShips==[0 for i in range(MaxPalubn)]:
                    for i in range(MaxPalubn):
                        MenuRectUnSelected=pygame.Rect(x1,y1//2+int(3*D1*(Palubn-1)),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
                        pygame.draw.rect(screen,(0,255,0),MenuRectUnSelected, width=2)
                   elif Palubn<MaxPalubn:
                      Palubn+=1

                   else: Palubn=1
                   MenuRectSelected=pygame.Rect(x1,y1//2+int(3*D1*(Palubn-1)),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
                   pygame.draw.rect(screen,(255,0,0),MenuRectSelected, width=2)
                   for i in range(MaxPalubn):
                    if i!=Palubn-1:
                        MenuRectUnSelected=pygame.Rect(x1,y1//2+int(3*D1*(Palubn-1)),MaxPalubn*int(3/2*D1)+4*D1,2*D1)
                        pygame.draw.rect(screen,(0,0,0),MenuRectUnSelected, width=2)
            #elif event.button==3:
                #PlayersshipplasmentInProcessOne=0
                #pygame.draw.rect(screen,(0,0,0),(x2+x*D-1,y2+y*D-1,D+1,D+1),d)
            #MenuAutoRectUnSelect=pygame.Rect(x1+17*D//2,y1+int(2*D*3-D/2),2*D,2*D)
            #pygame.draw.rect(screen,(0,0,0),MenuAutoRectUnSelect, width=2)      
                
    pygame.display.flip()
#Игрок и его интерфейс во время расстановки END

#клнец расстановки кораблей игрока
RedrawRect=pygame.Rect(x1-D,0,h+w,h+w)
pygame.draw.rect(screen,SEA,RedrawRect,0)

#расстановка кораблей противника

y1=y0 

#For Computer
makeBoards(x1,y1)


#spccheckerThread=threading.Thread(target=shipplacementcorrectchecker)
shipplacement=threading.Thread(target=shipplacement(Positions_list,x1,OppShips))

#spccheckerThread.start()
shipplacement.start()
sleep(0.1)

print(Positions_list)
print(OppShips)

#Конец расстановки кораблей противника
#for i in range(len(Positions_list)):
    
    #x=Positions_list[i]//10
    #y=Positions_list[i]-10*x

    #FreeRect=pygame.Rect(x1+D*(x),y1+D*(y),D,D)
    #pygame.draw.rect(screen,(55,0,0),FreeRect, width=0)







### GAMESTAGE!!!






GameStage=True
Turn=random.randint(0,1)     # 1- player, 0 - computer
Yestpopadaniye=0
correct=0
#WasatteckfromPlayer  =[[0 for i in range(intYboard)]for i in range(intXboard)]
WasatteckfromPlayer  =[(i*10**len(str(max(intXboard,intYboard)-1))+j) for i in range(intXboard) for j in range(intYboard)]
WasatteckfromComputer=[[0 for i in range(intYboard)]for i in range(intXboard)]
#WasatteckfromComputer=[(i*10**len(str(max(intXboard,intYboard)-1))+j) for i in range(intXboard) for j in range(intYboard)]
#print(PlayersShips)
Positions_list=[(i*10**len(str(max(intXboard,intYboard)-1))+j) for i in range(intXboard) for j in range(intYboard)]

PlayerDefeat=0
ComputerDefeat=0
while GameStage:
    pygame.time.Clock().tick(FPS)
    pygame.display.update()
    pygame.display.flip()
    if PlayerDefeat==-(MaxPalubn**3+3*MaxPalubn**2+2*MaxPalubn)//6:
        GameStage=False
        Turn=1
    elif ComputerDefeat==-(MaxPalubn**3+3*MaxPalubn**2+2*MaxPalubn)//6:
        GameStage=False
        Turn=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if x1<=event.pos[0]<=x1+intXboard*D and y1<=event.pos[1]<=y1+intYboard*D and Turn==1:
                x=(event.pos[0]-x1)//D
                y=(event.pos[1]-y1)//D
                #print(x,y)
                if WasatteckfromComputer[x][y]==0:
                  for i in range(MaxPalubn):
                    for j in range(len(OppShips[i])):
                        for k in range(len(OppShips[i][j])):
                            if OppShips[i][j][k]==x*10**len(str(max(intXboard,intYboard)-1))+y:
                                OppShips[i][j][k]=-1
                                DamageRect=pygame.Rect(x1+D*x,y1+D*y,D,D)
                                pygame.draw.rect(screen,FIRE,DamageRect, width=0)
                                Yestpopadaniye=1
                                Turn=1
                                ComputerDefeat+=-1

                  if Yestpopadaniye==0:
                    NoDamageRect=pygame.Rect(x1+D*x,y1+D*y,D,D)
                    pygame.draw.rect(screen,(255,255,255),NoDamageRect, width=0)
                    Turn=0
                  WasatteckfromComputer[x][y]=1         
                  Yestpopadaniye=0
                  
                #print(PlayersShips)

    Yestpopadaniye=0
    #print(Positions_list)
    while Turn==0:
        sleep(0.1)
        if Yestpopadaniye==0:
            YXAttack=WasatteckfromPlayer[random.randint(0,len(WasatteckfromPlayer)-1)]
            xAttack=YXAttack//(10**len(str(max(intXboard,intYboard)-1)))
            yAttack=YXAttack-xAttack*10**len(str(max(intXboard,intYboard)-1))
            print(YXAttack)
            print(WasatteckfromPlayer)
            xAttack0=xAttack
            yAttack0=yAttack
            print(xAttack0,yAttack0)
            YAttack=yAttack
            XAttack=xAttack
        elif Yestpopadaniye==1 :#and correct==0:
          print(correct)
          rot=[[0,1],[1,0],[0,-1],[-1,0]]
          while correct==0 and len(rot)!=0: #and uncorrect<4:
                rot1=random.randint(0,len(rot)-1)                     #Change rotation 1-up,2-right,3-down,4-left
                #rot2=random.randint(0,1)
                rotX=rot[rot1][0]
                rotY=rot[rot1][1]
                print(rotX,rotY)
                print(xAttack,yAttack)
                sleep(0.5)
                rot.remove(rot[rot1])

                if ((xAttack+rotX)*10**len(str(max(intXboard,intYboard)-1)) + yAttack+rotY) in Positions_list:
                    Positions_list.remove((xAttack+rotX)*10**len(str(max(intXboard,intYboard)-1)) + yAttack+rotY)
                    xAttack=xAttack0+rotX
                    yAttack=yAttack0+rotY
                    correct=1
                    print('NoError')
                    YAttack=yAttack
                    XAttack=xAttack
        elif Yestpopadaniye==2 :#and correct==0:
              rotVN=random.randint(0,1)
              XAttack=int((xAttack0+xAttack)/2+((-xAttack0+xAttack)/2+2)*2*(rotVN-1/2)*modul(rotX))
              YAttack=int((yAttack0+yAttack)/2+((-yAttack0+yAttack)/2+1)*2*(rotVN-1/2)*modul(rotY))
              print('start')
              print(xAttack,yAttack)
              print(xAttack0,yAttack0)
              print(XAttack,YAttack)
              sleep(0.1)
              
        else:
            print('stop')
            #Yestpopadaniye=0
            Turn=1
        for i in range(MaxPalubn):
                    for j in range(len(OppShips[i])):
                        for k in range(len(OppShips[i][j])):
                            if  PlayersShips[i][j][k]==XAttack*10**len(str(max(intXboard,intYboard)-1))+YAttack:
                                print("cokl stert")

                                #print(xAttack*10**len(str(max(intXboard,intYboard)-1))+yAttack)
                                PlayersShips[i][j][k]=-1
                                WasatteckfromComputer
                                DamageRect=pygame.Rect(x2+D*XAttack,y2+D*YAttack,D,D)
                                pygame.draw.rect(screen,FIRE,DamageRect, width=0)
                                Yestpopadaniye+=1
                                print(Yestpopadaniye)
                                Turn=0 
                                PlayerDefeat+=-1
        correct=0
        if Yestpopadaniye==0:
                NoDamageRect=pygame.Rect(x2+D*xAttack,y2+D*yAttack,D,D)
                pygame.draw.rect(screen,(255,255,255),NoDamageRect, width=0)
                Turn=1
        #WasatteckfromPlayer[xAttack][yAttack]=1
        #WasatteckfromPlayer.remove(YXAttack)
            
        #print(WasatteckfromPlayer)
                
                #except ValueError:
                    
FinalStage=True

while FinalStage:
    pygame.time.Clock().tick(FPS)
    pygame.display.update()
    pygame.display.flip()
    screen.fill(SEA)


    if Turn==0:
        font = pygame.font.SysFont('comicsansms',w//8,bold=False, italic=False)
        text = font.render('Выиграл компьютер!', True, (0,0,0))
        screen.blit(text, (h*(1-1/2)//2,w//2-D))

    elif Turn==1:
        font = pygame.font.SysFont('comicsansms',w//8,bold=False, italic=False)
        text = font.render('Выиграл игрок!', True, (0,0,0))
        screen.blit(text, (h*(1-1/3)//2,w//2-D))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #sleep(5)
    #FinalStage=False
