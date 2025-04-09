import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Visualizer import Visualizer


class TestVisualizer:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.visualizer = Visualizer()

    def run_tests(self):
        print("Running histogram plot test...")
        self.visualizer.plot_histogram(self.data, 'Rating', bins=5)

        print("Running boxplot test...")
        self.visualizer.plot_boxplot(self.data, 'Budget in USD')

        print("Running scatter plot test...")
        self.visualizer.plot_scatter(self.data, 'Budget in USD', 'Rating')

        print("Running correlation matrix plot test...")
        self.visualizer.plot_correlation_matrix(self.data)


if __name__ == "__main__":
    data_path = 'C:\\Users\\merye\\PycharmProjects\\PythonTermProject\\data.csv'
    test_visualizer = TestVisualizer(data_path)
    test_visualizer.run_tests()