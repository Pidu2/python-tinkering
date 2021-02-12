import pygame

WIDTH, HEIGHT = 900, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sudoku Solver")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 60

def draw_board():
    WIN.fill(BLACK)
    for i in range(9):
        for j in range(9):
            left = 100*i
            top = 100*j
            width = 96
            height = 96
            if i % 3 == 0:
                left += 4
                width -= 4
            if i % 3 == 2:
                width -= 4
            if j % 3 == 0:
                top += 4
                height -= 4
            if j % 3 == 2:
                height -= 4
            pygame.draw.rect(WIN, WHITE, pygame.Rect(left, top, width, height))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_board()
    pygame.quit()

if __name__ == "__main__":
    main()