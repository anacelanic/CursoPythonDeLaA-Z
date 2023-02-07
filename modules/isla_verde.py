class Tree():
    
    def __init__(self, name, height, diameter, talkative = False):
        self.name = name
        self.height = height
        self.diameter = diameter
        self.talkative = talkative
        
    def __str__(self):
        if self.talkative:
            espacio = ""
        else:
            espacio = "no "
        return '{} es un árbol {}parlante que mide {}cm de altura y {}cm de diámetro'.format(self.name, espacio, self.height, self.diameter)
    
    def talk(self, message):
        if self.talkative:
            return str(message)
        return '{} no es un árbol parlante'.format(self.name)
    
    def grow(self, add_height = 0, add_diameter = 0):
        self.height += add_height
        self.diameter += add_diameter    
    

trees = []

def born_tree(tree_object):
    trees.append(tree_object)
    print('{} acaba de nacer'.format(tree_object.name))
    print(tree_object)

def dead_tree(tree_object):
    trees.remove(tree_object)
    print('Descansa en paz, {}'.format(tree_object.name))