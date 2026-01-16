import pygame
import numpy as np

# Constants
WIDTH = 640
HEIGHT = 480
SCREEN_DIMS = (WIDTH, HEIGHT)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DBLUE = (0, 0, 100)

# Functions
def make_vec(x, y, z):
  return np.array([[x],[y],[z],[1]])

def make_iden_mat():
  return np.array(
    [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]])

def make_trans_mat(tx, ty, tz):
  return np.array(
    [[1, 0, 0, tx],
     [0, 1, 0, ty],
     [0, 0, 1, tz],
     [0, 0, 0,  1]])

def make_scale_mat(kx, ky, kz):
  return np.array(
    [[kx,  0,  0, 0],
     [ 0, ky,  0, 0],
     [ 0,  0, kz, 0],
     [ 0,  0,  0, 1]])

def get_rad(deg):
  return (deg / 360) * 2 * np.pi

def make_rota_x_mat(deg):
  a = get_rad(deg)

  return np.array(
    [[1,         0,          0, 0],
     [0, np.cos(a), -np.sin(a), 0],
     [0, np.sin(a),  np.cos(a), 0],
     [0,         0,          0, 1]])

def make_rota_y_mat(deg):
  a = get_rad(deg)

  return np.array(
    [[ np.cos(a), 0,  np.sin(a), 0],
     [         0, 1,          0, 0],
     [-np.sin(a), 0,  np.cos(a), 0],
     [         0, 0,          0, 1]])

def make_rota_z_mat(deg):
  a = get_rad(deg)

  return np.array(
    [[np.cos(a), -np.sin(a), 0, 0],
     [np.sin(a),  np.cos(a), 0, 0],
     [        0,          0, 1, 0],
     [        0,          0, 0, 1]])

def make_cube_arr():
  return [
    make_vec( 1.0,  1.0, 1.0),
    make_vec(-1.0,  1.0, 1.0),
    make_vec(-1.0, -1.0, 1.0),
    make_vec( 1.0, -1.0, 1.0),

    make_vec( 1.0,  1.0, -1.0),
    make_vec(-1.0,  1.0, -1.0),
    make_vec(-1.0, -1.0, -1.0),
    make_vec( 1.0, -1.0, -1.0)]

def mult_mat_arr(mat_arr):
  acc = make_iden_mat()
  for i in range(0, len(mat_arr)):
    acc = acc @ mat_arr[i]
  return acc

def draw_line_from_cube(cube_arr, mat, ia, ib):
  va = cube_arr[ia]
  vb = cube_arr[ib]

  pa = mat @ va
  pb = mat @ vb

  # TODO: apply perspective

  pygame.draw.line(screen, WHITE, (pa[0][0], pa[1][0]), (pb[0][0], pb[1][0]), 1)

def draw_cube(cube_arr, mat):
  # Front face
  draw_line_from_cube(cube_arr, mat, 0, 1)
  draw_line_from_cube(cube_arr, mat, 1, 2)
  draw_line_from_cube(cube_arr, mat, 2, 3)
  draw_line_from_cube(cube_arr, mat, 3, 0)

  # Back face
  draw_line_from_cube(cube_arr, mat, 4, 5)
  draw_line_from_cube(cube_arr, mat, 5, 6)
  draw_line_from_cube(cube_arr, mat, 6, 7)
  draw_line_from_cube(cube_arr, mat, 7, 4)

  # Connecting lines
  draw_line_from_cube(cube_arr, mat, 0, 4)
  draw_line_from_cube(cube_arr, mat, 1, 5)
  draw_line_from_cube(cube_arr, mat, 2, 6)
  draw_line_from_cube(cube_arr, mat, 3, 7)

def draw_stuff():
  cube_arr = make_cube_arr()

  total_mat = mult_mat_arr([
    make_trans_mat(WIDTH/2, HEIGHT/2, 0),
    make_scale_mat(WIDTH/4, WIDTH/4, 1),
    make_rota_z_mat(rota_angle),
    make_rota_x_mat(30),
    make_rota_y_mat(30)
  ])

  draw_cube(cube_arr, total_mat)

# Init
pygame.init()
pygame.display.set_caption("vectors")

screen = pygame.display.set_mode(SCREEN_DIMS)
#screen = pygame.display.set_mode(SCREEN_DIMS, pygame.FULLSCREEN)

clock = pygame.time.Clock()

rota_angle = 0

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
  screen.fill(DBLUE)
  draw_stuff()
  pygame.display.flip()
  clock.tick(24)
  rota_angle += 1
pygame.quit()
