import nuke
import os
import re

'''
From the current directory to the third-level directory, only add the third-level directory
'''
top = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(top):
    if os.path.basename(top) in re.split(r'[\\/]', root)[-3]:
        nuke.pluginAddPath(root.replace('\\', '/'))