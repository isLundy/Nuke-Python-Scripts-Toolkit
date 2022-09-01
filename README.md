<h1 align="center"> 
      <img src="/images/python-logo-only.png">
      <br> PythonScripts Toolkit for Nuke
</h1>

<br />

## Perface :books:

> 当你看到这个页面时说明你可以访问 GitHub（很显然你看到了一句废话）, 若熟悉科学上网请使用代理访问 :rocket:（无需多言），若不熟悉可略过。

我个人平时整合并制作了一个名为 `nuLibrary` 的工具库 :european_castle:（大约是在2018年12月，后续慢慢地不断优化）， nuLibrary 内含有 `Gizmos` :hammer_and_wrench:、 `PthonScripts` :hammer_and_wrench:、 `Series` :hammer_and_wrench: 三个不同的工具包，里面含有我平时搜集并使用的 gizmo 和 script，大部分来自于网络，少部分为自己编写。

nuLibrary 一直在作为个人使用，最近决定公开发布其中的 `PythonScripts` :hammer_and_wrench:。 `Gizmos` :hammer_and_wrench: 和 `Series` :hammer_and_wrench: 主要针对于我个人使用习惯做了排版布局，与 `NukeSurvivalToolkit` 中的内容类似，其表面的最大区别是在 Nuke 中的布局，所以暂不公开，无过多意义。

在 `PythonScripts` :hammer_and_wrench: 中整合了我在 Nuke 中所使用的一些较为 **`实用`**、 **`高效`** 且 **`优雅`** 的 Scripts（脚本、命令或者称之为插件 :electric_plug:），这完全改变了我与 Nuke 的交互方式。

> 可通过单击文件标头来访问该目录。 每个标题都列在目录中，可单击标题导航到所选部分。

<br />

## Download :books:

> 若熟悉 GitHub 可略过

点击右侧的 `Releases` > `latest`， 进入页面后点击 `Assets` 下的第一个 `.zip` 链接 :link: 即可。

<br />

## Install :books:

> 若熟悉安装可略过

1. 下载 `.zip` 文件 :briefcase: 解压后将 `nuLibrary` 文件夹 :file_folder: 复制到用户目录的 `.nuke` 文件夹 :file_folder: 内。
2. - 若 `.nuke` 文件夹 :file_folder: 内没有 `init.py` 文件，则创建一个 `init.txt` 文件，并将以下代码复制到文件中， 最后将 `init.txt` 更改为 `init.py`
   - 若 `.nuke` 文件夹 :file_folder: 内存在 `init.py` 文件，打开 `init.py`，并将以下代码复制到文件中。
   
     （右键用记事本方式打开或用你会的一种方式打开。若不会打开 :fearful:，请将电脑关 :chicken: :exclamation:）
      
     ```python
     import nuke

     nuke.pluginAddPath('./nuLibrary')
     ```
3. 打开 Nuke，尽情享用 ！

> 想要深入了解 nuke 插件安装？请查看官方指导 [Installing Plug-ins](https://learn.foundry.com/nuke/developers/latest/pythondevguide/installing_plugins.html#installingplugins-ref-label)

<br />

什么 :question: 你还想了解怎么 uninstall :question: 直接 delete :wastebasket: 即可~
- 只需删除 `.nuke` :file_folder: 文件夹内 `init.py` 中的下列代码， `nuLibrary` :file_folder: 文件夹可删也可不删~

  ```python
  nuke.pluginAddPath('./nuLibrary')
  ```

<br />

## Introduce :books:

### PythonScripts 菜单 :scroll:

完成安装后 :heavy_check_mark: 可以看到位于 Nuke 顶部菜单栏右侧的 `PythonScripts` 菜单 :scroll:。

<p align="center"><img src="./images/PythonScript_layout.png"></p>

以下为 `PythonScripts` :hammer_and_wrench: 中各种分类的介绍，分类方式遵循 `NukePedia`。目前存在 `3D` :label:、`Import_Export` :label:、`Misc` :label:、`NodeGraph` :label:、`UI` :label: 五种分类（以后可能会根据相应 script 继续添加分类）。有关快捷键，安装后请在 Nuke 中的 `PythonScripts` 菜单 :scroll: 内查看。

> 如若感兴趣建议尽可能地熟悉 `W_hotbox` :hammer: （下面有介绍），**`快速高效`**、**`高度自定义化`**、**`大幅减少了对快捷键的占用`**。完全熟悉后，会使你 **`锦上添花`** :sunflower: **`如虎添翼`** :eagle:。

<br />

#### 3D :label:
- `animatedSnap3D`
  - > _作者：Ivan Busquets_
  - > _使用方法：[https://www.nukepedia.com/python/3d/animatedsnap3d](https://www.nukepedia.com/python/3d/animatedsnap3d)_

<br />

#### Import_Export :label:
- `CollectFiles`
  - > _作者：Mariano Antico_
  - > _使用方法：[https://www.nukepedia.com/python/import/export/collectfiles](https://www.nukepedia.com/python/import/export/collectfiles)_

- `CreateOutDirs`
  - > _来源：Nuke 官方开发者文档_
  - > _使用方法：无需操作，打开 Nuke 后自动启用。它会在 `Write` 节点开始渲染前的那一刻自动检测当前 `Write` 节点的文件目录是否存在，若为否，则先创建该目录然后再渲染。相当于主动勾选 	:ballot_box_with_check: 了 `Write` 节点中的 `create directories` 选项。只不过它无视 `create directories` 选项，无论是否勾选，都会运行 `CreateOutDirs` :heavy_check_mark:。待发布_

<br />

#### Misc :label:
- `Auto open .nk as NukeX`
  - > _作者：Max van Leeuwen_
  - > _使用方法：仅针对于 Windows 系统，需要到文件路径 .nuke/nuLibrary/PythonScripts/Misc/Auto_open_nk_as_NukeX 下手动运行。[https://www.nukepedia.com/miscellaneous/auto-open-nk-as-nukex](https://www.nukepedia.com/miscellaneous/auto-open-nk-as-nukex)_

- `Default`
  - > _作者：Simon Jokuschies_
  - > _使用方法：[https://www.nukepedia.com/python/misc/default-automatic-knobdefaults](https://www.nukepedia.com/python/misc/default-automatic-knobdefaults)_

- `openExploreDir`
  - > _作者：Lundy Hu (Yes, It's me !), （原名：winExploreDir，原作者：Thorsten 编写，Varun Hadkar 发布。思路来源于 Thorsten，名称和代码现已全部被我更改，已适用于 Windows、Linux、Mac，并添加了新功能）_
  - > _使用方法：待发布_

- `readFromWrite`
  - > _作者：未知_
  - > _使用方法：表里如一，和字面意思一样。可使用快捷键从选定的 Write 节点读取输出的图像。_

<br />

#### NodeGraph :label:
- `AlignDots`
  - > _作者：Max van Leeuwen_
  - > _使用方法：快捷键已被我更改。[https://www.nukepedia.com/python/nodegraph/aligndots](https://www.nukepedia.com/python/nodegraph/aligndots)_

- `AlignNodes`
  - > _作者：Frank Rueter_
  - > _使用方法：快捷键已被我更改。[https://www.nukepedia.com/python/nodegraph/alignnodes](https://www.nukepedia.com/python/nodegraph/alignnodes)_

- `MultiChannelSplit`
  - > _作者：Simon Jokuschies_
  - > _使用方法：[https://www.nukepedia.com/python/nodegraph/multichannelsplit_v03](https://www.nukepedia.com/python/nodegraph/multichannelsplit_v03)_

- `V_Tools`
  - > _作者： Victor Perez_
  - > _使用方法：只保留了 V_ConvertGizmosToGroups，V_PostageStampGenerator，V_PresetBackdrop 这三个 scripts（另外一个由上面 readFromWrite 替代）。功能同字面意思一样。_

- `W_scaleTree`
  - > _作者：Wouter Gilsing_
  - > _使用方法：[https://www.nukepedia.com/python/nodegraph/w_scaletree](https://www.nukepedia.com/python/nodegraph/w_scaletree)_

- `W_smartAlign`
  - > _作者：Wouter Gilsing_
  - > _使用方法：快捷键已被我更改。[https://www.nukepedia.com/python/nodegraph/w_smartalign](https://www.nukepedia.com/python/nodegraph/w_smartalign)_

<br />

 > _`AlignDots`、`AlignNodes`、`W_smartAlign` 现在三者的快捷键已关联到 `Alt + 0 2 4 5 6 8`，更改这三个 scripts 的快捷键的原因是为了相互配合适用，在使用数字键盘对齐节点时极为便利。_

<br />

#### UI :label:
- `AnimationMaker`
  - > _作者：David Emeny_
  - > _使用方法：[https://www.nukepedia.com/python/ui/animation-maker](https://www.nukepedia.com/python/ui/animation-maker)_

- `Channel_Hotbox`
  - > _作者：Falk Hofmann_
  - > _使用方法：[https://www.nukepedia.com/python/ui/channel-hotbox](https://www.nukepedia.com/python/ui/channel-hotbox)_

- `CloseAllProperties`
  - > _作者：Max van Leeuwen_
  - > _使用方法：使用对应快捷键可一次关闭所有已打开的 Node 面板和 Project Settings 面板。 对于习惯使用 Node 浮动面板的人非常适合（例如我）, 可以减少对操作空间的占用，nice :clap: ！_

- `SearchReplacePanel`
  - > _作者：Frank Rueter_
  - > _使用方法：[https://www.nukepedia.com/python/ui/searchreplacepanel](https://www.nukepedia.com/python/ui/searchreplacepanel)_

- `W_hotbox `
  - > _作者：Wouter Gilsing_
  - > _使用方法：[https://www.nukepedia.com/python/ui/w_hotbox](https://www.nukepedia.com/python/ui/w_hotbox)，我个人编写的一些 scripts 也放在了 W_hotbox 中，因为实在是太方便了。_

<br />

#### Question :question:

Q1. 安装完打开 Nuke 后为什么有些没有显示在 `PythonScripts` 菜单中 :question: 例如 `W_hotbox` `animatedSnap3D` 或者 `CreateOutDirs`。

- > 有些弊大于利。有些作者的主要代码块内设置了布局，为方便以后的更新一般采用作者的默认设置。对于 `W_hotbox`，看了它的使用方法后会发现它分别显示在了 Nuke 的 `Edit` 菜单最下面和 `Preferences` 面板中。对于 `animatedSnap3D`，使用方法中也有介绍到，它会显示在 `Card`、 `Cube`、 `Camera` 等这类三维节点面板的 `snap_menu` 旋钮中。

- > 有些没有必要显示。对于 `CreateOutDirs` 这类自动启动、自动运行、全程后台的 scripts。

<br />

### PythonScript 文件夹 :file_folder: 结构
> 若不熟悉变成可略过。

`.nuke/nuLibrary/init.py` 和 `.nuke/nuLibrary/PythonScripts/init.py` 会按照规则自动添加文件夹 :file_folder: 目录。若需自定义，可自行更改。

## Appendix :books:

在此非常感谢 `Wouter Gilsing`、`Frank Rueter`、`Max van Leeuwen`、`Falk Hofmann`、`David Emeny`、`Victor Perez`、`Simon Jokuschies`、`Mariano Antico`、`Ivan Busquets`、`Thorsten`、`Varun Hadkar` 以及 Nuke 社区的其他创作者、分享者。 :sparkling_heart:

