# -*- coding: utf-8 -*-
'''
Poly2Tri Copyright (c) 2009-2010, Poly2Tri Contributors
http://code.google.com/p/poly2tri/

All rights reserved.
Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice,
  this list of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Poly2Tri nor the names of its contributors may be
  used to endorse or promote products derived from this software without specific
  prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''

from .shapes import Point, Edge, Triangle
from .advancing_front import AdvancingFront,Node


class Basin(object):
    def __init__(self):
        self.left_node = None
        self.bottom_node = None
        self.right_node = None
        self.width = 0.0
        self.left_highest=False
    def Clear(self):
        self.left_node = None
        self.bottom_node = None
        self.right_node = None
        self.width = 0.0
        self.left_highest=False
        

class EdgeEvent(object):
    def __init__(self):
        self.constrained_edge=None
        self.right=False
        
class SweepContext(object):
    def __init__(self,polyline):
        self.basin = Basin()
        self.edge_event = EdgeEvent()
        self.edge_list = []
        
        self.points_ = polyline
        self.triangles_ = []
        self.map_ = []
        self.kAlpha = .3
        
        self.InitEdges(self.points_)
        
        self.front_ = None
        self.head_ = None
        self.tail_ = None
        self.af_head_ = None
        self.af_middle_ = None
        self.af_tail_ = None
        
    def AddHole(self,polyline):
        self.InitEdges(polyline)
        self.points_.extend(polyline)
    def AddPoint(self,point):
        self.points_.pushback(point)
    def GetTriangles(self):
        return self.triangles_
    def GetMap(self):
        return self.map_
    def InitTriangulation(self):
        import numpy
        xs = numpy.array([item.x for item in self.points_])
        ys = numpy.array([item.y for item in self.points_])
        xmin = xs.min()
        xmax = xs.max()
        ymin = ys.min()
        ymax = ys.max()
        
        dx = self.kAlpha * (xmax - xmin)
        dy = self.kAlpha * (ymax - ymin)
        self.head_ = Point(xmax+dx,ymin-dy)
        self.tail_ = Point(xmin-dx,ymin-dy)
        
        from operator import attrgetter
        self.points_ = sorted(self.points_,key = attrgetter('y','x'))
#        self.points_.reverse()        

    def InitEdges(self,polyline):
        self.edge_list.extend([Edge(line1,line2) for line1,line2 in zip(polyline,polyline[1:]+polyline[:1])])
    def GetPoint(self,index):
        return self.points_[index]
    def AddToMap(self,triangle):
        self.map_.append(triangle)
    def LocateNode(self,point):
        return self.front_.LocateNode(point.x)
    def CreateAdvancingFront(self,nodes):
        triangle = Triangle(self.points_[0],self.tail_,self.head_)
        self.map_.append(triangle)
        
        self.af_head_ = Node(triangle.GetPoint(1),triangle)
        self.af_middle_ = Node(triangle.GetPoint(0),triangle)
        self.af_tail_ = Node(triangle.GetPoint(2))
        self.front_ = AdvancingFront(self.af_head_,self.af_tail_)
        
        self.af_head_.next = self.af_middle_
        self.af_middle_.next = self.af_tail_
        self.af_middle_.prev = self.af_head_
        self.af_tail_.prev= self.af_middle_
    def RemoveNode(self,node):
        del node
    def MapTriangleToNodes(self,t):
        for i in range(3):
            if not t.GetNeighbor(i):
                n=self.front_.LocatePoint(t.PointCW(t.GetPoint(i)))
                if n!=None:
                    n.triangle = t
    def RemoveFromMap(self,triangle):
        self.map_.remove(triangle)
    def MeshClean(self,triangle):
#        if triangle!=None and not triangle.IsInterior():
#            triangle.IsInterior(True)
#            self.triangles_.append(triangle)
#            for i in range(3):
#                if not triangle.constrained_edge[i]:
#                    self.MeshClean(triangle.GetNeighbor(i))
        triangles = []
        triangles.append(triangle)
        while len(triangles)>0:
            t = triangles.pop()
        
            if (t != None) and not(t.IsInterior()):
                t.IsInterior(True)
                self.triangles_.append(t)
                for i in range(3):
                    if t.constrained_edge[i]!=None:
                        triangles.append(t.GetNeighbor(i))
        
    def front(self):
        return self.front_
    def point_count(self):
        return len(self.points_)
    def set_head(self,p1):
        self.head_ = p1
    def head(self):
        return self.head_
    def set_tail(self,p1):
        self.tail_ = p1
    def tail(self):
        return self.tail_