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

def plot(screen, f, t, xlim=10, ylim=10, color=WHITE, width=2):
    x_scale_factor = min(w,h)/(2*xlim)
    y_scale_factor = min(w,h)/(2*ylim)
    
    t = np.array(t)
    f = np.array(f)

    # scaled and adjust to screen coords
    t_adjusted = (t*x_scale_factor) + w//2
    f_adjusted = (-f*y_scale_factor) + h//2

    pygame.draw.lines(screen, color, False, list(zip(t_adjusted,f_adjusted)), width)


def plot_points(func, time_range):
    L = np.diff(time_range)
    N = int(L*10)
    t = (np.array([t for t in range(0,N)]) * L/N) + time_range[0]
    f = func(t)

    return f,t


class Plotter():
    def __init__(self, screen, xlim, ylim):
        self.screen = screen
        self.xlim = xlim
        self.ylim = ylim

    def plot(self, f, t, color=WHITE, width=2):
        plot(self.screen,f,t,self.xlim,self.ylim,color,width)


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

        func = lambda t: np.sin(t) + 1/2 * np.cos(2*t + np.pi/4)
        t_range = [-np.pi, np.pi]
        f,t = plot_points(func,t_range)
        plot(screen, f, t, xlim=5, ylim=2)

        pygame.display.flip()


if __name__ == '__main__':
    main()
