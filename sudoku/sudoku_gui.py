import pygame
import sys

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# increase for faster solving
FPS = 6

# hardest sodoku (increase FPS to > 200 or it takes forever)
# or just comment out "clock.tick(FPS)"
# board = [
#     [8,0,0,0,0,0,0,0,0],
#     [0,0,3,6,0,0,0,0,0],
#     [0,7,0,0,9,0,2,0,0],
#     [0,5,0,0,0,7,0,0,0],
#     [0,0,0,0,4,5,7,0,0],
#     [0,0,0,1,0,0,0,3,0],
#     [0,0,1,0,0,0,0,6,8],
#     [0,0,8,5,0,0,0,1,0],
#     [0,9,0,0,0,0,4,0,0]
# ]
# easy sudoku (choose FPS as low as you want)
board= [
    [0,0,1,5,0,9,4,0,2],
    [0,9,0,1,0,4,5,0,0],
    [3,5,0,0,0,8,0,9,0],
    [0,8,3,2,5,1,0,7,0],
    [0,2,9,7,0,0,3,4,0],
    [5,0,0,9,0,0,0,0,8],
    [0,0,0,0,6,0,0,5,0],
    [0,0,0,0,9,0,2,0,6],
    [0,4,2,8,0,0,0,0,7]
]

pygame.font.init()
myfont = pygame.font.SysFont('Arial', 50)
clock = pygame.time.Clock()

# used to get the next empty field of sudoku
def getNextEmpty(b):
    for rowi in range(len(b)):
        for coli in range(len(b[rowi])):
            if b[rowi][coli] == 0:
                return (rowi, coli)
    return False

# is the planned move valid?
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

# draw and update the pygame sudoku board
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

# actual solving function that is called recursively
def solve(b):
    # PYGAME STUFF
    clock.tick(FPS)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)
    draw_board(b)

    # SOLVING
    #get next empty space or done if none
    nextEmpty = getNextEmpty(b)
    if not nextEmpty:
        return True
    #try 0 to 9, if valid, enter it
    for num in range(1,10):
        if isValidMove(b, nextEmpty, num):
            b[nextEmpty[0]][nextEmpty[1]] = num
            #recursive call (try advancing with set number)
            if solve(b):
                return True
            #if cant be solved, set changed pos back to 0
            b[nextEmpty[0]][nextEmpty[1]] = 0

if __name__ == "__main__":
    solve(board)
    # this is only used to keep the window open when solving finishes
    while True:
        clock.tick(1)
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(1)