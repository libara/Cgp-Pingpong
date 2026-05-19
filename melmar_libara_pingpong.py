import pygame
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Pro Game")

# Colors (hindi black background)
BG_COLOR = (30, 144, 255)  # blue
WHITE = (255, 255, 255)
RED = (255, 80, 80)
GREEN = (80, 255, 120)

# Paddles
paddle_width = 12
paddle_height = 90

left_paddle = pygame.Rect(30, HEIGHT//2 - 45, paddle_width, paddle_height)
right_paddle = pygame.Rect(WIDTH - 42, HEIGHT//2 - 45, paddle_width, paddle_height)

# Ball
ball = pygame.Rect(WIDTH//2 - 10, HEIGHT//2 - 10, 20, 20)
ball_speed_x = 4
ball_speed_y = 4

# Scores
left_score = 0
right_score = 0
font = pygame.font.SysFont("Arial", 40)

clock = pygame.time.Clock()

def reset_ball():
    ball.center = (WIDTH//2, HEIGHT//2)
    return 4, 4

running = True
while running:
    clock.tick(60)
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Controls (2 Player)
    keys = pygame.key.get_pressed()

    # Left player (W/S)
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 6
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += 6

    # Right player (Up/Down)
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 6
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += 6

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Top/bottom bounce
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Paddle collision
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1
        ball_speed_x *= 1.1
        ball_speed_y *= 1.1

    # Score system
    if ball.left <= 0:
        right_score += 1
        ball_speed_x, ball_speed_y = reset_ball()

    if ball.right >= WIDTH:
        left_score += 1
        ball_speed_x, ball_speed_y = reset_ball()

    # Speed increase over time
    ball_speed_x *= 1.0005
    ball_speed_y *= 1.0005

    # Draw objects
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, RED, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Score text
    score_text = font.render(f"{left_score} : {right_score}", True, GREEN)
    screen.blit(score_text, (WIDTH//2 - 60, 20))

    # GAME OVER (score limit 5)
    if left_score == 5 or right_score == 5:
        winner = "LEFT PLAYER WINS!" if left_score == 5 else "RIGHT PLAYER WINS!"
        screen.fill((20, 20, 60))
        end_text = font.render("GAME OVER", True, RED)
        win_text = font.render(winner, True, WHITE)
        screen.blit(end_text, (WIDTH//2 - 100, HEIGHT//2 - 50))
        screen.blit(win_text, (WIDTH//2 - 200, HEIGHT//2 + 10))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

    pygame.display.update()