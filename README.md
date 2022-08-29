<h1 align="center"> 
      <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
      <br> PythonScripts Toolkit for Nuke</br>
</h1>

## Perface
当你看到这个页面时就说明你可以访问GitHub了（这是废话）,

## Install  
> 若熟悉安装可略过
1. 将 `nuLibrary` 文件夹复制到 `.nuke` 文件夹内
2. - 若 `.nuke` 文件夹内没有 `init.py` 文件，则创建一个`init.txt`文件，并将以下代码复制到文件中。
      ```python
      import nuke

      nuke.pluginAddPath('./nuLibrary')
      ```
      最后将 `init.txt` 更改为 `init.py`
      
    - 若 `.nuke` 文件夹内存在 `init.py` 文件，打开 `init.py` （右键用记事本方式打开或用你会的一种方式打开。若都不会，请将电脑关鸡！），
      将下面一行代码复制到文件中（总之，缺少哪行代码就复制哪行）。
      ```python
      nuke.pluginAddPath('./nuLibrary')
      ``` 
想要深入了解插件安装？请查看官方指导 [Installing Plug-ins](https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html#installingplugins-ref-label)
## Introduce
