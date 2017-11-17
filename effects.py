#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from pygame.gfxdraw import bezier
from math import sin, pi


def flash(surface, _):
    surface.fill((255, 255, 255))


def wave(surface, pos):
    surface.fill((0, 0, 0))
    width, height = surface.get_size()
    w = width // 20
    color = (int(max(0.0, sin(pos*2*pi))*255),
             int(max(0.0, sin(pos*2*pi+pi*2/3))*255),
             int(max(0.0, sin(pos*2*pi+pi*4/3))*255))
    for i in range(w):
        bezier(surface, [
            (int(pos * width), height // 2 + i),
            (int(pos * width + width / 2), i),
            (int(pos * width + width / 2), height + i),
            (int(pos * width + width), height // 2 + i)
        ], 16, color)
        bezier(surface, [
            (int(pos * width - width), height // 2 + i),
            (int(pos * width - width / 2), i),
            (int(pos * width - width / 2), height + i),
            (int(pos * width), height // 2 + i)
        ], 16, color)