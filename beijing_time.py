from lxml import etree
import requests
class BeijingTime(object):
    def __init__(self):
        self.headers= {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    "connection": "keep-alive",
    "cookie": "Hm_lvt_a2740af6d9c917df3466091dae04fd26=1758971707; Hm_lpvt_a2740af6d9c917df3466091dae04fd26=1758971707; HMACCOUNT=B5BDE13816DA4E63",
    "host": "time.syiban.com",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
}
        self.url="http://time.syiban.com/"

    def get_time(self):
        response = requests.get(self.url, headers=self.headers)
        time_page=etree.HTML(response.text)
        time=time_page.xpath("//div[@class='time']/text()")
        return time[0]
    def get_date(self):
        response = requests.get(self.url, headers=self.headers)
        date_page=etree.HTML(response.text)
        date=date_page.xpath("//div[@class='date']/text()")
        return date[0]

if __name__ == '__main__':
    beijing_time=BeijingTime()
    print(beijing_time.get_time())
    print(beijing_time.get_date())