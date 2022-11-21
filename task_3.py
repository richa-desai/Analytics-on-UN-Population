''' This file is for Python Data Project Problem 3'''
import csv
import matplotlib.pyplot as plt
from function_1 import bar_plot


def calculate():
    '''function to get data to plot graphs'''
    with open("population-estimates_csv.csv", encoding="utf-8") as inputfile:
        saarc_population = {}
        population_reader = csv.DictReader(inputfile)

        for population in population_reader:
            country = population['Region']
            population_count = population['Population']
            year = int(population['Year'])
            if country in ["Afghanistan","Bangladesh","Bhutan","India",
                            "Maldives","Nepal","Pakistan","Sri Lanka"]:
                saarc_population[year] = (
                    saarc_population.get(year, 0)
                    + (float(population_count) * 1000)
                )

    return saarc_population


def execute():
    ''' driver function'''
    # get required data from csv in dict and then call plot function

    saarc_population = calculate()

    bar_plot(saarc_population, "Year",
                "Population", "Population of SAARC countries"
                )
    # show plot
    plt.show()


execute()  # driver function
