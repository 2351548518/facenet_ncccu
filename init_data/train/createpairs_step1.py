#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 11:29:55 2019
change the name of the image
@author: cong
"""

import os

# import re
imgs_path = 'new_datasets'

if os.path.isdir(imgs_path):
    for s in os.listdir(imgs_path):
        newdir = os.path.join(imgs_path, s)
        # print(newdir)
        filenames = os.listdir(newdir)
        filenames.sort()
        for name in filenames:
            newname = newdir.split('\\')[-1]
            os.rename(newdir + '\\' + name, os.path.join(newdir, newname + '_' + '%04d' % int(filenames.index(name) + 1)) + '.png')
            # print(newname)