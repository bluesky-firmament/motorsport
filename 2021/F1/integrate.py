import pandas as pd
import glob
import csv

print("ラウンドを入れてください(数字のみ)")
Rd = input()
csv_files = glob.glob("Rd" + Rd + '/*.csv')

#読み込むファイルのリストを表示
for a in csv_files:
    print(a)

#csvファイルの中身を追加していくリストを用意
practice_1_data_list = []
practice_2_data_list = []
practice_3_data_list = []
race_1_data_list = []

#読み込むファイルのリストを走査
for file in csv_files:
    # if('Practice_1' in file):
    #     practice_1_data_list.append(pd.read_csv(file,header=None))
    # if('Practice_2' in file):
    #     practice_2_data_list.append(pd.read_csv(file,header=None))
    # if('Practice_3' in file):
    #     practice_3_data_list.append(pd.read_csv(file,header=None))
    if('Race_1' in file):
        race_1_data_list.append(pd.read_csv(file,header=None))
#リストを全て行方向に結合
#axis=0:行方向に結合, sort
# df = pd.concat(practice_1_data_list, axis=0, sort=True)
# df.to_csv("./Rd" + Rd + "_pratice_1_total" + '.csv',index=False)
# df = pd.concat(practice_2_data_list, axis=0, sort=True)
# df.to_csv("./Rd" + Rd + "_pratice_2_total" + '.csv',index=False)
# df = pd.concat(practice_3_data_list, axis=0, sort=True)
# df.to_csv("./Rd" + Rd + "_pratice_3_total" + '.csv',index=False)
df = pd.concat(race_1_data_list, axis=0, sort=True)
df.to_csv("./Rd" + Rd + "_Race_1_total" + '.csv',index=False)