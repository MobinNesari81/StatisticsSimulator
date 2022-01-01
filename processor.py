# Statistics simulation program. Design and Developed by: Mobin Nesari 99222107
# Import required libraries:
import math
import random

import pylab
from bokeh.plotting import figure, show
import numpy as np
import collections
import matplotlib.pyplot as plt


# The probability density function which I used in this this simulation is f(x) = 1/(2*sqrt(15)) * 1/sqrt(x)
# If we integrate both sides then F(x) = sqrt(x/15) and inverse of cumulative distribution function is F^-1(x) = 15*x^2

def random_number_generator(counter: int) -> list:  # This function generate random numbers in interval [0,1)
    numbers = []
    for i in range(counter):
        numbers.append((random.random() + 0.0000001) % 1)
    return numbers


def random_number_generator_mk2(counter: int):
    numbers = np.linspace(0.0, 1.0, counter, endpoint=True)
    return numbers


def random_number_generator_mk3(counter: int):
    numbers = np.random.uniform(0, 1, counter)
    return numbers


def random_number_generator_mk4(counter: int):
    zone = counter // 15
    numbers = []
    for i in range(0, 15):
        for j in range(zone):
            k = random.uniform(math.sqrt(i / 15), math.sqrt((i + 1) / 15))
            if probability_density_function(inverse_cumulative_function(k)) <= 1:
                numbers.append(k)
            else:
                j -= 1

    return numbers


def cumulative_function(x: float) -> float:  # Cumulative function: [0,15] -> [0,1]
    return math.sqrt(x / 15)


def inverse_cumulative_function(x: float) -> float:  # Inverse cumulative function: [0,1] -> [0,15]
    return 15 * x ** 2


def probability_density_function(x: float) -> float:  # Probability density function  (0,15] -> [0,1]
    return (1 / (2 * math.sqrt(15))) * (1 / math.sqrt(x))


def generate_artificial_data(length: int) -> list:  # Creating some numbers which we can use for simulation.
    array = random_number_generator_mk4(length)
    data = [inverse_cumulative_function(i) for i in array]
    return data


def distribution_test(array: list) -> collections.defaultdict:
    answer = collections.defaultdict()
    for i in range(0, 16):
        k = 0
        for j in array:
            if i <= j < i + 1:
                k += 1
        answer[i] = k
    return answer


def plotter(x: list, y: list) -> None:  # Plotting data
    p = figure(title="Histogram of random data", x_axis_label='x', y_axis_label='y')
    p.line(x, y, legend_label="Temp.", line_width=2)
    show(p)


def histogram_plotter(array: list, figure_name="histogram") -> None:
    fig = pylab.gcf()
    fig.canvas.manager.set_window_title(figure_name)
    plt.hist(array)
    plt.show()


def expected_value_computer(density: list, data: list) -> float:
    answer = 0
    for i in range(len(density)):
        answer += density[i] * data[i]
    answer /= len(density) / 15
    return answer


def second_order_expected_value(density: list, data: list) -> float:
    answer = 0
    for i in range(len(density)):
        answer += density[i] * data[i] ** 2
    answer /= len(density) / 15
    return answer


def variance_computer(density: list, data: list) -> float:
    answer = second_order_expected_value(density, data) - expected_value_computer(density, data) ** 2
    return answer


def mean_data_generator(repeat_time: int, data_length: int) -> list:
    answer = []
    for i in range(repeat_time):
        arr = generate_artificial_data(data_length)
        answer.append(sum(arr)/data_length)
    return answer


def means_expected_value_computer(means: list) -> float:
    answer = 0
    for i in means:
        answer += i * means.count(i)/len(means)
    return answer


def means_second_order_expected_value(means: list) -> float:
    answer = 0
    for i in means:
        answer += (i ** 2) * (means.count(i)/len(means))
    return answer


def means_variance(means: list) -> float:
    answer = means_second_order_expected_value(means) - means_expected_value_computer(means) ** 2
    return answer
