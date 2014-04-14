# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 09:56:07 2014

@author: danaukes
"""
import PySide.QtCore as qc
import PySide.QtGui as qg
import sys

filename = u'C:/Users/danaukes/Documents/code projects/popupcad/popupcad/designs/recursefail.shape'
from popupcad.geometry.genericpolygon import GenericPolygon
from popupcad.widgets.propertyeditor import PropertyEditor

gp = GenericPolygon.load_yaml(filename)
cdt = gp.toCDT3()
cdt.Triangulate()
print 'Exterior:'
for point1,point2 in gp.exteriorpoints():
    print point1,point2
print ''

print 'Interiors:'
for interior in gp.interiorpoints():
    for point1,point2 in interior:
        print point1,point2 
    print ''

app = qg.QApplication(sys.argv)

pv = PropertyEditor(cdt)

pv.show()
sys.exit(app.exec_())    