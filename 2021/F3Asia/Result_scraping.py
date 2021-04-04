import csv
import urllib
from bs4 import BeautifulSoup

round = "ROUND_5"

def main():
    list=["QUALIFYING_1","QUALIFYING_2","Race_1","Race_2","Race_3"]
    for item in list:
        url = "https://www.f3asia.com/races/results/2021/" + round
        url += "/" + item + "/"
        if(item == "Race 3"):
            url = "https://www.f3asia.com/races/results/2021/ROUND%201/races/results/"
        try:
            html = urllib.request.urlopen(url)
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.find_all("table")
            for tab in table:
                table_className = tab.get("class")
                if table_className[0] == "table1":
                    break
            name = item.replace('%20','_')
            csvname = round + "_" + name + ".csv"
            for tab in table:
                table_className = tab.get("class")
                if table_className[0] == "table1":
                    with open(csvname, "w", encoding='utf-8',newline="") as file:
                        writer = csv.writer(file)
                        rows = tab.find_all("tr")
                        for row in rows:   
                            csvRow = []
                            for cell in row.findAll(['td', 'th']):
                                try:
                                    element = str(cell.contents[0])
                                    csvRow.append(element.replace('/',','))
                                except IndexError:
                                    continue
                            del csvRow[2]
                            integration = ','.join(csvRow)
                            degration = integration.split(',')
                            writer.writerow(degration)
                    break
        except:
            continue

if __name__ == "__main__":
    main()