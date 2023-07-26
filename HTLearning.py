"""
Author: Hayden Marshall
Date Created: 7/24/23
Edited by: Hayden Marshall and Tyler Wagner
Date Edited: 7/26/23
"""

import numpy as np
from collections import Counter
from math import log2

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
    def __init__(self, max_depth=None, num_attributes = None, min_num_examples = 2):
        self.max_depth = max_depth
        self.num_attributes = num_attributes
        self.min_num_examples = min_num_examples
        self.root_node = None

    def fit(self, training, testing):
        self.num_attributes = training.shape[1] if not self.num_attributes else min(self.num_attributes, training.shape[1])
        
        self.root_node = self.create_tree(training, testing)

    def create_tree(self, training, testing, depth=0):
        num_examples, num_attr = training.shape
        num_labels = len(np.unique(testing))

        #check for stopping criteria
        if(depth >= self.max_depth or num_labels == 1 or num_examples < self.min_num_examples):
            leaf_value = self._most_common_label(testing)
            return Node(value=leaf_value)
        
        attribute_indexes = np.random.choice(num_attr, self.num_attributes, replace=False) #making sure we choose based on best information gain and not randomly

        #finding the best split
        best_attribute, best_thresh = self._best_split(training, testing, attribute_indexes)

        #create the child nodes
        left_indexes, right_indexes = self._split(training[:, best_attribute], best_thresh)
        left = self.create_tree(training[left_indexes, :],training[left_indexes], depth + 1)
        right = self.create_tree(testing[right_indexes, :], training[right_indexes], depth + 1)
        return Node(best_attribute, best_thresh, left, right)



    def _most_common_label(self, testing):
        value = -1
        for column_name in testing:
            if testing[column_name].value_counts().nlargest(1).values[0] > value:
                value = testing[column_name].value_counts().nlargest(1).values[0]

        return value
    

    def _entropy(self, attribute_values):
        labels, values = np.unique(attribute_values, return_counts=True)
        qs = values / len(attribute_values)
        entropy = -np.sum([q * np.log(q)for q in qs if q > 0])
        return entropy
    
    def _information_gain(self, testing, training_column, thresh):

        parent_entropy = self._entropy(testing)
        print("Parent entropy: ")
        print(parent_entropy)

        left_indexes, right_indexes = self._split(training_column, thresh)
        print("Left indexes:")
        print(left_indexes)

        if len(left_indexes) == 0 or len(right_indexes) == 0:
            return 0
        
        total_num = len(testing)
        num_left, num_right = len(left_indexes), len(right_indexes)
        examples_left, examples_right = self._entropy(testing[left_indexes]), self._entropy(testing[right_indexes])
        child_entropy = (num_left / total_num) * examples_left + (num_right / total_num) * examples_right
        print("child entropy:")
        print(child_entropy)

        information_gain = parent_entropy - child_entropy
        print(information_gain)
        return information_gain
                


    def _split(self, training_column, split_threshold):
        left_indexes = np.argwhere(training_column <= split_threshold).flatten()
        right_indexes = np.argmax(training_column > split_threshold).flatten()
        return left_indexes, right_indexes

    def _best_split(self, training, testing, attribute_indexes):
        best_gain = -1
        split_index, split_threshold = None

        for attribute_index in attribute_indexes:
            training_column = training[:, attribute_index]
            thresholds = np.unique(training_column)

            for thr in thresholds:
                #calculate information gain
                gain = self._information_gain(training, training_column) #CHECK HERE FOR INFORMATION GAIN ERRORS

                if gain > best_gain:
                    best_gain = gain
                    split_index = attribute_index
                    split_threshold = thr

            return split_index, split_threshold
    

    
    def predict(self, training):
        return np.array([self._traverse_tree(x) for x in training])
    
    def _traverse_tree(self, x, node):
        if node.is_leaf_node():
            return node.value
        
        if x[node.feature] <= node.threshold:
            return self._traverse_tree(x ,node.left)
        
        return self._traverse_tree(x, node.right)