import pandas as pd
import numpy as np
import csv
from GUI import window
from HTLearning import DecisionTree, Node

class Main:
    def __init__(self):
        self.run()

    def run(self):
        # Read the data from the CSV file into a Pandas DataFrame
        data = pd.read_csv('iris.csv')
        print (data.columns)

        # Prepare the data for training (using the first 4 columns as features and the last column as the target)
        X = data.drop('variety', axis=1)
        y = data['variety']

        # Create and train the HTLearning Decision Tree classifier
        dt_classifier = DecisionTree(max_depth=5)  # Set the max_depth as desired
        dt_classifier.fit(X.values, y.values)

        # Example prediction using a sample data point
        sample_data = np.array([[5.1, 3.5, 1.4, 0.2]])  # Replace with your sample data
        prediction = dt_classifier.predict(sample_data)
        print("Predicted class:", prediction[0][0])


if __name__ == "__main__":
    main = Main()