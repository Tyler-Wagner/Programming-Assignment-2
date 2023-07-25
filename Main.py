"""
Original Creator: Tyler Wagner
Date Created: 7/21/23
Edited By: Tyler Wagner
Edited Date: 7/25/23
"""

import csv
from tabulate import tabulate #used to display the 2D array
from GUI import window
from HTLearning import DecisionTree, Node
import numpy as np
import pandas as pd

#allows the user to read a csv file and import it as a 2D array
def read_csv_file(file_path):
    CSVData = []
    with open(file_path, newline='') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            CSVData.append(row)
    return CSVData

#displays the table (ONLY USE IF YOU THINK THERE IS AN ERROR IN THE TABLE)
def display_array(FilledCSVData):
    myheaders = FilledCSVData[0]
    data = FilledCSVData[1:]
    print(tabulate(data, headers=myheaders, tablefmt = "simple"))

def main():
    
    tree = DecisionTree(max_depth=10) #change max depth to be a user input
    training_rest_data = pd.read_csv("restaurant.csv")
    training_rest_data.columns = ["Alt", "Bar", "Friday?", "Hungry?", "NumPatrons", "Price", "Rain?", "Res", "Type", "Est wait Time", "(Output)WillWait"]
    testing_rest_data = pd.read_csv("restaurant_test.csv")
    testing_rest_data.columns = ["Alt", "Bar", "Friday?", "Hungry?", "NumPatrons", "Price", "Rain?", "Res", "Type", "Est wait Time", "(Output)WillWait"]
    #print(tree._most_common_label(training_rest_data))

    #error checking area
    #print(training_rest_data.isnull().sum())
    print(training_rest_data.dtypes)


if __name__ == "__main__":
    main()