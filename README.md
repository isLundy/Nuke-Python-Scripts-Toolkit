# <p align='center'>PythonScripts Toolkit</p>
## Install 
1. 将 `nuLibrary` 文件夹复制到 `.nuke` 文件夹内
2. 若 `.nuke` 文件夹内没有 `init.py` 文件，则创建一个`init.txt`文件，并将以下代码复制到文件中。
      ```python
      import nuke

      nuke.pluginAddPath('./nuLibrary')
      ```
      最后将 `init.txt` 更改为 `init.py`
      
      若 .nuke 文件夹内存在 init.py 文件，打开init.py（右键用记事本方式打开或用你会的一种方式打开。若都不会，请将电脑关鸡！），
      将下面一行代码复制到文件中。
      ```python
      nuke.pluginAddPath('./nuLibrary')
      ``` 
      
## Introduce
