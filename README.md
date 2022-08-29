<h1 align="center"> 
      <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
      <br> PythonScripts Toolkit for Nuke</br>
</h1>

## Perface
当你看到这个页面时说明你可以访问GitHub（废话）, 若会科学上网请使用代理访问:rocket:（无需多言），若不会可略过。

## Install  
> 若熟悉安装可略过
1. 将 `nuLibrary` 文件夹复制到用户目录的 `.nuke` 文件夹内
2. - 若 `.nuke` 文件夹内没有 `init.py` 文件，则创建一个`init.txt`文件，并将以下代码复制到文件中。
      ```python
      import nuke

      nuke.pluginAddPath('./nuLibrary')
      ```
      最后将 `init.txt` 更改为 `init.py`
      
    - 若 `.nuke` 文件夹内存在 `init.py` 文件，打开 `init.py` （右键用记事本方式打开或用你会的一种方式打开。若都不会，请将电脑关鸡！:bomb::boom:），
      将下面一行代码复制到文件中（总之，缺少哪行代码就复制哪行）。
      ```python
      nuke.pluginAddPath('./nuLibrary')
      ``` 
想要深入了解插件安装？请查看官方指导 [Installing Plug-ins](https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html#installingplugins-ref-label)

## Introduce
我个人平时制作了一个名为 `nuLibrary` 的工具， nuLibrary 内含有 `Gizmos`， `PthonScripts`， `Series` 三个不同的工具包，大部分的 gizmo 和 script 来自于网络，少部分为自己编写。在这里只公开发布 `PythonScripts`， Gizmo 和 Series 暂不公开，其中一部分原因是与 `NukeSurvivalToolkit` 中的内容大致相同，其表面的最大的区别是在 Nuke 中的布局不一样。

NukeSurvivalToolkit 的 GitHub 地址 [Here](https://github.com/CreativeLyons/NukeSurvivalToolkit_publicRelease.git)。

在 PythonScripts 中整合了我在 Nuke 中一些较为`实用`, `高效`, 且`优雅`的 Scripts,并在 Nuke 中做了布局。

如若感兴趣建议尽可能地熟悉 `W_Hotbox` 插件。`快速`，`高度自定义化`，`可以减少很多快捷键的占用`。
