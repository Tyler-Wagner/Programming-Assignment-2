"""
Original Creator: Tyler Wagner
Date Created: 7/21/23
Edited By: Tyler Wagner
Edited Date: 7/25/23
"""

import csv
from GUI import window
from HTLearning import DecisionTree, Node
import numpy as np
import pandas as pd


def main():
    user_in_max_depth = int(input("Enter the max depth you want the tree to have:"))

    tree = DecisionTree(max_depth=user_in_max_depth) #change max depth to be a user input
    training_rest_data = pd.read_csv("restaurant.csv")
    training_rest_data.columns = ["Alt", "Bar", "Friday?", "Hungry?", "NumPatrons", "Price", "Rain?", "Res", "Type", "Est wait Time", "(Output)WillWait"]
    testing_rest_data = pd.read_csv("restaurant_test.csv")
    testing_rest_data.columns = ["Alt", "Bar", "Friday?", "Hungry?", "NumPatrons", "Price", "Rain?", "Res", "Type", "Est wait Time", "(Output)WillWait"]
    
    tree.fit(training_rest_data, testing_rest_data)


    #ERROR TESTING
    # print(training_rest_data)
    # MCL = tree._most_common_label(training_rest_data)
    # print(MCL)
    #print(training_rest_data.isnull().sum())
    # entropy = tree.entropy(training_rest_data["Alt"])
    # print(entropy)


if __name__ == "__main__":
    main()