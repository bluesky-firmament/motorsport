# coding: utf-8
import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import numpy as np
import math

def plot(drivername,driver_lap,lap_number,round,race,iteration):

    npdriver_lap = np.array(driver_lap)
    npnumber_lap = np.array(lap_number)
    try:
        npdriver_lap = np.nan_to_num(npdriver_lap, nan=np.nanmean(npdriver_lap))
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
        
        if(iteration == 1):
            plt.plot(input_lap_data, predicted, color = 'blue',label=drivername)
            plt.scatter(lap_number,driver_lap, color = 'blue',label=drivername)
            plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=12)
        if(iteration == 2):
            plt.plot(input_lap_data, predicted, color = 'red',label=drivername)
            plt.scatter(lap_number,driver_lap, color = 'red',label=drivername)
            plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=12)
        if(iteration == 3):
            plt.plot(input_lap_data, predicted, color = 'green',label=drivername)
            plt.scatter(lap_number,driver_lap, color = 'green',label=drivername)
            plt.legend(bbox_to_anchor=(1, 1), loc='upper left', borderaxespad=0, fontsize=12)
        title = "Drivers_Race" + race + "_RacePace"
        plt.title(title)
        formula = drivername + ":y="+ coef + "+" + intercept
        plt.text(40, 100 + iteration * 0.5, formula, size=10)
        plt.ylim(77.5,100)
        plt.grid(color='r', linestyle='dotted', linewidth=1)
        figure_name = "Rd" + str(round) + "/Drivers_Race" + race + "_RacePace.png"
        plt.savefig(figure_name)
        # plt.show()
    except (ValueError,IndexError):
        return
    

# プロットするドライバーを選択
drivers = ["Mazepin","Shumacher"]
# drivers = ["Gasly","Stroll","Raikkonen"]
print("ラウンド数を入れてください")
round = int(input())
print("レース数を入れてください")
race = input()
file_name = 'Rd' + str(round) + '_Race_' + race + '_total.csv'
f = open(file_name,'r')
reader = csv.reader(f)
lap_number=[]
drivername = []
lap_time = []
iteration = 0
fig = plt.figure(figsize=(16, 8))
for row in reader:
    # print(row)
    if(iteration == 0):
        lap_number = [int(lap) for lap in row[1:]]
        print(lap_number)
        iteration += 1
    if(iteration != 0):
        lap_time = []
        if( row[0] in drivers ):
            drivername.append(row[0])
            for lap in row[1:]:
                try:
                    lap_time.append(float(lap))
                except (ValueError,IndexError):
                    lap_time.append(math.nan)
            # print(len(lap_time))
            # print(len(lap_number))
            plot(row[0],lap_time,lap_number,round,race,iteration)
    if( row[0] in drivers ):
        iteration += 1
            # break
    
print(drivername)
f.close()
