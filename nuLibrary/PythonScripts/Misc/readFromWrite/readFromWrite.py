import os
import nuke


def get_write_nodes():
    write_nodes = []
    for node in nuke.selectedNodes():
        if node.Class() == 'Write':
            write_nodes.append(node)
    if len(write_nodes) > 0:
        return write_nodes
    else:
        nuke.message("You haven't select any Write node.")


def get_write_file(write_node):
    write_file = write_node['file'].value()
    write_evaluate = write_node['file'].evaluate()
    if write_file != write_evaluate and '%04d' in write_file:
        write_file = write_evaluate.replace(str(nuke.frame()).zfill(4), '%04d')
    if write_evaluate.endswith('.mov'):
        write_file = write_evaluate

    file_format = os.path.splitext(write_file)[-1]
    filename_pattern = os.path.basename(write_file).split(".")[0]

    if '%04d' in write_file or '####' in write_file:
        image_sequence = []
        for img in os.listdir(os.path.dirname(write_file)):
            if filename_pattern in img and img.endswith(file_format):
                image_sequence.append(img)
        image_sequence.sort()
        return '{name} {start}-{end}'.format(
            name=write_file,
            start=image_sequence[0].split('.')[-2],
            end=image_sequence[-1].split('.')[-2]
        )
    else:
        return write_file


def create_read_node(read_file):
    read_node = nuke.createNode('Read')
    read_node['file'].fromUserText(read_file)
    read_node['before'].setValue(0)
    read_node['after'].setValue(0)
    read_node['on_error'].setValue(1)


def run():
    write_nodes = get_write_nodes()
    for write_node in write_nodes:
        create_read_node(get_write_file(write_node))