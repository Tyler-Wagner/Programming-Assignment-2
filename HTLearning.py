"""
Author: Hayden Marshall
Date Created: 7/24/23
Edited by: Hayden Marshall
Date Edited: 7/24/23
"""

import numpy as np
from collections import Counter

class Node:
    def __init__(self, examples, children, attribute, depth):
        self.examples = examples
        self.children = children
        self.attribute = attribute
        self.depth = depth

    #checks to see if the node is a leaf node
    def is_leaf_node(self):
        if(not self.children):
           return True
        
        return False
    
class DecisionTree:
    def __init__(self, root_node = None, max_depth=None, num_attributes = None, min_num_examples = 2):
        self.root_node = root_node
        self.max_depth = max_depth
        self.num_attributes = num_attributes
        self.min_num_examples = min_num_examples

    def fit(self, training, testing):
        self.num_attributes = training.shape[1] if not self.num_attributes else min(self.num_attributes, training.shape[1])
        

        self.root = self.create_tree(training, testing)

    def create_tree(self, training, testing, depth=0):
        num_examples, num_attr = training.shape
        num_labels = len(np.unique(testing))

        #check for stopping criteria
        if(depth >= self.max_depth or num_labels == 1 or num_examples < self.min_num_examples):
            leaf_value = self._most_common_label(testing)
            return Node(value=leaf_value)
        
        attribute_indexes = np.random.choice(num_attr, self.num_attributes, replace=False) #making sure we choose based on best information gain and not randomly

        #finding the best split
        best_attribute = self._best_split(training, testing, attribute_indexes)

        #create the child nodes



    def _most_common_label(self, testing):
        counter = Counter(testing)
        value = counter.most_common(1)[0][1]
        return value
    

    def entropy(self, attribute_values):
        hist = np.bincount(attribute_values)

        qs = hist / len(attribute_values)

        return -np.sum(q * np.log2(q) for q in qs if q > 0)
    
    def information_gain(self):

        parent_entropy = self.entropy()

    def split():
        return True

    def _best_split(self, training, testing, attribute_indexes):
        return True