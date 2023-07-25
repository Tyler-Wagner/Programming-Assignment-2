import numpy as np

class Node:
    def __init__(self, examples, children, attribute, depth):
        self.examples = examples
        self.children = children
        self.attribute = attribute
        self.depth = depth

    def is_leaf_node(self):
        if(not self.children):
           return True
        
        return False
    
class DecisionTree:
    def __init__(self, root_node, max_depth):
        self.root_node = root_node
        self.max_depth = max_depth

    def entropy(self, attribute_values):
        hist = np.bincount(attribute_values)

        qs = hist / len(attribute_values)

        return -np.sum(q * np.log2(q) for q in qs if q > 0)
    
    def information_gain(self):

        parent_entropy = self.entropy()

    def split():
        return True

    def best_split():
        return True