#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Blue
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for node in nodes:
    node['in1'].setValue('rgba')
    node['out1'].setValue('rgba')
    node['mappings'].setValue([(0, 'rgba.blue', 'rgba.red'), (0, 'rgba.blue', 'rgba.green'), (0, 'rgba.blue', 'rgba.blue'), (0, 'rgba.blue', 'rgba.alpha')])
    node['tile_color'].setValue(65535)
    node['label'].setValue("Blue > rgba")