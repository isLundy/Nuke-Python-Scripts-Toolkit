#"""
# ==============================================================================
# nuLibrary v9.6.2, built September 6 2022.

# Author: Lundy Hu

# Email: lundyhu@outlook.com

# See the https://github.com/isLundy/Nuke-PythonScripts-Toolkit for details.
# ==============================================================================
#"""

import nuke
import os
import re

'''
From the current directory to the third-level directory, only add the third-level directory
'''
top = os.path.dirname(os.path.abspath(__file__))
for root, dirs, files in os.walk(top):
    if re.split(r'[\\/]', root)[-3] == os.path.basename(top):
        nuke.pluginAddPath(root.replace('\\', '/'))