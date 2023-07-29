"""
Author: Hayden Marshall
Date Created: 7/24/23
Edited by: Hayden Marshall and Tyler Wagner and Tyler Van Pelt
Date Edited: 7/28/23
"""

import numpy as np
from collections import Counter
from math import log2

class Node:
    def __init__(self, attribute = None, threshold = None, left = None, right = None, *, value = None):
        self.threshold = threshold
        self.left = left
        self.right = right 
        self.attribute = attribute
        self.value = value

    #checks to see if the node is a leaf node
    def is_leaf_node(self):
        return self.value is not None
    
class DecisionTree:
    def __init__(self, max_depth=None, num_attributes = None, min_num_examples = 2):
        self.max_depth = max_depth
        self.num_attributes = num_attributes
        self.min_num_examples = min_num_examples
        self.root_node = None

    def fit(self, training, testing, columns = None):
        
        if columns is None:
            columns = list(range(training.shape[1]))

        self.num_attributes = training.shape[1] if not self.num_attributes else min(self.num_attributes, training.shape[1])

        self.root_node = self.create_tree(training, testing, columns)

        return self.root_node

    def create_tree(self, training, testing, columns, depth=0):
        
        num_examples, num_attr = training.shape
        num_labels = len(np.unique(testing))


        #check for stopping criteria
        if(depth >= self.max_depth or num_labels == 1 or num_examples < self.min_num_examples):
            leaf_value = self._most_common_label(training)
            return Node(value=leaf_value)
        
        attribute_indexes = np.random.choice(num_attr, self.num_attributes, replace=False) #making sure we choose based on best information gain and not randomly
        #finding the best split
        best_attribute, best_thresh, best_gain = self._best_split(training, testing, attribute_indexes)

        # Print tree structure and information gains for current node
        if depth == 0:
            print("Root Node:")
        else:
            print("  " * depth + "Child Node:")
        print("  " * depth + f"Attribute: {columns[best_attribute]}")
        print("  " * depth + f"Information Gain: {best_gain:.4f}")
        print("  " * depth + f"Threshold: {best_thresh}")

        #create the child nodes
        left_indexes, right_indexes = self._split(training[:, best_attribute], best_thresh)
        left = self.create_tree(training[left_indexes, :],training[left_indexes], columns, depth + 1)
        right = self.create_tree(training[right_indexes, :], testing[right_indexes], columns, depth + 1)
        return Node(best_attribute, best_thresh, left, right)
    
    
    

    def _most_common_label(self, training):
        value = -1
        for column_index in range(training.shape[1]):
            if np.unique(training[:, column_index]).shape[0] > value:
                value = np.unique(training[:, column_index]).shape[0]

        return value

    def _entropy(self, attribute_values):
        
        attribute_values_str = attribute_values.astype(str)
        labels, values = np.unique(attribute_values_str, return_counts=True)
        qs = values / len(attribute_values_str)
        entropy = -np.sum([q * np.log(q)for q in qs if q > 0])
        return entropy
    
    def _information_gain(self, testing, training_column, thresh):
        
        parent_entropy = self._entropy(testing)
        
        left_indexes, right_indexes = self._split(training_column, thresh)
        

        if len(left_indexes) == 0 or len(right_indexes) == 0:
            return 0
        
        total_num = len(testing)
        num_left, num_right = len(left_indexes), len(right_indexes)
        examples_left, examples_right = self._entropy(testing[left_indexes]), self._entropy(testing[right_indexes])
        child_entropy = (num_left / total_num) * examples_left + (num_right / total_num) * examples_right
        

        information_gain = parent_entropy - child_entropy
        
        return information_gain
                


    def _split(self, training_column, split_threshold):
        left_indexes = np.argwhere(training_column <= split_threshold).flatten()
        right_indexes = np.argwhere(training_column > split_threshold).flatten()
        return left_indexes, right_indexes

    def _best_split(self, training, testing, attribute_indexes):
        
        best_gain = -1
        split_index, split_threshold = None, None

        for attribute_index in attribute_indexes:
            
            training_column = training[:, attribute_index]
            
            thresholds = np.unique(training_column)

            
            

            for thr in thresholds:
                #calculate information gain
                gain = self._information_gain(training, training_column, thr) #CHECK HERE FOR INFORMATION GAIN ERRORS

                if gain > best_gain:
                    best_gain = gain
                    split_index = attribute_index
                    split_threshold = thr

                    

        return split_index, split_threshold, best_gain
    

    
    def predict(self, training):
        
        return np.array([self._traverse_tree(x, self.root_node) for x in training])
    
    def _traverse_tree(self, x, node):
        
        if node.is_leaf_node():
            return node.value
        
        if x[node.attribute] <= node.threshold:
            return self._traverse_tree(x ,node.left)
        
        return self._traverse_tree(x, node.right)