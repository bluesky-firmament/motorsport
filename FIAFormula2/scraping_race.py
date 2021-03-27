import csv
import urllib
from bs4 import BeautifulSoup
url = "https://fiaresultsandstatistics.motorsportstats.com/series/fia-formula-3-championship"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
# HTMLから表(tableタグ)の部分を全て取得する
table = soup.find_all("table")
for tab in table:
    table_className = tab.get("class")
    print(table_className)
    if table_className[0] == "_2Q90P":
        break
div_all = soup.find_all("div")
for div_one in div_all:
    # print(div_one)
    div_className = div_one.get("class")
    if div_className[0] == "_1BvfV":
        print(div_className[0])
        break
# break文がないときの出力結果
# ['vertical-navbox', 'nowraplinks', 'hlist']
# ['wikitable'] <- ここで,break文を使って抜ける
# ['wikitable', 'sortable']
# ['wikitable', 'sortable']
# ['wikitable']
# ['nowraplinks', 'mw-collapsible', 'autocollapse', 'navbox-inner']
for tab in table:
    table_className = tab.get("class")
    if table_className[0] == "_2Q90P":
        # CSV保存部分
        with open("test.csv", "w", encoding='utf-8') as file:
            writer = csv.writer(file)
            rows = tab.find_all("tr")
            for row in rows:
                csvRow = []
                print(row.get_text())
                for cell in row.findAll(['td', 'th']):
                    csvRow.append(cell.get_text())
                    print(cell.get_text())
        break