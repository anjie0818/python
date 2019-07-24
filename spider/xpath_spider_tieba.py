import requests, json
from lxml import etree

class Tieba(object):
    def __init__(self,search_name):

        self.search_name = search_name
        # 设置为手机端的UA
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"}

    def get_urls(self):
        '''获取url列表'''

        url_model = "http://tieba.baidu.com/f?kw="+self.search_name+"&ie=utf-8&pn={}"
        url_list = []
        for i in range(2):
            url_list.append(url_model.format(i*50))
        return url_list

    def do_post(self, url):
        '''一个发送请求，获取响应，同时etree处理html'''
        response = requests.get(url, headers=self.headers)
        html = response.content.decode()
        return etree.HTML(html)

    def get_title_href(self,html):
        '''获取返回html中的title和href'''
        li_temp_list = html.xpath('//*[@id="frslistcontent"]/li')  # 分组，按照li标签分组
        total_items = []
        for i in li_temp_list:
            href = "https://tieba.baidu.com"+i.xpath("./a/@href")[0] if (len(i.xpath("./a/@href"))>0 and (i.xpath("./a/@href")[0])!="javascript:;") else None
            text = i.xpath("./a/div[1]/span[1]/text()")
            text = text[0] if len(text) > 0 else None
            item = dict(  # 放入字典
                href=href,
                text=text
            )
            if href:
                total_items.append(item)
        return total_items

    def run(self):
        '''运行脚本'''

        # url拼接，得到url列表
        urls = self.get_urls()
        # 遍历url，使用etree处理返回，xpath提取文本+url
        for url in urls:
            html = self.do_post(url)
            total_item = self.get_title_href(html)
            # 遍历获取每个标题下的图片集合
            for item in total_item:
                href = item["href"]
                img_list = self.get_images(href)
                item["img"] = img_list
                # 4、保存到本地
                self.save_item(item)

    def get_images(self,url):
        html = self.do_post(url)
        img_list = html.xpath('//div[@class="pb_img_item"]//@data-url')
        img_list = [i.split("src=")[-1] for i in img_list]  # 提取图片的url
        img_list = [requests.utils.unquote(i) for i in img_list]
        return img_list
    def save_item(self, item):
        print(item)
        with open("teibatupian.txt","a") as f:
            f.write(json.dumps(item,ensure_ascii=False,indent=2))
            f.write("\n")

if __name__ == '__main__':

    tieba = Tieba("猫")
    # tieba.run()
