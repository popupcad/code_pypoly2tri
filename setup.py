# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:04:03 2013

@author: danaukes
"""

from distutils.core import setup

packages = []
packages.append('pypoly2tri')

package_data = {}
package_data['pypoly2tri'] = ['data/*']

setup(name='pypoly2tri',
      version='0.1',
      classifiers=['Programming Language :: Python','Programming Language :: Python :: 3'],      
      description='pyPoly2Tri: a pure python implementation of poly2tri',
      author='Daniel M. Aukes',
      author_email='danaukes@seas.harvard.edu',
      url='http://www.popupcad.com',
      packages=packages,
      package_data = package_data
     )