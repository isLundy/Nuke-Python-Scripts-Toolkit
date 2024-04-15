#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Red
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for node in nodes:
    node['in1'].setValue('rgba')
    node['out1'].setValue('rgba')
    node['mappings'].setValue([(0, 'rgba.red', 'rgba.red'), (0, 'rgba.red', 'rgba.green'), (0, 'rgba.red', 'rgba.blue'), (0, 'rgba.red', 'rgba.alpha')])
    node['tile_color'].setValue(2986344703)
    node['label'].setValue("Red > rgba")