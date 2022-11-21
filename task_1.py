''' This file is for Python Data Project Problem 1'''
import csv
import matplotlib.pyplot as plt
from function_1 import bar_plot


def calculate():
    '''function to get data to plot graphs'''
    with open("population-estimates_csv.csv", encoding="utf-8") as inputfile:
        india_population = {}
        population_reader = csv.DictReader(inputfile)

        for population in population_reader:
            country = population['Region']
            population_count = population['Population']
            year = population['Year']
            if country == "India":
                india_population[year] = (
                    india_population.get(year, 0)
                    + (float(population_count) * 1000)
                )

    return india_population


def execute():
    ''' driver function'''
    # get required data from csv in dict and then call plot function

    india_population = calculate()

    bar_plot(india_population, "Year",
             "Population", "Population of India over years"
             )
    # show plot
    plt.show()


execute()  # driver function
