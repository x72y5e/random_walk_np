import pygame
import numpy as np
import time


DIMS = (512, 512)


def f(A: np.ndarray) -> np.ndarray:
    x, y = np.where(A == 255.)
    x, y = x[0], y[0]
    A /= 1.2
    A[A < 1] = 0.
    neighbours = [(min(A.shape[0] - 1, max(0, x + i)),
                   min(A.shape[1] - 1, max(0, y + j)))
                  for i in (-1, 0, 1) for j in (-1, 0, 1)]
    blank = [(x, y) for (x, y) in neighbours
             if A[x, y] == 0.]
    blank = neighbours if not blank else blank
    A[blank[np.random.choice(len(blank))]] = 255.
    return A


def run():

    pygame.init()

    small_dims = (DIMS[0] // 4, DIMS[1] // 4)
    display = pygame.display.set_mode(DIMS)
    clock = pygame.time.Clock()
    done = False

    grid = np.zeros(small_dims)
    grid[np.random.randint(small_dims[0]), np.random.randint(small_dims[1])] = 255.

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        grid = f(grid)
        surf = pygame.surfarray.make_surface(grid.T)
        display_surf = pygame.transform.scale(surf, DIMS)
        display.blit(display_surf, (0, 0))

        pygame.display.update()

        clock.tick(20)


if __name__ == '__main__':
    run()
