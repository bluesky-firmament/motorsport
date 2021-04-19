# -*- coding: utf-8 -*-
import csv
import urllib
from bs4 import BeautifulSoup
import pandas as pd
import glob

def export_list_csv(export_list, csv_dir):

    with open(csv_dir, "w") as f:
        writer = csv.writer(f, lineterminator='\n')

        if isinstance(export_list[0], list): #多次元の場合
            writer.writerows(export_list)

        else:
            writer.writerow(export_list)

def get_sec(time_str):
    split_time = time_str.split(':')
    return float(split_time[0]) * 60 + float(split_time[1])

def practice_mode(Rd,drivers):
    print("どのプラクティスから入力しますか?(1 or 2 or 3)")
    practice_number = int(input())
    for Race in range(practice_number,4):
            # print("レースのラップ数を入れてください")
            # Lap_iterator = int(input())
            Lap_iterator = 50
            for driver in drivers:
                i = 0
                lap_list=[driver]
                for Lap in range(Lap_iterator):
                    lap_list.append(None)
                print(lap_list)
                print("公式サイトから" + driver + "のプラクティス" + str(Race) + "のラップタイムをペーストしてください(終了時やもしラップチャートがない場合はcを入力してください")
                while i<100:
                    i = i + 1
                    lap = input()
                    if(lap == "c"):
                        break
                    laptime = input()
                    if((i != 1) & (laptime == "")):
                        break
                    laptime = laptime.lstrip()
                    # print(laptime)
                    try:
                        laptime = get_sec(laptime)
                    except (ValueError,IndexError):
                        continue
                    try:
                        lap_list[i] = laptime
                    except ValueError:
                        continue
                print(lap_list)
                csv_name = "./Rd" + Rd + "_" + "Practice_" + str(Race) + "_" + driver + ".csv"
                export_list_csv(lap_list, csv_name)

def race_mode(Rd,drivers):
    start = 1
    for Race in range(start,2):
        print("レースのラップ数を入れてください")
        Lap_iterator = int(input())
        for driver in drivers:
            i = 0
            lap_list=[driver]
            for Lap in range(Lap_iterator):
                lap_list.append(None)
            print(lap_list)
            print("公式サイトから" + driver + "のレース" + str(Race) + "のラップタイムをペーストしてください(終了時やもしラップチャートがない場合はcを入力してください")
            while i<100:
                i = i + 1
                lap = input()
                if(lap == "c"):
                    break
                laptime = input()
                if((i != 1) & (laptime == "")):
                    break
                laptime = laptime.lstrip()
                # print(laptime)
                try:
                    laptime = get_sec(laptime)
                except (ValueError,IndexError):
                    continue
                try:
                    lap_list[i] = laptime
                except ValueError:
                    continue
            print(lap_list)
            csv_name = "./Rd" + Rd + "_" + "Race_" + str(Race) + "_" + driver + ".csv"
            export_list_csv(lap_list, csv_name)

def auto_mode(Rd):
    drivers = ["Ricciardo","Norris","Vettel","Latifi","Raikkonen","Mazepin","Gasly","Perez","Alonso","Leclerc","Stroll","Tsunoda","Ocon","Verstappen","Hamilton","Shumacher","Sainz","Russell","Bottas","Giovinazzi"]
    # driver = input()
    # print(driver)
    # print("レース?から記録しますか?(1or2or3)")
    # start = int(input())
    print("プラクティス?から記録しますか?(yes or no)")
    practice = input()
    if(practice == "yes"):
        practice_mode(Rd,drivers)
    race_mode(Rd,drivers)

def manual_mode(Rd):
    # Race = input()
    print("ドライバー名を入れてください")
    driver = input()
    drivers = [driver]
    print("プラクティス?から記録しますか?(yes or no)")
    practice = input()
    if(practice == "yes"):
        practice_mode(Rd,drivers)
    race_mode(Rd,drivers)

def main():
    print("ラウンドを入れてください(数字のみ)")
    Rd = input()
    print("Autoモード(ドライバー名が自動で入力されるモード)にする場合はautoと入力してください")
    mode_dicide = input()
    if(mode_dicide == "auto"):
        auto_mode(Rd)
    else:
        manual_mode(Rd)
    
    
if __name__ == "__main__":
    main()