import csv
import urllib
from bs4 import BeautifulSoup
def main():
    # url = "https://www.f3asia.com/races/results/2021/ROUND_1/"
    print("URLを入れてください")
    url = input()
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all("table")
    for tab in table:
        table_className = tab.get("class")
        if table_className[0] == "_2Q90P":
            break
    print("ファイル名を打ち込んでください")
    name = input()
    csvname = name + ".csv"
    for tab in table:
        table_className = tab.get("class")
        if table_className[0] == "_2Q90P":
            with open(csvname, "w", encoding='utf-8',newline="") as file:
                writer = csv.writer(file)
                rows = tab.find_all("tr")
                for row in rows:   
                    csvRow = []
                    for cell in row.findAll(['td', 'th']):
                        try:
                            # element = str(cell.contents[0])
                            # csvRow.append(element.replace('/',','))
                            csvRow.append(cell.get_text())
                        except IndexError:
                            continue
                    # integration = ','.join(csvRow)
                    # degration = integration.split(',')
                    # writer.writerow(degration)
                    writer.writerow(csvRow)
            break

if __name__ == "__main__":
    main()