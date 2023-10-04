import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from load_csv import load

def main():
    """main function"""
    dataset = load("life_expectancy_years.csv")
    ids = dataset.index[dataset['country'] == 'Germany'].tolist()
    x = dataset.columns.to_numpy()[1:]
    y = dataset.iloc[ids[0]].to_numpy()[1:]
    plt.plot(x, y, color='g')
    plt.gca().xaxis.set_major_locator(MultipleLocator(base=40))
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title('Life expectancy germany')
    plt.show()


if __name__ == "__main__":
    main()
