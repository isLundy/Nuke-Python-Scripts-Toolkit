'''
# Author: Lundy Hu
# Email: lundyhu@outlook.com
# See the https://github.com/isLundy/Nuke-PythonScripts-Toolkit for details.
'''
import nuke
from pathlib import Path

for dirs in sorted(Path(__file__).absolute().parent.iterdir()):
    if dirs.is_dir():
        for dirs_2 in sorted(dirs.iterdir()):
            if dirs_2.is_dir():
                nuke.pluginAddPath(dirs_2.as_posix())