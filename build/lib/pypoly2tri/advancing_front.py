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
class Node(object):
    def __init__(self,p,t=None):
        self.point =p
        self.triangle = t
        self.value = p.x
        self.next = None
        self.prev = None
        
class AdvancingFront(object):
    def __init__(self,head,tail):
        self.head_ = head
        self.tail_ = tail
        self.search_node_ = head
    
    def LocateNode(self,x):
        node = self.search_node_
        
        if x < node.value:
            dummy = node.prev
            while (dummy != None):
                node = dummy
                if x>= node.value:
                    self.search_node_=node
                    return node
#                node = node.prev
                dummy = node.prev

        else:
            dummy = node.next            
            while (dummy != None):
                node = dummy
                if x < node.value:
                    self.search_node_=node.prev
                    return node.prev
                dummy = node.next            

        return None
    def FindSearchNode(self,x):
        return self.search_node_
        
    def LocatePoint(self,point):
        px = point.x
        node = self.FindSearchNode(px)
        nx = node.point.x
        
        if px==nx:
            if point!=node.point:
                if point == node.prev.point:
                    node = node.prev
                elif point ==node.next.point:
                    node = node.next
                else:
                    assert(0)
        elif px<nx:
            dummy = node.prev
            while(dummy!=None):
                node = dummy
                if point==node.point:
                    break
                dummy = node.prev

        else:
            dummy = node.next
            while(dummy!=None):
                node = dummy
                if point==node.point:
                    break
                dummy = node.next
            
        if node!=None:
            self.search_node_=node
        return node
        
    def head(self):
        return self.head_

    def set_head(self,node):
        self.head_ = node

    def tail(self):
        return self.tail_

    def set_tail(self,node):
        self.tail_ = node

    def search(self):
        return self.search_node_

    def set_search(self,node):
        self.search_node_ = node
        