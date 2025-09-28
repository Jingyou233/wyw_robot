import requests
from lxml import etree
class Area(object):
    def __init__(self):
        self.area ={
        "五河":"101220204",
        "蚌埠":"101220201",
        "芜湖":"101220301",
        "洛阳": "101220104",
        "宜阳": "101180904",
        "铜陵": "101221301",
        "合肥": "101220101",
        "杭州": "101210101",
        "义乌": "101210904",
        "宣城": "101221401",
        "肥东": "101220103",
        "宿州": "101220701",
        "淮南": "101220401",
        "阜阳": "101220801",
        "安庆": "101220601",
        "上海": "101020100"
}
        self.headers = {
            "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7": "accept-encoding",
            "gzip,": "deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9",
            "connection": "keep-alive",
            "cookie": "sessionId=uniqueSessionIdValue; Hm_lvt_080dabacb001ad3dc8b9b9049b36d43b=1758988958; HMACCOUNT=B5BDE13816DA4E63; defaultCty=101200101; userNewsPort0=1; defaultCtyName=%u6B66%u6C49; f_city=%E6%AD%A6%E6%B1%89%7C101200101%7C; Hm_lpvt_080dabacb001ad3dc8b9b9049b36d43b=1758990032",
            "host": "www.weather.com.cn",
            "referer": "https://www.weather.com.cn/weather1d/101220201.shtml",
            "sec-ch-ua": "\"Chromium\";v=\"140\", \"Not=A?Brand\";v=\"24\", \"Google Chrome\";v=\"140\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
        }
    def area_name(self,area_id):
        return(self.area[area_id])
    def get_area(self,area_num):
        url = f"https://www.weather.com.cn/weather/{area_num}.shtml"
        resp=requests.get(url,headers=self.headers)
        resp.encoding = "utf-8"
        area_page=etree.HTML(resp.text)
        weather=area_page.xpath("//ul[@class='t clearfix']/li")
        weather_content=[]

        for wea in weather:
            date=wea.xpath("./h1/text()")
            thing = wea.xpath("./p[@class='wea']/text()")
            temp=wea.xpath("./p[@class='tem']/i/text()")
            weather_content.append([date[0],thing[0],temp[0]])


        return weather_content


if __name__ == '__main__':
    area=Area()

