# Max van Leeuwen - maxvanleeuwen.com
# CloseAllProperties - 1.1
#
# Closes all property boxes at once (especially useful if you like to use floating windows).


import nuke


def CloseAllProperties():
    # for each node, even the ones in groups
    for n in nuke.allNodes(recurseGroups=True):
        # hide the control panel
        # if n.shown():
        n.hideControlPanel()

    if nuke.root().shown():
        nuke.root().hideControlPanel()

# autostart (if not imported)
if __name__ == "__main__":
    CloseAllProperties()