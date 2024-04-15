.. _download_installation:

Download and installation
=========================
Downloading and installing default should be pretty straight forward, simply follow the upcoming steps.

Download
--------
default can be downloaded from one of the following links:

Nukepedia_

.. _Nukepedia: http://www.nukepedia.com/python/misc/default-automatic-knobdefaults

LeafPictures_

.. _LeafPictures: http://www.leafpictures.de/default

Gitlab_

.. _Gitlab: https://gitlab.com/nukevfx/default

Installation
------------
After having downloaded default from one of the download links above simply extract it and put the default folder into your Nuke home directory.
Next, add the following line to your init.py::

   nuke.pluginAddPath("./default")

Alternatively you can put the default folder anywhere else on your hard drive. Simply make sure to add the correct path to your init.py file.
When launching Nuke you should see the default's menu under Scripts.

.. image:: img/default_menu.png