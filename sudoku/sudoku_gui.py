import pygame

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

BOARD = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]
]

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)

def getNextEmpty(b):
    for rowi in range(len(b)):
        for coli in range(len(b[rowi])):
            if b[rowi][coli] == 0:
                return (rowi, coli)
    return False

def isValidMove(b, pos, num):
    #check row
    for coli in range(len(b[pos[0]])):
        if b[pos[0]][coli] == num:
            return False
    #check col
    for rowi in range(len(b[pos[0]])):
        if b[rowi][pos[1]] == num:
            return False
    #check field
    v_field = pos[0] // 3
    h_field = pos[1] // 3
    for rowi in range(3):
        for coli in range(3):
            if b[rowi+v_field*3][coli+h_field*3] == num:
                return False
    return True

def draw_board(b):
    WIN.fill(BLACK)
    for i in range(9):
        for j in range(9):
            left = 100*j
            top = 100*i
            width = 96
            height = 96
            if j % 3 == 0:
                left += 4
                width -= 4
            if j % 3 == 2:
                width -= 4
            if i % 3 == 0:
                top += 4
                height -= 4
            if i % 3 == 2:
                height -= 4
            pygame.draw.rect(WIN, WHITE, pygame.Rect(left, top, width, height))
            text = myfont.render(str(b[i][j]), False, BLACK)
            WIN.blit(text, (left+35, top+18))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_board(BOARD)
    pygame.quit()

if __name__ == "__main__":
    main()