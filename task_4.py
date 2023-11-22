''' This file is for Python Data Project Problem 4'''
import csv
import matplotlib.pyplot as plt
from function_1 import bar_group_plot


def calculate():
    '''function to get data to plot graphs'''
    with open("population-estimates_csv.csv", encoding="utf-8") as inputfile:
        cambodia_population = {}
        brunei_population = {}
        indonesia_population = {}
        malaysia_population = {}
        myanmar_population = {}
        philippines_population = {}
        singapore_population = {}
        thailand_population = {}
        population_reader = csv.DictReader(inputfile)

        for population in population_reader:
            country = population['Region']
            population_count = population['Population']
            year = int(population['Year'])
            if 2004 <= year <= 2014:
                if country in ["Cambodia", "Brunei", "Indonesia", "Laos",
                               "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand",
                               "Vietnam"]:
                    match country:
                        case "Cambodia":
                            cambodia_population[year] = (
                                cambodia_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Brunei":
                            brunei_population[year] = (
                                brunei_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Indonesia":
                            indonesia_population[year] = (
                                indonesia_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Malaysia":
                            malaysia_population[year] = (
                                malaysia_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Myanmar":
                            myanmar_population[year] = (
                                myanmar_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Philippines":
                            philippines_population[year] = (
                                philippines_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Singapore":
                            singapore_population[year] = (
                                singapore_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )
                        case "Thailand":
                            thailand_population[year] = (
                                thailand_population.get(year, 0)
                                + (float(population_count) * 1000)
                            )

    return {"Cambodia": cambodia_population, "Indonesia": indonesia_population,
            "Malaysia": malaysia_population, "Myanmar": myanmar_population,
            "Philippines": philippines_population, "Singapore": singapore_population,
            "Thailand": thailand_population}


def execute():
    ''' driver function'''
    # get required data from csv in dict and then call plot function

    asean_population = calculate()

    bar_group_plot(asean_population, "Year",
                   "Population", "Population of ASEAN countries as groups over the years 2004-2014"
                   )
    # show plot
    plt.show()


execute()  # driver function
