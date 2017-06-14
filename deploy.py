# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:43:25 2017

@author: daukes
"""

import os
import shutil

try:
    shutil.rmtree('build')
except FileNotFoundError:
    pass

try:
    shutil.rmtree('dist')
except FileNotFoundError:
    pass

try:
    shutil.rmtree('pypoly2tri.egg-info')
except FileNotFoundError:
    pass
    