import pygame

# Constants
SCREEN_DIMS = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Init
pygame.init()
pygame.display.set_caption("template")

screen = pygame.display.set_mode(SCREEN_DIMS)
#screen = pygame.display.set_mode(SCREEN_DIMS, pygame.FULLSCREEN)

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(BLACK)

  pygame.draw.line(screen, WHITE, (0, 0), SCREEN_DIMS, 1)

  pygame.display.flip()

pygame.quit()
