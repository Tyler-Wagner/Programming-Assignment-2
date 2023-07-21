"""
Original Creator: Tyler Wagner
Date Created: 7/21/23
Edited By: Tyler Wagner
Edited Date: 7/21/23
"""

import csv
from tabulate import tabulate #used to display the 2D array
import tkinter as tk

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
    file_path = 'restaurant.csv' #this will stay the same
    FilledCSVData = read_csv_file(file_path)
    #display_array(FilledCSVData) READ THE COMMENT ON THE METHOD


if __name__ == "__main__":
    main()