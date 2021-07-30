import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd

df = pd.read_csv("./csv_data/School2.csv")
data = df["Math_score"].tolist()

def random_set_of_means(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0, 1000):
    set_of_means = random_set_of_means(100)
    mean_list.append(set_of_means)

standard_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("Mean of Sampling Distribution is: ", mean)
print("Standard Deviation of Sampling Distribution is: ", standard_deviation)

first_std_deviation_start, first_std_deviation_end = mean - standard_deviation, mean + standard_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2 * standard_deviation), mean + (2 * standard_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3 * standard_deviation), mean + (3 * standard_deviation)

df = pd.read_csv("./csv_data/School_1_Sample.csv")
data = df["Math_score"].tolist()

meanOfSample1 = statistics.mean(data)
print("Mean of Sample 1:- ", meanOfSample1)

fig = ff.create_distplot([mean_list], ["student marks"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meanOfSample1, meanOfSample1], y=[0, 0.17], mode="lines", name="MEAN OF STUDENTS WHO HAD MATH LABS"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END"))
fig.show()

z_score = (mean - meanOfSample1) / standard_deviation
print("The Z Score is:- ", z_score)