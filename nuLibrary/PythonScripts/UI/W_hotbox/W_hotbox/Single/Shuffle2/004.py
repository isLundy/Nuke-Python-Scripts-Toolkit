#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Alpha to rgba
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for node in nodes:
    node['in1'].setValue('rgba')
    node['out1'].setValue('rgba')
    node['mappings'].setValue([(0, 'rgba.alpha', 'rgba.red'), (0, 'rgba.alpha', 'rgba.green'), (0, 'rgba.alpha', 'rgba.blue'), (0, 'rgba.alpha', 'rgba.alpha')])
    node['tile_color'].setValue(1499027967)
    node['label'].setValue("Alpha > rgba")