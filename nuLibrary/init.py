import nuke
import os

# Only add directories of all folders in the current directory. Faster than os.walk().
top = os.path.dirname(os.path.abspath(__file__))
for dirname in sorted(os.listdir(top)):
    dirpath = os.path.join(top, dirname)
    if os.path.isdir(dirpath):
        nuke.pluginAddPath(dirpath.replace('\\', '/'))