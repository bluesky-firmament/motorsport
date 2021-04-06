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
    m, s = time_str.split(':')
    return int(m) * 60 + s


def main():
    print("ラウンドを入れてください(数字のみ)")
    Rd = input()
    print("何レースを入れてください(数字のみ)")
    Race = input()
    print("ドライバー名を入れてください")
    driver = input()
    print(driver)
    i = 1
    lap_list = [driver]
    print("公式サイトからラップタイムをペーストしてください")
    while i<100:
        lap = input()
        laptime = input()
        if((i != 1) & (laptime == "")):
            break
        laptime = laptime.lstrip()
        laptime = get_sec(laptime)
        try:
            lap_list.append(laptime)
        except ValueError:
            break
        i = i + 1
    print(lap_list)
    csv_name = "./Rd" + Rd + "_Race" + "Race_" + driver + ".csv"
    export_list_csv(lap_list, csv_name)

    
if __name__ == "__main__":
    main()