import pygame
from pygame.locals import *
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game constants
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SPEED_X = 3
BALL_SPEED_Y = 3
PADDLE_SPEED = 5

# Create the Ball class
class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.rect = pygame.Rect(WIDTH // 2 - self.radius, HEIGHT // 2 - self.radius, self.radius * 2, self.radius * 2)
        self.speed_x = BALL_SPEED_X * random.choice((1, -1))
        self.speed_y = BALL_SPEED_Y * random.choice((1, -1))

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self):
        self.speed_x *= -1

    def reset(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed_x = BALL_SPEED_X * random.choice((1, -1))
        self.speed_y = BALL_SPEED_Y * random.choice((1, -1))

# Create the Paddle class
class Paddle:
    def __init__(self, x):
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.rect = pygame.Rect(x, HEIGHT // 2 - self.height // 2, self.width, self.height)
        self.speed = PADDLE_SPEED

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def check_collision(self, ball):
        return self.rect.colliderect(ball.rect)

    def check_bounds(self):
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Create the Game class
class Game:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0
        self.font = pygame.font.Font(None, 36)
        self.ball = Ball()
        self.player_paddle = Paddle(0)
        self.opponent_paddle = Paddle(WIDTH - PADDLE_WIDTH)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

        keys = pygame.key.get_pressed()
        if keys[K_UP] and self.player_paddle.rect.top > 0:
            self.player_paddle.move_up()
        if keys[K_DOWN] and self.player_paddle.rect.bottom < HEIGHT:
            self.player_paddle.move_down()

    def update(self):
        self.ball.move()

        # Ball collision with paddles
        if self.player_paddle.check_collision(self.ball) or self.opponent_paddle.check_collision(self.ball):
            self.ball.bounce()

        # Ball collision with walls
        if self.ball.rect.top < 0 or self.ball.rect.bottom > HEIGHT:
            self.ball.speed_y *= -1

        # Paddle collision with walls
        self.player_paddle.check_bounds()
        self.opponent_paddle.check_bounds()

        # Ball out of bounds
        if self.ball.rect.left < 0:
            self.opponent_score += 1
            self.ball.reset()
        if self.ball.rect.right > WIDTH:
            self.player_score += 1
            self.ball.reset()

        # AI opponent
        if self.opponent_paddle.rect.centery < self.ball.rect.y:
            self.opponent_paddle.move_down()
        if self.opponent_paddle.rect.centery > self.ball.rect.y:
            self.opponent_paddle.move_up()

    def draw(self):
        WIN.fill(BLACK)
        pygame.draw.rect(WIN, WHITE, self.player_paddle.rect)
        pygame.draw.rect(WIN, WHITE, self.opponent_paddle.rect)
        pygame.draw.ellipse(WIN, WHITE, self.ball.rect)
        score_text = self.font.render(f"{self.player_score} : {self.opponent_score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH // 2, 30))
        WIN.blit(score_text, score_rect)
        pygame.display.flip()

    def run(self):
        clock = pygame.time.Clock()
        while True:
            self.handle_events()
            self.update()
            self.draw()
            clock.tick(60)

# Run the game
if __name__ == '__main__':
    game = Game()
    game.run()
