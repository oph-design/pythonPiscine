import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from load_csv import load


def main():
    """main function"""
    lifeex = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    x = income.get("1900").to_numpy()
    y = lifeex.get("1900").to_numpy()
    # plt.gca().xaxis.set_major_locator(MultipleLocator(base=40))
    # plt.gca().yaxis.set_major_locator(MultipleLocator(base=20))
    plt.scatter(x, y)
    plt.xlabel("Gross Domestic Product")
    plt.ylabel("Lifeexpectancy")
    plt.title("1900")
    plt.show()


if __name__ == "__main__":
    main()
