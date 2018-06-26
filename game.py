import numpy as np
import msvcrt
import os


def insert_random_2or4(grid):
    p = (grid.flat == 0)
    if p.any():
        i = np.random.choice(np.arange(grid.size), p=p/np.sum(p))
        grid.flat[i] = np.random.choice([2, 4], p=[0.9, 0.1])
        return True


def shift_left(grid):
    new = np.zeros_like(grid)
    for j, row in enumerate(grid):
        cpr = list(np.extract(row > 0, row))
        for i in range(row.size):
            if cpr:
                new[j, i] = cpr.pop(0)
                if cpr and new[j, i] == cpr[0]:
                    new[j, i] += cpr.pop(0)
    return new


dirs = {b'K': lambda g: shift_left(g),  # left
        b'M': lambda g: np.fliplr(shift_left(np.fliplr(g))),  # right
        b'H': lambda g: shift_left(g.T).T,  # up
        b'P': lambda g: np.fliplr(shift_left(np.fliplr(g.T))).T}  # down

grid = np.zeros((4, 4), dtype=int)
while insert_random_2or4(grid):  # main loop
    os.system('cls')
    print(grid)
    while "Ignore invalid moves":
        c1, c2 = msvcrt.getch(), msvcrt.getch()  # arrow keys ('\xe0', 'K/M/H/P')
        if c1 == b'\xe0' and c2 in dirs:
            new = dirs[c2](grid)
            if (new != grid).any():
                grid = new
                break
