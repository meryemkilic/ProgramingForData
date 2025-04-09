import pandas as pd
import numpy as np
from OutlierHandler import OutlierHandler
class TestOutlierHandler:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.handler = OutlierHandler()

        # Creating some outliers for testing
        self.data.loc[0, 'Rating'] = 100  # Extreme outlier for 'Rating'
        self.data.loc[1, 'Budget in USD'] = 1e10  # Extreme outlier for 'Budget in USD'
        self.data.loc[2, 'Awards'] = -100  # Extreme outlier for 'Awards'

    def run_tests(self):
        print("Original data with outliers:")
        print(self.data)

        print("\nData after removing outliers using IQR method:")
        data_no_outliers = self.handler.iqr_outliers(self.data.copy(), 'Rating')
        print(data_no_outliers)

        print("\nData after replacing outliers with median using IQR method:")
        data_replaced_outliers = self.handler.replace_outliers_with_median(self.data.copy(), 'Budget in USD')
        print(data_replaced_outliers)


if __name__ == "__main__":
    data_path = 'C:\\Users\\merye\\PycharmProjects\\PythonTermProject\\data.csv'
    test_handler = TestOutlierHandler(data_path)
    test_handler.run_tests()