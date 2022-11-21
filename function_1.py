''' This file has all the functions '''
import matplotlib.pyplot as plt


def bar_plot(bar_plot_data: dict, xlabel: str, ylabel: str, title: str):
    """Pass dict variable having keys to plot on x-axis and pass values to plot on y-axis"""
    # initialisation
    x_axis_keys = list(bar_plot_data.keys())
    y_axis_values = list(bar_plot_data.values())
    fig = plt.figure()

    # creating the bar plot
    plt.bar(x_axis_keys, y_axis_values)
    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.xticks(x_axis_keys)

def bar_group_plot(bar_group_data: list, xlabel: str, ylabel: str, title: str):
    '''Pass dict variable'''
    # initialisation
    y1 = bar_group_data["Cambodia"].values()
    y2 = bar_group_data["Indonesia"].values()
    y3 = bar_group_data["Malaysia"].values()
    y4 = bar_group_data["Myanmar"].values()
    y5 = bar_group_data["Philippines"].values()
    y6 = bar_group_data["Singapore"].values()
    y7 = bar_group_data["Thailand"].values()

    x = list(range(11))
    x_3 = [i - 0.3 for i in x]
    x_2 = [i - 0.2 for i in x]
    x_1 = [i - 0.1 for i in x]
    x_plus_3 = [i + 0.3 for i in x]
    x_plus_2 = [i + 0.2 for i in x]
    x_plus_1 = [i + 0.1 for i in x]

    fig = plt.figure()
    width = 0.1
    plt.bar(x_3, y3, width)
    plt.bar(x_2, y2, width)
    plt.bar(x_1, y1, width)
    plt.bar(x, y4, width)
    plt.bar(x_plus_1, y5, width)
    plt.bar(x_plus_2, y6, width)
    plt.bar(x_plus_3, y7, width)

    # creating the bar plot

    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(bar_group_data.keys())
    plt.tight_layout()
    plt.xticks(x, list(bar_group_data["Cambodia"].keys()))
