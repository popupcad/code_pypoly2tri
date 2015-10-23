# -*- coding: utf-8 -*-
from distutils.core import setup
from distutils.extension import Extension

#import pypoly2tri
#import os
#basedir = os.path.split(pypoly2tri.__file__)[0]
#import glob
#files = glob.glob(basedir+'/*.py*')
compile_c = True

ext_modules = []
packages = [ 'pypoly2tri']

basedir='python/pypoly2tri'
#ext_modules = cythonize('pypoly2tri/*.pyx'),  # accepts a glob pattern

if compile_c:
    try:
        from Cython.Build import cythonize
        ext_modules.extend(cythonize(Extension('pypoly2tri.advancing_front',[basedir+'/advancing_front.py'])))
        ext_modules.extend(cythonize(Extension('pypoly2tri.cdt',[basedir+'/cdt.py'])))
        ext_modules.extend(cythonize(Extension('pypoly2tri.shapes',[basedir+'/shapes.py'])))
        ext_modules.extend(cythonize(Extension('pypoly2tri.sweep',[basedir+'/sweep.py'])))
        ext_modules.extend(cythonize(Extension('pypoly2tri.sweep_context',[basedir+'/sweep_context.py'])))
        ext_modules.extend(cythonize(Extension('pypoly2tri.utils',[basedir+'/utils.py'])))
    except ImportError:
        ext_modules.append(Extension('pypoly2tri.advancing_front',[basedir+'/advancing_front.c']))
        ext_modules.append(Extension('pypoly2tri.cdt',[basedir+'/cdt.c']))
        ext_modules.append(Extension('pypoly2tri.shapes',[basedir+'/shapes.c']))
        ext_modules.append(Extension('pypoly2tri.sweep',[basedir+'/sweep.c']))
        ext_modules.append(Extension('pypoly2tri.sweep_context',[basedir+'/sweep_context.c']))
        ext_modules.append(Extension('pypoly2tri.utils',[basedir+'/utils.c']))

setup(
    name = 'pypoly2tri',
    version='0.0.1',
    classifiers=['Programming Language :: Python','Programming Language :: Python :: 3'],      
    description='pyPoly2Tri: a pure python implementation of poly2tri',
    author='Dan Aukes',
    author_email='danaukes@danaukes.com',
    url='http://github.com/popupcad/pypoly2tri',
    ext_modules = ext_modules,
    packages = packages,
    package_dir={'pypoly2tri' : 'python/pypoly2tri'})