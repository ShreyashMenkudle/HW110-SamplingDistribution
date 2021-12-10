import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import random
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["reading_time"].to_list()

def show_fig(mean_list): 
    df = mean_list 
    mean = statistics.mean(df) 
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False) 
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN")) 
    fig.show()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)

    return mean

def setup():
    mean_list = []
    for i in range(1,30):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Sampling Distribution",mean)

setup()


claps_mean = statistics.mean(data)
print("Reading time mean:-",claps_mean)

claps_SD = statistics.stdev(data)
print("Reading time standard deviation:-",claps_SD)

def standard_deviation(): 
    mean_list = [] 
    for i in range(0,1000): 
        set_of_means= random_set_of_mean(100) 
        mean_list.append(set_of_means) 
    std_deviation = statistics.stdev(mean_list) 
    print("Standard deviation of sampling distribution:- ", std_deviation) 
standard_deviation()