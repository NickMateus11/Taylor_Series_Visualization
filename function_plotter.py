import pygame

import time
import numpy as np


BLACK       = pygame.Color(0, 0, 0)
WHITE       = pygame.Color(255, 255, 255)
GREY        = pygame.Color(100, 100, 100)
LIGHTGREY   = pygame.Color(70, 70, 70)

w, h = (800, 800)


def draw_grid(surface):
    linewidth = 1
    color = LIGHTGREY
    grid_spacing = int((min(w,h)/2) / 10)

    gridlines = []
    for x in range(0,w,grid_spacing):
        pygame.draw.line(surface, color, (x,0), (x,h), linewidth)
    for y in range(0,h,grid_spacing):
        pygame.draw.line(surface, color, (0,y),(w,y), linewidth)
    
    pygame.draw.line(surface, GREY, (w/2,0), (w/2,h), linewidth*3)
    pygame.draw.line(surface, GREY, (0,h/2), (w,h/2), linewidth*3)

def plot(screen, func, time_range, x_lim=10, y_lim=10):
    x_scale_factor = min(w,h)/(2*x_lim)
    y_scale_factor = min(w,h)/(2*y_lim)

    L = np.diff(time_range)
    N = min(w,h)*10
    t = (np.array([t for t in range(0,N)]) * L/N) + time_range[0]

    f = func(t)

    # scaled and adjust to screen coords
    t = (t*x_scale_factor) + w//2
    f = (f*y_scale_factor) + h//2

    pygame.draw.lines(screen, WHITE, False, list(zip(t,f)), 2)


def main():
    pygame.init()
    screen = pygame.display.set_mode([w, h])

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        draw_grid(screen)

        f = lambda t: np.sin(t) + 1/2 * np.cos(2*t + np.pi/4)
        t_range = [-np.pi, np.pi]
        plot(screen, func=f, time_range=t_range, x_lim=5, y_lim=2)

        pygame.display.flip()


if __name__ == '__main__':
    main()
