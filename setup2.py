# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 09:04:03 2013

@author: danaukes
"""

#from distutils.core import setup
#
packages = []
packages.append('popupcad')
packages.append('popupcad.algorithms')
packages.append('popupcad.constraints')
packages.append('popupcad.convert')
packages.append('popupcad.filetypes')
packages.append('popupcad.geometry')
packages.append('popupcad.graphics2d')
packages.append('popupcad.graphics3d')
packages.append('popupcad.manufacturing')
packages.append('popupcad.materials')
packages.append('popupcad.supportfiles')
packages.append('popupcad.widgets')
     
import sys
from cx_Freeze import setup, Executable

toinclude = []
toinclude.append(('C:/Python27/Lib/site-packages/geos_c.dll','geos_c.dll'))
#toinclude.append(('C:/Python27/Lib/site-packages/OpenGL/DLLS/gle32.dll','gle32.dll'))
#toinclude.append(('C:/Python27/Lib/site-packages/OpenGL/DLLS/glut32.dll','glut32.dll'))

import glob, os
explore_dirs = [
    'C:/Users/danaukes/Documents/code projects/popupcad/popupcad/supportfiles/',
    'C:/Users/danb0b/Documents/code projects/popupCAD/popupcad/supportfiles/',
]

shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "DTI Playlist",           # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]playlist.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]
msi_data = {}
    
files = []
for d in explore_dirs:
    files.extend( glob.glob( os.path.join(d,'*') ) )
    
zipinclude = []
for f in files:
#    print f
    toinclude.append( (f, os.path.join('supportfiles',os.path.basename(f) ) ))

build_exe_options = {"include_msvcr":True,"include_files":toinclude,"zip_includes": zipinclude,'packages':["scipy.integrate.vode","scipy.integrate.lsoda","scipy.sparse.csgraph._validation","OpenGL.platform.win32","matplotlib.backends"]}
bdist_msi_options = {
    'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
    'add_to_path': False,
#    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (company_name, product_name),
#    'data': msi_data    
    }
    
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "popupCAD",
        version = "0.1",
        description = "popupCAD Editor",
        executables = [Executable("popupcad.py", base=base)],
        options={'build_exe': build_exe_options,'bdist_msi': bdist_msi_options}
          )     