# -*- coding: utf-8 -*-
import csv
import urllib
from bs4 import BeautifulSoup

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

def auto_mode(Rd):
    drivers = ["Ricciardo","Norris","Vettel","Latifi","Raikkonen","Gasly","Perez","Alonso","Leclerc","Stroll","Tsunoda","Ocon","Verstappen","Hamilton","Shumacher","Sainz","Russell","Bottas","Giovinazzi"]
    # driver = input()
    # print(driver)
    # print("レース?から記録しますか?(1or2or3)")
    # start = int(input())
    print("プラクティス?から記録しますか?(yes or no)")
    practice = input()
    if(practice == "yes"):
        start = 1
        for Race in range(start,4):
            # print("レースのラップ数を入れてください")
            # Lap_iterator = int(input())
            Lap_iterator = 100
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


def main():
    print("ラウンドを入れてください(数字のみ)")
    Rd = input()
    print("Autoモード(ドライバー名が自動で入力されるモード)にする場合はautoと入力してください")
    mode_dicide = input()
    if(mode_dicide == "auto"):
        auto_mode(Rd)
    else:
        # Race = input()
        print("ドライバー名を入れてください")
        driver = input()
        # print(driver)
        for Race in range(1,4):
            print("レース" + str(Race) + "のラップ数を入れてください")
            Lap_iterator = int(input())
            lap_list=[driver]
            for Lap in range(Lap_iterator):
                lap_list.append(None)
            print(lap_list)
            i = 0
            print("公式サイトから" + driver + "のレース" + str(Race) + "のラップタイムをペーストしてください(終了時やもしラップチャートがない場合はcを入力してください")
            while i<Lap_iterator:
                i = i + 1
                lap = input()
                if(lap == "c"):
                    break
                laptime = input()
                if((i > 1) & (laptime == "")):
                    break
                laptime = laptime.lstrip()
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

    
if __name__ == "__main__":
    main()