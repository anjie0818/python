import requests

def to_get():

    resp = requests.get("http://www.baidu.com")
    print(resp)

def to_get_header_data():

    kw = {'wd': '长城'}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get("http://www.baidu.com/s?", params=kw, headers=headers)
    print(response)
    print(response.text)# unicode数据
    print(response.content)# 字节流
    print(response.encoding)

def to_text_vs_content():
    response = requests.get("http://www.sina.com")
    print(response.request.headers)
    print(response.content.decode())
    print(response.encoding)
    print("*"*100)
    response = requests.get("http://www.sina.com")
    print(response.request.headers)
    print(response.text)
    print(response.encoding)

def to_post():
    formdata = {
        "type": "AUTO",
        "i": "i love python",
        "doctype": "json",
        "xmlVersion": "1.8",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_ENTER",
        "typoResult": "true"
    }

    url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}

    response = requests.post(url, data=formdata, headers=headers)

    print(response.text)

    # 如果是json文件可以直接显示
    print(response.json())

def to_proxy():

    # 根据协议类型，选择不同的代理
    proxies = {
        "http": "http://118.190.95.43:9001",
        "https": "http://118.190.95.43:9001",
    }

    response = requests.get("http://www.baidu.com",stream=True,proxies= proxies)
    print(response.raw._connection.sock.getpeername()[0])

    print(response.request.headers)

if __name__ == '__main__':

    #to_get()
    #to_get_header_data()
    #to_text_vs_content()
    #to_post()
     to_proxy()
