'''
# Author: Lundy Hu
# Email: lundyhu@outlook.com
# URL: https://github.com/isLundy/Nuke-Python-Scripts-Toolkit.git
'''

from pathlib import Path
import nuke

for dirs in sorted(Path(__file__).absolute().parent.iterdir()):
    if dirs.is_dir():
        nuke.pluginAddPath(dirs.as_posix())