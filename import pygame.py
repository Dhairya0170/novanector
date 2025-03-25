import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set display size
WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (213, 50, 80)
BLUE = (50, 153, 213)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock
clock = pygame.time.Clock()
SNAKE_SPEED = 15

# Font
font = pygame.font.SysFont("bahnschrift", 20)

def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])

def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    x_change, y_change = 0, 0
    
    snake_body = []
    length_of_snake = 1

    food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
    food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

    while not game_over:
        while game_close:
            screen.fill(WHITE)
            message = font.render("Game Over! Press C-Continue or Q-Quit", True, RED)
            screen.blit(message, [WIDTH // 6, HEIGHT // 3])
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change, y_change = -BLOCK_SIZE, 0
                elif event.key == pygame.K_RIGHT:
                    x_change, y_change = BLOCK_SIZE, 0
                elif event.key == pygame.K_UP:
                    x_change, y_change = 0, -BLOCK_SIZE
                elif event.key == pygame.K_DOWN:
                    x_change, y_change = 0, BLOCK_SIZE
        
        x += x_change
        y += y_change
        
        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True
        
        screen.fill(BLUE)
        pygame.draw.rect(screen, RED, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])
        
        snake_body.append([x, y])
        if len(snake_body) > length_of_snake:
            del snake_body[0]
        
        for block in snake_body[:-1]:
            if block == [x, y]:
                game_close = True
        
        draw_snake(snake_body)
        pygame.display.update()
        
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            food_y = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
            length_of_snake += 1
        
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()
    quit()

game_loop()