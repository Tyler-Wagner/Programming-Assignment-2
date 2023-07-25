"""
Original Creator: Tyler Wagner
Date Created: 7/21/23
Edited By: Tyler Wagner
Edited Date: 7/21/23
"""

import csv
from tabulate import tabulate #used to display the 2D array
from GUI import window
from Learning import DecisionTree
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
    # clf = DecisionTree()
    rest_data = pd.read_csv("restaurant.csv")
    rest_data.columns = ["Alt", "Bar", "Friday?", "Hungry?", "NumPatrons", "Price", "Rain?", "Res", "Type", "Est wait Time", "(Output)WillWait"]
    print(rest_data)
    # FilledCSVData = read_csv_file("restaurant.csv")
    # display_array(FilledCSVData) #READ THE COMMENT ON THE METHOD
    window() #this will display the window for the tree's and such
    # clf.fit(restaurant_train_df, restaurant_test_df)


if __name__ == "__main__":
    main()