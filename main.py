import pygame
import time


board=[[1,2,3],[4,5,6],[7,8,9]]
pygame.init()
height=810
width=810
i=1
j=1
surface=pygame.display.set_mode((height,width))
white=(255,255,255)
black=(0,0,0)
surface.fill(white)
pygame.display.set_caption("TIC TAC TOE")
for i in range(1,4):
    for j in range(1,4):
        pygame.draw.rect(surface,black,pygame.Rect((i-1)*270,(j-1)*270,i*270,j*270),2)
        pygame.display.flip()
        j+=270
    i+=270
cross=pygame.image.load('images/36-368091_heart-simple-shape-silhouette-tic-tac-toe-cross.png')
cross=pygame.transform.scale(cross,(200,200))
circle=pygame.image.load('images/circle-black-outline-circle-black-outline-frame-vector-107159631.jpg')
circle=pygame.transform.scale(circle,(200,200))
running=True
def conversion(mouseposition):
    xcoordinate=mouseposition[0]//270
    ycoordinate=mouseposition[1]//270
    return(ycoordinate,xcoordinate)
def check(board):
    i=0
    j=0
    count=0
    for i in range(0,3):
        if(board[i][0]==board[i][1]==board[i][2]=='X'):
            print("player 1 won")
            return False
        elif(board[0][i]==board[1][i]==board[2][i]=='X'):
            print("player 1 won")
            return False
        elif(board[i][0]==board[i][1]==board[i][2]=='O'):
            print("player 2 won")
            return False
        elif(board[0][i]==board[1][i]==board[2][i]=='O'):
            print("player 2 won")
            return False
    if(board[0][0]==board[1][1]==board[2][2]=='X'):
        print("player 1 has won")
        return False
    elif(board[0][0]==board[1][1]==board[2][2]=='O'):
        print("player 2 has won")
        return False
    elif(board[2][0]==board[1][1]==board[0][2]=='X'):
        print("player 1 has won")
        return False
    elif(board[2][0]==board[1][1]==board[0][2]=='O'):
        print("player 2 has won")
        return False
    for i in range(0,3):
        for j in range(0,3):
            if(board[i][j] in range(0,11)):
                count=count+1
    if(count==0):
        return False





    

turn=0
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            running=False
        if event.type==pygame.MOUSEBUTTONUP:
            try:
                mouseposition=pygame.mouse.get_pos()
                print(conversion(mouseposition))
                print(mouseposition)
                xposition=(conversion(mouseposition))[0]
                yposition=(conversion(mouseposition))[1]
                print(board[xposition][yposition])
                print(xposition*270,yposition*270)
                if((board[xposition][yposition] in range(0,10))and (turn%2==0)):
                    board[xposition][yposition]='X'
                    print(board)
                    surface.blit(cross,(yposition*270+30,xposition*300+30))
                    turn=turn+1
                    if(check(board)==False):
                        running=False
                        break
                    
                    
                elif((board[xposition][yposition] in range(0,10))and(turn%2!=0)):
                    board[xposition][yposition]='O'
                    surface.blit(circle,(yposition*270+30,xposition*270+30))
                    print(board)
                    turn=turn+1
                    if(check(board)==False):
                        running=False
                        break

            except IndexError:
                pass
    pygame.display.update()           