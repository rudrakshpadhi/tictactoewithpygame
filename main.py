import pygame

board=[[1,2,3],[4,5,6],[7,8,9]]
pygame.init()
height=810
width=810
i=1
j=1
surface=pygame.display.set_mode((height,width))
color=(255,255,255)
pygame.display.set_caption("TIC TAC TOE")
for i in range(1,4):
    for j in range(1,4):
        pygame.draw.rect(surface,color,pygame.Rect((i-1)*270,(j-1)*270,i*270,j*270),2)
        pygame.display.flip()
        j+=270
    i+=270
cross=pygame.image.load('images/36-368091_heart-simple-shape-silhouette-tic-tac-toe-cross.png')
cross=pygame.transform.scale(cross,(200,200))
running=True
def conversion(mouseposition):
    xcoordinate=mouseposition[0]//270
    ycoordinate=mouseposition[1]//270
    return(ycoordinate,xcoordinate)




    

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
                if((board[xposition][yposition] in range(0,10))and (turn%2==0)):
                    board[xposition][yposition]='X'
                    print(board)
                    surface.blit(cross,(xposition*270,yposition*270))
                    turn=turn+1
                    
                elif((board[xposition][yposition] in range(0,10))and(turn%2!=0)):
                    board[xposition][yposition]='O'
                    surface.blit(cross,(xposition*270,yposition*270))
                    print(board)

            except IndexError:
                pass
