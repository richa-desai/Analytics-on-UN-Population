''' This file is for Python Data Project Problem 2'''
import csv
import matplotlib.pyplot as plt
from function_1 import bar_plot


def calculate():
    '''function to get data to plot graphs'''
    with open("population-estimates_csv.csv", encoding="utf-8") as inputfile:
        asean_population = {}
        population_reader = csv.DictReader(inputfile)

        for population in population_reader:
            country = population['Region']
            population_count = population['Population']
            year = int(population['Year'])
            if year == 2014:
                if country in ["Cambodia","Brunei","Indonesia","Laos",
                               "Malaysia","Myanmar","Philippines","Singapore","Thailand","Vietnam"]:
                    asean_population[country] = (
                        asean_population.get(country, 0)
                        + (float(population_count) * 1000)
                    )

    return asean_population


def execute():
    ''' driver function'''
    # get required data from csv in dict and then call plot function

    asean_population = calculate()

    bar_plot(asean_population, "Country",
                "Population", "Population of ASEAN countries for the year 2014"
                )
    # show plot
    plt.show()


execute()  # driver function
