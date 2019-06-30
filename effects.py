#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division, print_function, unicode_literals
from pygame.gfxdraw import bezier
from math import sin, cos, pi
from animations import snow, horizontal_line, vertical_line, double_wave, single_circle
from moods import Mood


def flash(surface, _):
    surface.fill((255, 255, 255))


def wave(surface, pos, color_pos):
    width, height = surface.get_size()
    w = width // 40
    color = (int(max(0.0, sin(color_pos*2*pi))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*2/3))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*4/3))*255))
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


def snowflakes(surface, pos):
    snow(surface, pos, Mood((255, 255, 255), (220, 220, 220)), seed=2)

def horizontal_line_effect(surface, pos):
    horizontal_line(surface, pos, Mood((255, 255, 255), (220, 220, 220)))

def vertical_line_effect(surface, pos, color_pos):
    color = (int(max(0.0, sin(color_pos*2*pi))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*2/3))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*4/3))*255))
    vertical_line(surface, pos, Mood(color, (220, 220, 220)))

def double_wave_effect(surface, pos, color_pos):
    width, height = surface.get_size()
    w = width // 40
    color = (int(max(0.0, sin(color_pos*2*pi))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*2/3))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*4/3))*255))
    color2= (int(max(0.0, cos(pos*2*pi))*255),
             int(max(0.0, cos(pos*2*pi+pi*2/3))*255),
             int(max(0.0, cos(pos*2*pi+pi*4/3))*255))
    double_wave(surface, pos, Mood(color, color2))

def single_circle_effect(surface, pos, color_pos):
    color = (int(max(0.0, sin(color_pos*2*pi))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*2/3))*255),
             int(max(0.0, sin(color_pos*2*pi+pi*4/3))*255))
    single_circle(surface, pos, Mood(color, color))
