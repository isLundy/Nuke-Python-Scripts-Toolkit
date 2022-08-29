<h1 align="center"> 
      <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
      <br> PythonScripts Toolkit for Nuke
</h1>

## Perface

> 当你看到这个页面时说明你可以访问GitHub（很显然你看到了一句废话）, 若会科学上网请使用代理访问:rocket:（无需多言），若不会可略过。

我个人平时制作了一个名为 `nuLibrary` 的工具， nuLibrary 内含有 `Gizmos`， `PthonScripts`， `Series` 三个不同的工具包，大部分的 gizmo 和 script 来自于网络，少部分为自己编写。在这里只公开发布 `PythonScripts`， Gizmo 和 Series 暂不公开，其中一部分原因是与 `NukeSurvivalToolkit` 中的内容大致相同，其表面的最大区别是在 Nuke 中的布局不一样。

在 PythonScripts 中整合了我在 Nuke 中所使用的一些较为`实用`, `高效`, 且`优雅`的 Scripts（或者称之为插件）,并在 Nuke 中做了布局。

如若感兴趣建议尽可能地熟悉 `W_hotbox` 插件。`快速`，`高度自定义化`，`可以减少很多快捷键的占用`。若对Python有了解的话，犹如锦上添花。

## Download

> 若熟悉GitHub可略过

举例：

点击右侧的 `Releases` > `latest` 会进入到以下页面

点击 `Assets` 下的第一个就可以了。

## Install

> 若熟悉安装可略过

1. 将 `nuLibrary` 文件夹复制到用户目录的 `.nuke` 文件夹内
2. - 若 `.nuke` 文件夹内没有 `init.py` 文件，则创建一个`init.txt`文件，并将以下代码复制到文件中， 最后将 `init.txt` 更改为 `init.py`
   - 若 `.nuke` 文件夹内存在 `init.py` 文件，打开 `init.py` （右键用记事本方式打开或用你会的一种方式打开。若不会打开，请将电脑关鸡，鸡你太美！:bomb::boom:），
      并将以下代码复制到文件中。
      ```python
      import nuke

      nuke.pluginAddPath('./nuLibrary')
      ```

> 想要深入了解 nuke 插件安装？请查看官方指导 [Installing Plug-ins](https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html#installingplugins-ref-label)

## Introduce

完成安装后可以看到位于 Nuke 顶部菜单栏右侧的 `PythonScripts`。
<br>
<br>
#### **W_hotbox**

W_hotbox 没有显示在以下布局中，显示在 Nuke 菜单的 Edit 下和 Preferences 面板中。

作者：Wouter Gilsing

介绍及使用方法： [http://www.nukepedia.com/python/ui/w_hotbox](http://www.nukepedia.com/python/ui/w_hotbox)
<br>
<br>
**Import_Export**
- CollectFiles

**Misc**
- Default
- winExploreDir

**NodeGraph**
- AlignNodes
- MultiChannelSplit
- V_Tools
- W_scaleTree
- W_smartAlign

**UI**
- Channel_Hotbox
- CloseAllProperties
- SearchReplacePanel
- W_hotbox

**zLundy**
- openPresetFolder
