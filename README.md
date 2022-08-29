# <p align='center'>nuke-PythonScripts-Toolkit</p>
## Install
###### （若熟悉安装可略过）
1. 将 `nuLibrary` 文件夹复制到 `.nuke` 文件夹内
2. 若 `.nuke` 文件夹内没有 `init.py` 文件，则创建一个`init.txt`文件，并将以下代码复制到文件内。
      ```python
      import nuke

      nuke.pluginAddPath('./nuLibrary')
      ```
      然后将 `init.txt` 更改为 `init.py`
## Introduce
