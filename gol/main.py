import pygame
import random
from enum import IntEnum

# Constants
BOARD_DIMS = (40, 40)
CELL_WIDTH = 20
SCREEN_DIMS = (BOARD_DIMS[0] * CELL_WIDTH, BOARD_DIMS[1] * CELL_WIDTH)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

FPS = 10

CURSOR_DELAY = 30

class CELL(IntEnum):
  EMPTY = 0,
  ALIVE = 1,
  NEXT  = 2

class Cursor:
  def __init__(self, x, y, delay):
    self.x = x
    self.y = y
    self.delay = delay

def get_color_for_cell(val):
  match val & CELL.ALIVE:
    case CELL.EMPTY:
      return BLACK
    case CELL.ALIVE:
      return WHITE

def get_board():
  board = []
  for r in range(0, BOARD_DIMS[1]):
    row = []
    for c in range(0, BOARD_DIMS[0]):
      row.append(CELL.EMPTY)
    board.append(row)
  return board

def draw_board():
  global screen
  global board

  for r in range(0, BOARD_DIMS[1]):
    for c in range(0, BOARD_DIMS[0]):
      color = get_color_for_cell(board[r][c])

      pos_x = c * CELL_WIDTH
      pos_y = r * CELL_WIDTH

      rect_dims = (pos_x, pos_y, CELL_WIDTH, CELL_WIDTH)

      pygame.draw.rect(screen, color, rect_dims)

def randomize_board():
  global board

  for r in range(0, BOARD_DIMS[1]):
    for c in range(0, BOARD_DIMS[0]):
      n = random.randint(1, 100)

      if n < 50:
        board[r][c] = CELL.EMPTY
      else:
        board[r][c] = CELL.ALIVE

def update_single_cell(r, c):
  global board

  is_left  = c == 0
  is_right = c == (BOARD_DIMS[0] - 1)

  is_top    = r == 0
  is_bottom = r == (BOARD_DIMS[1] - 1)

  count = 0

  # For reference:
  # 123
  # 4p5
  # 678
  # Check top row.
  if not is_left and not is_top:
    count += board[r-1][c-1] & CELL.ALIVE
  if not is_top:
    count += board[r-1][c] & CELL.ALIVE
  if not is_right and not is_top:
    count += board[r-1][c+1] & CELL.ALIVE

  # Check current row.
  if not is_left:
    count += board[r][c-1] & CELL.ALIVE
  if not is_right:
    count += board[r][c+1] & CELL.ALIVE

  # Check bottom row.
  if not is_left and not is_bottom:
    count += board[r+1][c-1] & CELL.ALIVE
  if not is_bottom:
    count += board[r+1][c] & CELL.ALIVE
  if not is_right and not is_bottom:
    count += board[r+1][c+1] & CELL.ALIVE

  # Figure out what to do for the current cell.
  val = board[r][c]

  if val == CELL.EMPTY:
    if count == 3:
      board[r][c] = val | CELL.NEXT
  elif val == CELL.ALIVE:
    if count == 2 or count == 3:
      board[r][c] = val | CELL.NEXT

def update_cells():
  for r in range(0, BOARD_DIMS[1]):
    for c in range(0, BOARD_DIMS[0]):
      update_single_cell(r, c)

def advance_cells():
  global board

  for r in range(0, BOARD_DIMS[1]):
    for c in range(0, BOARD_DIMS[0]):
      board[r][c] = (board[r][c] >> 1)

# Init
pygame.init()
pygame.display.set_caption("Game of Life")

board = get_board()
randomize_board()
screen = pygame.display.set_mode(SCREEN_DIMS)

clock = pygame.time.Clock()

is_stopped = False
must_randomize = False
must_empty = False
must_toggle_cell = False
running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(BLACK)

  update_cells()
  advance_cells()
  draw_board()
  pygame.display.flip()
  clock.tick(FPS)

pygame.quit()
