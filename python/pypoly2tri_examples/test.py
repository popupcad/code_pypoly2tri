# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 21:03:06 2019

@author: danaukes
"""

from pypoly2tri.cdt import CDT
from pypoly2tri.shapes import Point
import numpy
import matplotlib.pyplot as plt
#import shapely.geometry as sg
#
#circle = sg.Point(0,0).buffer(1,resolution=3)
#square = sg.box(-.5,-.5,.5,.5)
#geom = circle.difference(square)
#ext = list(geom.exterior.coords)[:-1]
#ints = [list(item.coords)[:-1] for item in geom.interiors]

ext = [(1.0, 0.0),
 (0.8660254037844389, -0.49999999999999956),
 (0.5000000000000009, -0.8660254037844382),
 (1.3934999695075554e-15, -1.0),
 (-0.4999999999999983, -0.8660254037844397),
 (-0.8660254037844374, -0.5000000000000022),
 (-1.0, -3.2310891488651735e-15),
 (-0.8660254037844406, 0.49999999999999667),
 (-0.5000000000000034, 0.8660254037844366),
 (-4.624589118372729e-15, 1.0),
 (0.49999999999999545, 0.8660254037844413),
 (0.8660254037844357, 0.5000000000000051)]

ints =  [[(0.5, -0.5), (0.5, 0.5), (-0.5, 0.5), (-0.5, -0.5)]]

ext2 = [Point(*item) for item in ext]
ints2=[[Point(*item) for item in loop] for loop in ints]

cdt = CDT(ext2)
for loop in ints2:
    cdt.AddHole(loop)   
cdt.Triangulate()

points = cdt.GetPoints()

tris = cdt.GetTriangles()
tris2 = numpy.array([item.toList() for item in tris])

plt.figure()
for tri in tris2:
    area = tri[(0,1,2,0),:]
    plt.fill(area[:,0],area[:,1])