# coding: utf-8
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import numpy as np


def plot(drivername,driver_lap,lap_number,round):
    fig = plt.figure(figsize=(12, 8))
    npdriver_lap = np.array(driver_lap)
    npnumber_lap = np.array(lap_number)
    c_min, c_max = np.percentile(npdriver_lap, [0, 80])
    print(c_min,c_max,npdriver_lap.min())
    npdriver_lap = np.clip(npdriver_lap, c_min, c_max)
    input_driver_data = npdriver_lap.reshape(-1,1)
    input_lap_data = npnumber_lap.reshape(-1,1)
    # print(input_lap_data)
    model = LinearRegression()
    model.fit(input_lap_data, input_driver_data)
    intercept = str(model.intercept_)
    coef = str(model.coef_)
    predicted = model.predict(input_lap_data)
    plt.scatter(lap_number,driver_lap)
    plt.plot(input_lap_data, predicted, color = 'blue')
    title = drivername + "_Race_Pace"
    plt.title(title)
    formula = "y="+ coef + "+" + intercept
    plt.text(40, 100, formula, size=10)
    plt.ylim(60.0,120.0)
    figure_name = "Rd" + str(round) + "/" + drivername + "_Race_Pace.png"
    plt.savefig(figure_name)
    # plt.show()


f = open('Rd2_Race_1_total.csv','r')
reader = csv.reader(f)
print("ラウンド数を入れてください")
round = int(input())
lap_number=[]
drivername = []
lap_time = []
iteration = 0
for row in reader:
    # print(row)
    if(iteration == 0):
        lap_number = [int(lap) for lap in row[1:]]
        print(lap_number)
    if(iteration != 0):
        lap_time = []
        drivername.append(row[0])
        for lap in row[1:]:
            try:
                lap_time.append(float(lap))
            except (ValueError,IndexError):
                lap_time.append(0.0)
        # print(len(lap_time))
        # print(len(lap_number))
        plot(row[0],lap_time,lap_number,round)
        # break
    iteration = iteration + 1
print(drivername)
f.close()
