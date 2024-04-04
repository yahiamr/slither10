import pygame
import random
from enum import Enum 
from collections import namedtuple

# Initialize Pygame library
pygame.init()
# Setting up a font for displaying score
font = pygame.font.Font('Arial.ttf',25)

# Enumeration for the snake's direction
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# Namedtuple for easier point (x, y coordinates) management
Point = namedtuple('point','x,y')

# Color definitions for use in UI elements
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0,0,0)

# Game constants
BLOCK_SIZE = 20  # Size of the snake's segment and food
SPEED = 15       # Game speed

# Main game class
class Slither10_game:

    def __init__(self,w=640,h=480):
        self.w = w  # Width of the game window
        self.h = h  # Height of the game window
        # Initialize game window
        self.display = pygame.display.set_mode((self.w,self.h))
        pygame.display.set_caption('Slither10')
        self.clock = pygame.time.Clock()  # Game clock for controlling game speed
        
        # Initial game state
        self.direction =  Direction.RIGHT  # Starting direction
        # Initial position of the snake
        self.head = Point(self.w/2,self.h/2)
        self.snake = [self.head,  # Snake is a list of points
                      Point(self.head.x-BLOCK_SIZE,self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE),self.head.y)]
        self.score = 0  # Starting score
        self.food = None  # Initial food position
        self._place_food()  # Place the first food

    # Method for placing food at a random position
    def _place_food(self):
        x = random.randint(0,(self.w-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        y = random.randint(0,(self.h-BLOCK_SIZE)//BLOCK_SIZE)*BLOCK_SIZE
        self.food = Point(x,y)
        # Ensure food is not placed where the snake currently is
        if self.food in self.snake:
            self._place_food()

    # Main game loop step
    def play_step(self):
        # 1. Process user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Check for window close
                pygame.quit()
                quit()
            # Change direction based on key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

        # 2. Move the snake in the current direction
        self._move(self.direction)  # Move the snake's head
        self.snake.insert(0, self.head)  # Add new head position to the snake

        # 3. Check for collisions (with boundaries or itself)
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score  # Game over condition

        # 4. Check if the snake has eaten food
        if self.head == self.food:
            self.score += 1  # Increase score
            self._place_food()  # Place new food
        else:
            self.snake.pop()  # Remove last segment if no food eaten

        # 5. Update the UI
        self._update_ui()
        self.clock.tick(SPEED)  # Control game speed

        # 6. Return game over status and score
        return game_over, self.score

    # Method to update the game display
    def _update_ui(self):
        self.display.fill(BLACK)  # Clear the display

        # Draw the snake
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))

        # Draw the food
        pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        # Display the score
        text = font.render("Score: "+str(self.score), True, WHITE)
        self.display.blit(text, [0,0]) pygame.display.flip()  # Update the full display# Method to move the snake based on direction
def _move(self, direction):
    x, y = self.head.x, self.head.y
    if direction == Direction.RIGHT:
        x += BLOCK_SIZE
    elif direction == Direction.LEFT:
        x -= BLOCK_SIZE
    elif direction == Direction.DOWN:
        y += BLOCK_SIZE
    elif direction == Direction.UP:
        y -= BLOCK_SIZE
    self.head = Point(x, y)

# Check for collision with boundaries or itself
def _is_collision(self):
    # Check boundary collision
    if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
        return True
    # Check self collision
    if self.head in self.snake[1:]:
        return True   
    return False
if name == 'main': game = Slither10_game()# Main game loop
while True:
    game_over, score = game.play_step()

    if game_over:
        break  # Exit loop if game over

print('Final score', score)
pygame.quit()  # Quit Pygame
