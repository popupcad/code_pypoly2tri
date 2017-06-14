# -*- coding: utf-8 -*-
'''
Written by Daniel M. Aukes and CONTRIBUTORS
Email: danaukes<at>asu.edu.
Please see LICENSE for full license.
'''

from setuptools import setup
from setuptools.extension import Extension
import sys

#import pypoly2tri
#import os
#basedir = os.path.split(pypoly2tri.__file__)[0]
#import glob
#files = glob.glob(basedir+'/*.py*')
compile_c = False

packages = [ 'pypoly2tri']

package_data = {}
package_data['pypoly2tri'] = ['licenses/poly2tri/LICENSE']

setup_kwargs = {}
setup_kwargs['name']='pypoly2tri'
setup_kwargs['version']='0.0.3'
setup_kwargs['classifiers']=['Programming Language :: Python','Programming Language :: Python :: 3']   
setup_kwargs['description']='pyPoly2Tri: a pure python implementation of poly2tri'
setup_kwargs['author']='Dan Aukes'
setup_kwargs['author_email']='danaukes@danaukes.com'
setup_kwargs['url']='http://github.com/popupcad/pypoly2tri'
setup_kwargs['license']='MIT'
setup_kwargs['packages']=packages
setup_kwargs['package_dir']={'pypoly2tri' : 'python/pypoly2tri'}
setup_kwargs['package_data'] = package_data

if compile_c:

    ext_modules = []
    
    basedir='python/pypoly2tri'
    #ext_modules = cythonize('pypoly2tri/*.pyx'),  # accepts a glob pattern
    
    
#    with open('test.txt','w') as f:
#        f.writelines(sys.argv)
    
    try:
        from Cython.Distutils import build_ext
#        from Cython.Build import cythonize
        ext_modules.append(Extension('pypoly2tri.advancing_front',[basedir+'/advancing_front.py']))
        ext_modules.append(Extension('pypoly2tri.cdt',[basedir+'/cdt.py']))
        ext_modules.append(Extension('pypoly2tri.shapes',[basedir+'/shapes.py']))
        ext_modules.append(Extension('pypoly2tri.sweep',[basedir+'/sweep.py']))
        ext_modules.append(Extension('pypoly2tri.sweep_context',[basedir+'/sweep_context.py']))
        ext_modules.append(Extension('pypoly2tri.utils',[basedir+'/utils.py']))
        setup_kwargs['cmdclass'] = {'build_ext':build_ext}
    except ImportError:
        ext_modules.append(Extension('pypoly2tri.advancing_front',[basedir+'/advancing_front.c']))
        ext_modules.append(Extension('pypoly2tri.cdt',[basedir+'/cdt.c']))
        ext_modules.append(Extension('pypoly2tri.shapes',[basedir+'/shapes.c']))
        ext_modules.append(Extension('pypoly2tri.sweep',[basedir+'/sweep.c']))
        ext_modules.append(Extension('pypoly2tri.sweep_context',[basedir+'/sweep_context.c']))
        ext_modules.append(Extension('pypoly2tri.utils',[basedir+'/utils.c']))
    
    setup_kwargs['ext_modules'] = ext_modules
    setup(**setup_kwargs)
    
else:

#    import pypoly2tri
    
#    package_data = {}
#    package_data['popupcad'] = ['supportfiles/*','supportfiles/icons/*']
    
    setup(**setup_kwargs)
