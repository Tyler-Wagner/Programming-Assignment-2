"""
Original Creator: Tyler Wagner
Date Created: 7/21/23
Edited By: Tyler Wagner
Edited Date: 7/25/23
"""

import csv
from HTLearning import DecisionTree, Node
import numpy as np
import pandas as pd
from gui import display_results_window


def main():
    user_depth = int(input("Enter the max depth: "))
    # Load the restaurant.csv file
    data = pd.read_csv('restaurant.csv')

    # Prepare the data for training (using all columns as features except for the last column as the target)
    X_train = data.drop('Outputy', axis=1)
    y_train = data['Outputy']

    # Load the restaurant_test.csv file
    test_data = pd.read_csv('restaurant_test.csv')

    if 'Outputy' in test_data.columns:
        X_test = test_data.drop('Outputy', axis=1)
        y_test = test_data['Outputy']
    else:
        X_test = test_data

    # Create and train the DecisionTree classifier
    dt_classifier = DecisionTree(max_depth=user_depth)  # Set the max_depth as desired
    root_node = dt_classifier.fit(X_train.values, y_train.values, X_train.columns.tolist())

    # Evaluate the classifier on the test data
    predictions_test = dt_classifier.predict(X_test.values)

    # Save the trained model to a file using pickle
    with open('saved_model.pkl', 'wb') as f:
        np.save(f, dt_classifier)

    # Load the model from the file for prediction using pickle
    with open('saved_model.pkl', 'rb') as f:
        loaded_model = np.load(f, allow_pickle=True).item()

    # Load the restaurant_predict.csv file for prediction
    predict_data = pd.read_csv('restaurant_predict.csv')

    # Use the loaded model to predict on the new data
    predictions_new_data = loaded_model.predict(predict_data.values)

    # Display results in GUI
    display_results_window(predictions_test, predictions_new_data, root_node)




if __name__ == "__main__":
    main()