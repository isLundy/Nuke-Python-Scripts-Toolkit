#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Remove Alpha
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for node in nodes:
    node['in1'].setValue('rgba')
    node['out1'].setValue('rgba')
    node['mappings'].setValue([(0, 'rgba.red', 'rgba.red'), (0, 'rgba.green', 'rgba.green'), (0, 'rgba.blue', 'rgba.blue'), (-1, 'black', 'rgba.alpha')])
    node['tile_color'].setValue(1499027967)
    node['label'].setValue("Alpha = 0")