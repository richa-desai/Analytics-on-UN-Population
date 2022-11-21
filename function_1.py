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
    y_values = []
    for idx, country in enumerate(["Cambodia","Indonesia","Malaysia","Myanmar",
                    "Philippines","Singapore","Thailand"]):
        y_values.append([])
        for year in range(2004, 2015, 1):
            y_values[idx].append(bar_group_data[country][year])

    x_values = []
    for i in [-0.3, -0.2, -0.1, 0, 0.1, 0.2, 0.3]:
        x_values.append([j + i for j in range(11)])

    fig = plt.figure()
    width = 0.1

    # creating the bar plot
    for i in range(len(bar_group_data)):
        plt.bar(x_values[i], y_values[i], width)

    fig.autofmt_xdate()  # gives rotation to the x axis titles
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend(bar_group_data.keys())
    plt.tight_layout()
    plt.xticks(x_values[3], list(bar_group_data["Cambodia"].keys()))
