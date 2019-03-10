from bs4 import BeautifulSoup
import requests
import csv
import pymysql

db = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="123", db="langtai", charset='utf8')
cursor = db.cursor()
page = 0
csv_file = open("rent_bk.csv", "w")
csv_writer = csv.writer(csv_file, delimiter=",")
print("==============================房屋信息查询系统========================")
print("按地铁站查找，请输入1；按区查找，请输入2")
p = int(input("选择查找方式："))

if p == 1:
    url = "https://bj.zu.ke.com/ditiezufang/li46461179/pg{page}rt200600000002brp{min}erp{max}"
else:
    url = "https://bj.zu.ke.com/zufang/{district}/rt20060002brp{min}erp{max}"
    district = input("请输入查找区域的拼音：")
min = input("输入您期望的最小价格：")
max = input("输入您期望的最大价格：")

while True:
    page += 1
    if p == 1:
        print("正在爬取贝客网的数据:   " + url.format(page=page, min=min, max=max))
        response = requests.get(url.format(page=page, min=min, max=max))
    else:
        print("正在爬取贝客网的数据:   " + url.format(page=page, district=district, min=min, max=max))
        response = requests.get(url.format(page=page, district=district, min=min, max=max))
    html = BeautifulSoup(response.text, "html.parser")
    house_list = html.select(".content__list > .content__list--item")
    if not house_list:
        break

    for house in house_list:
        house_title = house.select(".content__list--item--main")[0].select("p")[0].select("a")[0].string.strip()
        house_price = house.select(".content__list--item-price")[0].select("em")[0].string
        house_location1 = house.select(".content__list--item--des")[0].select("a")[0].string
        house_location2 = house.select(".content__list--item--des")[0].select("a")[1].string
        house_location = house_location1 + "-" + house_location2
        house_url_suffix = house.select("a")[0]["href"]
        house_url = "https://bj.zu.ke.com" + house_url_suffix
        house_info_list = house_title.split()
        house_info = house_info_list[2] + "-" + house_info_list[3]
        csv_writer.writerow([house_info, house_location, house_price, house_url])
        sql = "INSERT INTO house_info_bk VALUES('{house_info}','{house_location}','{house_price}','{house_url}')" \
            .format(house_info=house_info, house_location=house_location, house_price=house_price, house_url=house_url)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

csv_file.close()
db.close()
