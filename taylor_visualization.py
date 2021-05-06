import pygame
import time
import numpy as np

import function_plotter as fp
import taylor_series_expansion as ts

BLACK       = pygame.Color(0, 0, 0)
WHITE       = pygame.Color(255, 255, 255)
GREY        = pygame.Color(100, 100, 100)
LIGHTGREY   = pygame.Color(70, 70, 70)
LIGHTBLUE   = pygame.Color(0, 0, 127)
LIGHTRED   = pygame.Color(127, 0, 0)

w, h = (800, 800)

def main():
    pygame.init()
    screen = pygame.display.set_mode([w, h])

    fps = 1

    xlim = 10
    ylim = 2

    centered = 0
    func = lambda t: np.sinc(t)
    f,t = fp.plot_points(func, (-xlim,xlim))
    taylor = ts.Taylor_Series(f,t,centered)

    plotter = fp.Plotter(screen, xlim, ylim)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        fp.draw_grid(screen)

        plotter.plot(f, t, color=LIGHTBLUE, width=4)
        taylor.add_next_term()
        plotter.plot(taylor.get_series(), t, color=LIGHTRED)

        pygame.display.flip()
        time.sleep(1/fps)


if __name__ == '__main__':
    main()