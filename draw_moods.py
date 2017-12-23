#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 16:53:39 2017

@author: dweber
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import moods

factor = 1/255
moods = [moods.gray,moods.fire,moods.water,moods.green,moods.yellow,moods.pink,moods.red,moods.bluered,moods.yellowpink,moods.brown,moods.cyan]
space = 0.2
height = 1
plot_margin = 5

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect="equal")

for i in range(0, len(moods)):
    offset = i*(space+1)
    ax1.add_patch(patches.Rectangle((offset,0), .5, height, facecolor=[b*factor for b in moods[i].primary_color] ))
    ax1.add_patch(patches.Rectangle((offset+.5,0), .5, height, facecolor=[b*factor for b in moods[i].secondary_color] ))
    ax1.add_patch(patches.Rectangle((offset,0), 1, height, fill=False, edgecolor=(0,0,0), linewidth=.5 ))
    
plt.axis([-plot_margin, offset+1+plot_margin,-plot_margin, height+plot_margin])
plt.axis('off')
plt.savefig("colorspec.png", dpi=300, bbox_inches='tight')
