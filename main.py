import processor
import matplotlib.pyplot as plt

# Constants:
length = 10000
repeat_time = 1000

new_data = processor.generate_artificial_data(length)
processor.histogram_plotter(new_data, "Artificial Data Histogram")

density = [processor.probability_density_function(i) for i in new_data]
expected_value = processor.expected_value_computer(density, new_data)
print("Expected value: ", expected_value)

second_order_expected_value = processor.second_order_expected_value(density, new_data)
print("Second order expected value: ", second_order_expected_value)

variance = processor.variance_computer(density, new_data)
print("Variance: ", variance)

means = processor.mean_data_generator(repeat_time, length)
processor.histogram_plotter(means, "Means of Data Histogram")

means_expected_value = processor.means_expected_value_computer(means)
print("Means expected value: ", means_expected_value)

means_second_order_expected_value = processor.means_second_order_expected_value(means)
print("Means second order expected value: ", means_second_order_expected_value)

means_variance = processor.means_variance(means)
print("Means variance: ", means_variance)


