import requests, re

class Duanzi_spider(object):

    def __init__(self):

        self.url = "http://www.neihan8.com/article/list_5_%s.html"
        self.headers = {
            "User_Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleW\
                    ebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
            "Accept-Encoding": None,
            "Accept-Language": "zh-CN,zh;q=0.8"
        }

    def load_page(self, url):

        resp = requests.get(url, timeout=300, headers=self.headers)
        if resp.status_code == 200:
            print(resp.request.headers)
            return resp.content.decode("gbk")
        else:
            raise ValueError("status_code is:",resp.status_code)


    def get_content(self,html):
        # 这里需要注意一个是re.S是正则表达式中匹配的一个参数。
        #
        # 如果
        # 没有re.S
        # 则是
        # 只匹配一行
        # 有没有符合规则的字符串，如果没有则下一行重新匹配。
        #
        # 如果
        # 加上re.S
        # 则是将
        # 所有的字符串
        # 将一个整体进行匹配，findall
        # 将所有匹配到的结果封装到一个list中。
        pattern = re.compile(r'<a\shref="/article/\d+\.html">(.*?)</a>.*?<div\sclass="f18 mb20">(.*?)</div>', re.S)
        t = pattern.findall(html)
        result = []
        for i in t:
            temp = []
            for j in i:
                j = re.sub(r"[<b>|</b>|<br />|<br>|<p>|</p>|\\u3000|\\r\\n|\s]", "", j)
                j = j.replace("&ldqo;", '"').replace("&helli;", "...").replace("&dqo;", '"').strip()
                temp.append(j)
            result.append(temp)
        return result

    def save_content(self, content):
        myFile = open("./duanzi.txt", 'a')
        for temp in content:
            myFile.write("\n" + temp[0] + "\n" + temp[1] + "\n")
            myFile.write("-----------------------------------------------------")
        myFile.close()

    def run(self):
        for i in range(1,506):
            page_html = self.load_page(self.url%i)
            content = self.get_content(page_html)
            self.save_content(content)

if __name__ == '__main__':

    ds = Duanzi_spider()
    ds.run()