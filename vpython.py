# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:34:11 2016

@author: Tim
"""

import vpython

##########################################
# Create Wall(s)
##########################################
wallR = box(pos=vector(6,0,0), length=0.2, height=4, width=4, color = color.white)

##########################################
# Create Ball(s)
##########################################
ball = sphere(pos=vector(-5,0,0), radius=1.0, color=color.red)
