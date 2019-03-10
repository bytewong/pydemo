from bs4 import BeautifulSoup
import requests
import csv
import pymysql

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123", db="langtai", charset='utf8')
cursor = db.cursor()
url = "http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=1500_2000"

page = 0

csv_file = open("rent.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print("fetch:   ", url.format(page=page))
    response = requests.get(url.format(page=page))
    html = BeautifulSoup(response.text, "html.parser")
    house_list = html.select("ul.list > li")
    # print(house_list)
    if not house_list:
        break

    for house in house_list:
        house_title = house.select("h2")[0].string
        house_url = house.select("a")[0]["href"][2:]
        house_info_list = house_title.split()
        house_location = house_info_list[1]
        house_money = house.select(".money")[0].select("b")[0].string
        csv_writer.writerow([house_title, house_location, house_money, house_url])
        sql = "INSERT INTO house_info VALUES" \
              "('{house_title}','{house_location}','{house_money}','{house_url}')" \
            .format(house_title=house_title, house_location=house_location, house_money=house_money,
                    house_url=house_url)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
db.close()
csv_file.close()
