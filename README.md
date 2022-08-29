<h1 align="center"> 
      <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png">
      <br> PythonScripts Toolkit for Nuke
</h1>

<br />

## Perface :books:

> 当你看到这个页面时说明你可以访问GitHub（很显然你看到了一句废话）, 若会科学上网请使用代理访问 :rocket:（无需多言），若不会可略过。

我（yes, it's me. Lundy Hu）个人平时整合并制作了一个名为 `nuLibrary` :toolbox: 的工具库， nuLibrary 内含有 `Gizmos` :hammer_and_wrench:， `PthonScripts` :hammer_and_wrench:， `Series` :hammer_and_wrench: 三个不同的工具包，里面含有我平时搜集并使用的 gizmo 和 script，大部分来自于网络，少部分为自己编写。

在这里只公开发布 `PythonScripts` :hammer_and_wrench:。 Gizmos :hammer_and_wrench: 和 Series :hammer_and_wrench: 主要针对于我个人使用习惯做了 layout，与 `NukeSurvivalToolkit` 中的内容大致相同，其表面的最大区别是在 Nuke 中的 layout 不一样，所以暂不公开，无意义。

在 PythonScripts 中整合了我在 Nuke 中所使用的一些较为`实用`, `高效`, 且`优雅`的 Scripts（脚本，或者称之为插件 :electric_plug:）,并在 Nuke 中做了 layout。

如若感兴趣建议尽可能地熟悉 `W_hotbox` :hammer: 插件，**`快速`**、**`高度自定义化`**、**`可以避免对很多快捷键的占用`**。若对Python有了解的话，会使你锦上添花 :sunflower:。

<br />

## Download :books:

> 若熟悉GitHub可略过

举例：

点击右侧的 `Releases` > `latest` 会进入到以下页面

点击 `Assets` 下的第一个就可以了。

<br />

## Install :books:

> 若熟悉安装可略过

1. 将 `nuLibrary` :file_folder: 文件夹复制到用户目录的 `.nuke` :file_folder: 文件夹内
2. - 若 `.nuke` :file_folder: 文件夹内没有 `init.py` 文件，则创建一个`init.txt`文件，并将以下代码复制到文件中， 最后将 `init.txt` 更改为 `init.py`
   - 若 `.nuke` :file_folder: 文件夹内存在 `init.py` 文件，打开 `init.py` （右键用记事本方式打开或用你会的一种方式打开。若不会打开，请将电脑关鸡，鸡你太美！:bomb::boom:），
      并将以下代码复制到文件中。
      ```python
      import nuke

      nuke.pluginAddPath('./nuLibrary')
      ```

> 想要深入了解 nuke 插件安装？请查看官方指导 [Installing Plug-ins](https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html#installingplugins-ref-label)

什么 :question: 你还想问怎么 uninstall :question: 直接 delete :wastebasket: 就好了~（删除掉文件夹、文件或文件中的代码）

<br />

## Introduce :books:

:heavy_check_mark: 完成安装后可以看到位于 Nuke 顶部菜单栏右侧的 `PythonScripts` 一栏，并且内有显示 **`快捷键`** ，请查看。

<p align="center"><img src="./images/PythonScript_layout.png"></p>



#### 3D :label:
- animatedSnap3D
  - > _作者：Ivan Busquets
  - > _使用方法：[https://www.nukepedia.com/python/3d/animatedsnap3d](https://www.nukepedia.com/python/3d/animatedsnap3d)_

#### Import_Export :label:
- CollectFiles
  - > _作者：Mariano Antico_
  - > _使用方法：[https://www.nukepedia.com/python/import/export/collectfiles](https://www.nukepedia.com/python/import/export/collectfiles)_

#### Misc :label:
- Default
  - > _作者：Simon Jokuschies_
  - > _使用方法：[https://www.nukepedia.com/python/misc/default-automatic-knobdefaults](https://www.nukepedia.com/python/misc/default-automatic-knobdefaults)_
- winExploreDir
  - > _作者: Thorsten 编写， Varun Hadkar 发布。（思路来源于 Thorsten，代码已全部被我更改。现已适用于 Windows、Linux、Mac）_
  - > 使用方法：
    > 

#### NodeGraph :label:
- AlignNodes
- MultiChannelSplit
- V_Tools
- W_scaleTree
- W_smartAlign

#### UI :label:
- Channel_Hotbox
- CloseAllProperties
- SearchReplacePanel
- W_hotbox 
  - > _作者：Wouter Gilsing_
  - > _使用方法：[https://www.nukepedia.com/python/ui/w_hotbox](https://www.nukepedia.com/python/ui/w_hotbox)_
