import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from load_csv import load

def getCountry(name: str, data: pd.DataFrame) -> np.array:
    ids = data.index[data['country'] == name].tolist()
    return data.iloc[ids[0]].to_numpy()[1:250]

def main():
    """main function"""
    data = load("population_total.csv")
    x = data.columns.to_numpy()[1:250]
    y = getCountry("France", data)
    y2 = getCountry("Belgium", data)
    plt.plot(x, y2, color='b', label='Belgium')
    plt.plot(x, y, color='g', label='Germany')
    plt.gca().xaxis.set_major_locator(MultipleLocator(base=40))
    plt.gca().yaxis.set_major_locator(MultipleLocator(base=20))
    plt.xlabel('Year')
    plt.ylabel('Total Population')
    plt.title('Population Projections')
    plt.show()


if __name__ == "__main__":
    main()
