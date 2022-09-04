.. _adding_knob_defaults:

Adding a new knob default
=========================
There are three ways to create new knob defaults.

1) Using the Add knobDefault window
-----------------------------------
When clicking the blue **add new knobDefault** button at the bottom left of the `default main window <main_window.html>`_ the "Add knobDefault" window appears.
This window lets you create new knobDefaults.

.. image:: img/add_knob_default_start.png

Simply type in the node class, the knob name and the default value that you would like to set.
Before adding the knob default make sure to click the **check validity** button.
This will check if the node name and the knob name are correct and prevents you from creating knob defaults that are invalid:

.. image:: img/add_knob_default_invalid.png

In this example the knob name is invalid. The knob name should be lowercase, so 'size'.

.. image:: img/add_knob_default_valid.png

When everything is correct click the **register knobDefault** button.
The knob default will be added to the list. You don't need to restart Nuke, the knob default is immediately set.
You can always edit or delete any knob default from the list.

How do I know the exact node- and knob name?
````````````````````````````````````````````
To find out the node name create the node, select it and press **I**.
In the upcoming window you will see the node class.

.. image:: img/hint_node_name.png

To find out the knob name open the node in the properties bin and hover over the knob to change.
The name in bold is the internal knob name.

.. image:: img/hint_knob_name.png


.. _context_menu:

2) Using the context menu
-------------------------
You can also set knob defaults interactively and on the fly.
Set up the knob of your choice to the value that you would like to have as a knob default.
Then simply right click the knob and choose from the context menu: **default -> set as new knobDefault**.

.. image:: img/context_menu_set.png

If you don't see the 'default' context menu follow the steps in 3).

3) Using the list menu
----------------------
The default context menu does not work with drop down menus, unfortunately.
If you right click a knob and don't see the 'default' menu in the context menu then do the following steps.

Right click any other knob that does actually show the 'default' context menu. From the menu choose **show knob list**.

.. image:: img/context_menu_list.png

The upcoming window contains a drop down menu 'knob' that contains all knobs of the selected node - also knobs that weren't accessible through the 'default' context menu.
Select the desired knob from the drop down list and set the desired value.

.. image:: img/all_knobs_list.png
