#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Green
#
#----------------------------------------------------------------------------------------------------------

nodes = nuke.selectedNodes()

for node in nodes:
    node['in1'].setValue('rgba')
    node['out1'].setValue('rgba')
    node['mappings'].setValue([(0, 'rgba.green', 'rgba.red'), (0, 'rgba.green', 'rgba.green'), (0, 'rgba.green', 'rgba.blue'), (0, 'rgba.green', 'rgba.alpha')])
    node['tile_color'].setValue(6684927)
    node['label'].setValue("Green > rgba")