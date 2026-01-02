import common as c
import sys

import pygame

# Constants
SCREEN_DIMS = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FRONT_FONT_SIZE = 70
BACK_FONT_SIZE = 45

FONT_NAMES = ["TakaoPMincho"] # Add font names here.

# Functions
def await_event():
  pygame.event.clear()
  pygame.event.wait()
  return pygame.event.poll()

def await_key():
  event = await_event()

  while True:
    if event.type == pygame.TEXTINPUT:
      return event
    else:
      event = await_event()

def draw_surface_at_y(screen, surface, y):
  surface_width = surface.get_width()
  surface_x = (SCREEN_DIMS[0] / 2) - (surface_width / 2)
  screen.blit(surface, (surface_x, y))
  
def draw_card(front, back):
  global SCREEN_DIMS
  global BLACK
  global WHITE
  global front_font
  global back_font

  screen.fill(BLACK)

  if front is not None:
    front_surface = front_font.render(front, True, WHITE)
    draw_surface_at_y(screen, front_surface, 100)

  if back is not None:
    substrings = back.split(";")
    for i in range(0, len(substrings)):
      s = substrings[i]
      back_surface = back_font.render(s, True, WHITE)
      draw_surface_at_y(screen, back_surface, 200 + BACK_FONT_SIZE * i)

  pygame.display.flip()

# Main logic
is_running = True
deck_path = c.get_deck_path()
full_deck = c.read_deck_from_path(deck_path)

pygame.init()
pygame.display.set_caption("kioku")

screen = pygame.display.set_mode(SCREEN_DIMS)

front_font = pygame.font.SysFont(FONT_NAMES, FRONT_FONT_SIZE)
back_font = pygame.font.SysFont(FONT_NAMES, BACK_FONT_SIZE)

while is_running:
  test_deck = c.get_test_cards(full_deck)

  for card in test_deck:
    # Show front.
    draw_card(card["front"], None)
    event = await_key()

    # Show back and process input.
    draw_card(card["front"], card["back"])
    event = await_key()

    match event.text:
      case "y" | "Y":
        card["score"] += 1
      case "n" | "N":
        card["score"] -= 1
      case _: # Leave the game if anything else gets pressed
        is_running = False
        break

  c.reset_cards(full_deck)

c.write_deck_to_path(deck_path, full_deck)
