def alignNodes(nodes, direction = 'x'):
    '''Align nodes either horizontally or vertically.'''
    direction = direction.lower()
    if len(nodes) < 2:
        return
    if direction not in ('x', 'y'):
        raise ValueError('direction argument must be x or y')
    
    if direction == 'x':       
        positions = [float(n['xpos'].value() + n.screenWidth() * .5) for n in nodes]
    else:
        positions = [float(n['ypos'].value() + n.screenHeight() * .5) for n in nodes]
    avrg = sum(positions) / len(positions)
    for n in nodes:
        if direction == 'x':
            for n in nodes:
                n.setXpos(int(avrg - n.screenWidth() * .5))
        else:
            for n in nodes:
                n.setYpos(int(avrg - n.screenHeight() * .5))

    return avrg