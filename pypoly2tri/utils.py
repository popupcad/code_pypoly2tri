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

#from enum import Enum
import math

def enum(**enums):
    return type('Enum', (), enums)
    
PI_3div4 = 3*math.pi/4
EPSILON = 1e-12
Orientation = enum(CW=101,CCW=102,COLLINEAR=103)

def Orient2d(pa,pb,pc):
    detleft = (pa.x-pc.x) * (pb.y-pc.y)
    detright = (pa.y-pc.y) * (pb.x-pc.x)
    val = detleft - detright
    
    if val>-EPSILON and val<EPSILON:
        return Orientation.COLLINEAR
    elif val>0:
        return Orientation.CCW

    return Orientation.CW
        
#def InScanArea(pa,pb,pc,pd):
#    pdx = pd.x
#    pdy = pd.y
#    adx = pa.x - pdx
#    ady = pa.y - pdy
#    bdx = pb.x - pdx
#    bdy = pb.y - pdy
#    
#    adxbdy = adx*bdy
#    bdxady = bdx*ady
#    oabd = adxbdy - bdxady
#    if oabd<=EPSILON:
#        return False
#
#    cdx = pc.x - pdx
#    cdy= pc.y - pdy
#    cdxady = cdx*ady
#    adxcdy = adx*cdy
#    ocad = cdxady - adxcdy
#
#    if ocad<=EPSILON:
#        return False
#        
#    return True
    
def InScanArea(pa,pb,pc,pd):
    oadb = (pa.x - pb.x)*(pd.y - pb.y) - (pd.x - pb.x)*(pa.y - pb.y)
    if (oadb >= -EPSILON) :
        return False


    oadc = (pa.x - pc.x)*(pd.y - pc.y) - (pd.x - pc.x)*(pa.y - pc.y)
    if (oadc <= EPSILON) :
        return False
    return True
    