'''
# Author: Lundy Hu
# Email: lundyhu@outlook.com
# See the https://github.com/isLundy/Nuke-PythonScripts-Toolkit for details.
'''

from pathlib import Path
import nuke

for dirs in sorted(Path(__file__).absolute().parent.iterdir()):
    if dirs.is_dir():
        nuke.pluginAddPath(dirs.as_posix())