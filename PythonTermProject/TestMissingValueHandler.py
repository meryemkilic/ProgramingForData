import pandas as pd
import numpy as np
from MissingValueHandler import MissingValueHandler


class TestMissingValueHandler:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.handler = MissingValueHandler()

        # Creating some missing values for testing
        self.data.loc[1, 'Rating'] = np.nan
        self.data.loc[2, 'Budget in USD'] = np.nan
        self.data.loc[3, 'Awards'] = np.nan

    def run_tests(self):
        print("Original data with missing values:")
        print(self.data)

        print("\nFilling missing values with mean:")
        data_filled_mean = self.handler.fill_mean(self.data.copy(), ['Rating', 'Budget in USD', 'Awards'])
        print(data_filled_mean)

        print("\nFilling missing values with median:")
        data_filled_median = self.handler.fill_median(self.data.copy(), ['Rating', 'Budget in USD', 'Awards'])
        print(data_filled_median)

        print("\nFilling missing values with constant value (0):")
        data_filled_constant = self.handler.fill_constant(self.data.copy(), ['Rating', 'Budget in USD', 'Awards'], 0)
        print(data_filled_constant)

        print("\nDropping rows with missing values:")
        data_dropped = self.handler.drop_missing(self.data.copy())
        print(data_dropped)


if __name__ == "__main__":
    data_path = 'C:\\Users\\merye\\PycharmProjects\\PythonTermProject\\data.csv'
    test_handler = TestMissingValueHandler(data_path)
    test_handler.run_tests()