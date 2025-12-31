import common as c
import sys

import pygame

# Constants
SCREEN_DIMS = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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
      print(event)

def draw_card(front, back):
  global SCREEN_DIMS
  global BLACK
  global WHITE
  global front_font
  global back_font

  screen.fill(BLACK)

  print(front)
  print(back)

  if front is not None:
    front_surface = front_font.render(front, True, WHITE)
    screen.blit(front_surface, (50, 100))

  if back is not None:
    back_surface = back_font.render(back, True, WHITE)
    screen.blit(back_surface, (50, 200))

  pygame.display.flip()

# Main logic
is_running = True
deck_path = c.get_deck_path()
full_deck = c.read_deck_from_path(deck_path)

pygame.init()
pygame.display.set_caption("kioku")

screen = pygame.display.set_mode(SCREEN_DIMS)

front_font = pygame.font.SysFont(FONT_NAMES, 70)
back_font = pygame.font.SysFont(FONT_NAMES, 45)

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
