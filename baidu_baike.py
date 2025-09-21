import requests
from lxml import etree
from urllib.parse import quote


class BaiDuBaiKe(object):
    def __init__(self,):

        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "zh-CN,zh;q=0.9",
            "connection": "keep-alive",
            "cookie": "BIDUPSID=D1484585C7AE625A866120CF4E28B3B0; PSTM=1751276752; BAIDUID=7D71A4407D68A73FF911120DD0E4B74C:FG=1; MAWEBCUID=web_DhblMqwKALvRxEbQHZdPghTpmCQlUCmNDQfRqMQLhlBQrQzBjR; BDUSS=kxlcmphdVJ0NWFMQkFJMXpteEI4Y2FMa34zdEtyNVVHdkdRQlZ0cEp6UjZCYmhvSVFBQUFBJCQAAAAAAAAAAAEAAABbpKjOZ2FvMTM1MTczMjU2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHp4kGh6eJBoM; BDUSS_BFESS=kxlcmphdVJ0NWFMQkFJMXpteEI4Y2FMa34zdEtyNVVHdkdRQlZ0cEp6UjZCYmhvSVFBQUFBJCQAAAAAAAAAAAEAAABbpKjOZ2FvMTM1MTczMjU2MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHp4kGh6eJBoM; channel=baidusearch; BAIDUID_BFESS=7D71A4407D68A73FF911120DD0E4B74C:FG=1; ZFY=rmDHyrQ7JrrYi8QSY24ZodFTz84NuVqcSVqNx3E7dpE:C; RT=\"z=1&dm=baidu.com&si=f6a35e50-1387-455d-8dce-e13bb198f82b&ss=mfezuyea&sl=1&tt=ajn&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=bbq&ul=4ebz&hd=4ec7\"; BA_HECTOR=058000840g058k2481a40g800g040g1kcj5oj24; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; __bid_n=1995389357b49921068f7b; H_PS_PSSID=63143_63326_63947_64559_64654_64752_64696_64811_64815_64841_64868_64875_64910_64966_64974_65077_65087_65122_65141_65138_65139_65189_65204_65222_65242_65257_65143_65275_65325; delPer=0; PSINO=3; H_WISE_SIDS=63143_63326_63947_64559_64654_64752_64696_64811_64815_64841_64868_64875_64910_64966_64974_65077_65087_65122_65141_65138_65139_65189_65204_65222_65242_65257_65143_65275_65325; zhishiTopicRequestTime=1758083630906; baikeVisitId=c31492ec-4ae3-4682-9b23-ccbd21f5ffbe; ab_sr=1.0.1_M2U4ZjQxZDJiMDgzMjg1M2YxOTk4MDg1MTFmNDdlNzRmZTk5MDA3NDQ2ZDQwZDhhZTM1ZTQ4YzdiYzlmZGMxNjNjOTJmZDg2YTlkM2JjOGMzNDZmZDQxMGFhODg3MDAwMjg3MzE1NjM1NjhlM2MwNWFhZGYzZDJiY2NjOTg3MTExODNmN2RiNDRmNDNiOTdhMTc3ZmRlZTZmMGYyODFjNGQ2Yjg1ODgzYWRmYWEwZmM2MTk2Y2I1YTBjNWVjMzkyNmE4Yjg1NzNiMzFhYTk0YmY2ZmNkMTNlNGZiNDEzNTI=",
            "host": "baike.baidu.com",
            "referer": "https://baike.baidu.com/item/%E8%92%82%E5%A7%86%C2%B7%E5%BA%93%E5%85%8B/4576793?fromtitle=%E5%BA%93%E5%85%8B&fromid=35535",
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
        self.payload= {
            "fromModule": "lemma_search-box"
        }
    def chinese_to_utf8(self,chinese_str):
        if not isinstance(chinese_str, str):
            raise ValueError("输入必须是字符串类型")

        # 使用quote函数进行UTF-8编码，safe参数确保不编码ASCII字符
        return quote(chinese_str, safe='')
    def resp(self,utf8_encoded):
        url = f"https://baike.baidu.com/item/{utf8_encoded}?fromModule=lemma_search-box"
        response=requests.get(url, headers=self.headers,params=self.payload)
        message_page=etree.HTML(response.text)
        message=message_page.xpath('//meta[@name="description"]/@content')
        return message

if __name__ == '__main__':
    search=BaiDuBaiKe()
    utf8=search.chinese_to_utf8("张俊豪")
    resp=search.resp(utf8)
    print(resp)