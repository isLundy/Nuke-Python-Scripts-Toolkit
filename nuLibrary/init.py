#"""
# ==============================================================================
# nuLibrary v9.6.3, built October 18 2022.

# Author: Lundy Hu

# Email: lundyhu@outlook.com

# See the https://github.com/isLundy/Nuke-PythonScripts-Toolkit for details.
# ==============================================================================
#"""

import nuke
import os

# Only add directories of all folders in the current directory. Faster than os.walk().
top = os.path.dirname(os.path.abspath(__file__))
for dirname in sorted(os.listdir(top)):
    dirpath = os.path.join(top, dirname)
    if os.path.isdir(dirpath):
        nuke.pluginAddPath(dirpath.replace('\\', '/'))