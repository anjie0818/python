# 爬虫
## python原理和数据抓取
### 通用爬虫和聚焦爬虫
#### 通用爬虫
通用网络爬虫 是 捜索引擎抓取系统（Baidu、Google、Yahoo等）的重要组成部分。主要目的是将互联网上的网页下载到本地，形成一个互联网内容的镜像备份。
#### 聚焦爬虫
聚焦爬虫，是"面向特定主题需求"的一种网络爬虫程序，它与通用搜索引擎爬虫的区别在于： 聚焦爬虫在实施网页抓取时会对内容进行处理筛选，尽量保证只抓取与需求相关的网页信息。
### str和bytes区别
* bytes对象只负责以二进制字节序列的形式记录所需记录的对象，至于该对象到底表示什么（比如到底是什么字符）则由相应的编码格式解码所决定
* python2 VS python3
    * bytes是Python 3中特有的，Python 2 里不区分bytes和str。
    * 互联网使用二进制传输，python3需要将str转换成bytes进行传输，而在接收中通过decode()解码成我们需要的编码进行处理数据
* bytes VS bytearray
    * bytearray和bytes不一样的地方在于，bytearray是可变的。

### Requests 使用
[跳转脚本](request_test.py)
> requests 的底层实现其实就是 urllib   
开源地址：https://github.com/kennethreitz/requests   
中文文档 API： http://docs.python-requests.org/zh_CN/latest/index.html

* 安装：pip install requests   
* 优点
    * 底层实现urlib
    * python2/python3通用
    * 简单易用
    * 自动解压（gzip等）压缩等网页
* 使用：
    * response = requests.get(url)
    * 常用方法：
        * response.text
        * response.content
        * response.status_code
        * response.request.headers
        * response.headers
    * 返回数据的编码和解码
        ```
        response.text
        类型：str
        解码类型： 根据HTTP 头部对响应的编码作出有根据的推测，推测的文本编码
        如何修改编码方式：response.encoding=”gbk”
        
        response.content
        类型：bytes
        解码类型： 没有指定
        如何修改编码方式：response.content.deocde(“utf8”)
        ```
* 代理
    * 目的：模拟多个客户端请求+ 防止真是IP泄漏
    ![](../images/proxy.png)
    * 常用代理网站：
    * http://www.66ip.cn/pt.html
    * https://www.jianshu.com/p/93fd64a2747b
* 代理（proxies参数）
```
import requests

# 根据协议类型，选择不同的代理
proxies = {
  "http": "http://12.34.56.79:9527",
  "https": "http://12.34.56.79:9527",
}

response = requests.get("http://www.baidu.com", proxies = proxies)
print response.text
   
也可以通过本地环境变量 HTTP_PROXY 和 HTTPS_PROXY 来配置代理：

export HTTP_PROXY="http://12.34.56.79:9527"
export HTTPS_PROXY="https://12.34.56.79:9527"

```
* 私密代理验证（特定格式） 和 Web客户端验证（auth 参数）
```
import requests

# 如果代理需要使用HTTP Basic Auth，可以使用下面这种格式：
proxy = { "http": "mr_mao_hacker:sffqry9r@61.158.163.130:16816" }

response = requests.get("http://www.baidu.com", proxies = proxy)

print (response.text)
```
* web客户端验证
```
import requests

auth=('test', '123456')

response = requests.get('http://192.168.199.107', auth = auth)

print (response.text)
```
* Cookies
    * 如果一个响应中包含了cookie，那么我们可以利用 cookies参数拿到：
    ``` 
    import requests
    response = requests.get("http://www.baidu.com/")
    # 7\. 返回CookieJar对象:
    cookiejar = response.cookies
    # 8\. 将CookieJar转为字典：
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print (cookiejar)
    print (cookiedict)
    ```
> cookie数据存放在客户的浏览器上，session数据放在服务器上。   
cookie不是很安全，别人可以分析存放在本地的cookie并进行cookie欺骗。
session会在一定时间内保存在服务器上。当访问增多，会比较占用你服务器的性能。
单个cookie保存的数据不能超过4K，很多浏览器都限制一个站点最多保存20个cookie。
* session
    * 在 requests 里，session对象是一个非常常用的对象，这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。
    * 会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。
    ```
    实现人人网登录
    import requests
        # 1\. 创建session对象，可以保存Cookie值
        ssion = requests.session()
        # 2\. 处理 headers
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        # 3\. 需要登录的用户名和密码
        data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}  
        # 4\. 发送附带用户名和密码的请求，并获取登录后的Cookie值，保存在ssion里
        ssion.post("http://www.renren.com/PLogin.do", data = data)
        # 5\. ssion包含用户登录后的Cookie值，可以直接访问那些登录后才可以访问的页面
        response = ssion.get("http://www.renren.com/410043129/profile")
        # 6\. 打印响应内容
        print (response.text)
    ```
* 处理HTTPS请求 SSL证书验证
    * Requests也可以为HTTPS请求验证SSL证书：
    * 如果我们想跳过 12306 的证书验证，把 verify 设置为 False 就可以正常请求了。
        * r = requests.get("https://www.12306.cn/mormhweb/", verify = False)
## 非结构化数据和结构化数据提取
### 分类
* 非结构化的数据：文本、电话号码、邮箱地址、html等
    * 处理方法：正则表达式、xpath
* 结构化数据：json，xml等
    * 处理方法：转化为python数据类型
### 正则表达式
* 定义：正则表达式，又称规则表达式，通常被用来检索、替换那些符合某个模式(规则)的文本。
![](../images/reg.png)
* 【注】有一点需要特别注意的是，正则表达式使用 对特殊字符进行转义，所以如果我们要使用原始字符串，只需加一个 r 前缀，示例：r'chuanzhiboke\t\.\tpython'
* 使用步骤：
    * 使用 compile() 函数将正则表达式的字符串形式编译为一个 Pattern 对象
    * 通过 Pattern 对象提供的一系列方法对文本进行匹配查找，获得匹配结果，一个 Match 对象。
    * 最后使用 Match 对象提供的属性和方法获得信息，根据需要进行其他的操作
* compile 函数
    * compile 函数用于编译正则表达式，生成一个 Pattern 对象，它的一般使用形式如下：
    ```python
    import re
    # 将正则表达式编译成 Pattern 对象
    pattern = re.compile(r'\d+')
    ```
* Pattern 对象
    * match 方法：从起始位置开始查找，一次匹配(如果起始位置不匹配直接返回None) 
        * match(string[, pos[, endpos]])
     ```python
        >>> import re
        >>> pattern = re.compile(r'\d+')  # 用于匹配至少一个数字
        
        >>> m = pattern.match('one12twothree34four')  # 查找头部，没有匹配
        >>> print (m)
        None
        
        >>> m = pattern.match('one12twothree34four', 2, 10) # 从'e'的位置开始匹配，没有匹配
        >>> print (m)
        None
        
        >>> m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配
        >>> print (m)                                         # 返回一个 Match 对象
        <_sre.SRE_Match object at 0x10a42aac0>
        
        >>> m.group(0)   # 可省略 0
        '12'
        >>> m.start(0)   # 可省略 0
        3
        >>> m.end(0)     # 可省略 0
        5
        >>> m.span(0)    # 可省略 0
        (3, 5)
    ```  
    * search 方法：从任何位置开始查找，一次匹配
        * search 方法用于查找字符串的任何位置，它也是一次匹配，只要找到了一个匹配的结果就返回，而不是查找所有匹配的结果，它的一般使用形式如下：
        * search(string[, pos[, endpos]])
        ```python
            >>> import re
            >>> pattern = re.compile('\d+')
            >>> m = pattern.search('one12twothree34four')  # 这里如果使用 match 方法则不匹配
            >>> m
            <_sre.SRE_Match object at 0x10cc03ac0>
            >>> m.group()
            '12'
            >>> m = pattern.search('one12twothree34four', 10, 30)  # 指定字符串区间
            >>> m
            <_sre.SRE_Match object at 0x10cc03b28>
            >>> m.group()
            '34'
            >>> m.span()
            (13, 15)
        ```
    * findall 方法：全部匹配，返回列表   
        * 上面的 match 和 search 方法都是一次匹配，只要找到了一个匹配的结果就返回。然而，在大多数时候，我们需要搜索整个字符串，获得所有匹配的结果。
        * findall(string[, pos[, endpos]])
        ```python
            # re_test.py
            
            import re
            
            #re模块提供一个方法叫compile模块，提供我们输入一个匹配的规则
            #然后返回一个pattern实例，我们根据这个规则去匹配字符串
            pattern = re.compile(r'\d+\.\d*')
            
            #通过partten.findall()方法就能够全部匹配到我们得到的字符串
            result = pattern.findall("123.141593, 'bigcat', 232312, 3.15")
            
            #findall 以 列表形式 返回全部能匹配的子串给result
            for item in result:
                print (item)
            运行结果：
            
            123.141593
            3.15
        ```
    * finditer 方法：全部匹配，返回迭代器   
    * split 方法：分割字符串，返回列表   
    ```python
        import re
        p = re.compile(r'[\s\,\;]+')
        print (p.split('a,b;; c   d'))
        执行结果：
        ['a', 'b', 'c', 'd']  
    ```
    * sub 方法：替换   
    ```python
    import re
    p = re.compile(r'(\w+) (\w+)') # \w = [A-Za-z0-9]
    s = 'hello 123, hello 456'
    
    print (p.sub(r'hello world', s))  # 使用 'hello world' 替换 'hello 123' 和 'hello 456'
    print (p.sub(r'\2 \1', s))        # 引用分组
    
    def func(m):
        print(m)
        return 'hi' + ' ' + m.group(2) #group(0) 表示本身，group(1)表示hello，group(2) 表示后面的数字
    
    print (p.sub(func, s))  #多次sub，每次sub的结果传递给func
    print (p.sub(func, s, 1))         # 最多替换一次
    ```
    * 匹配中文
    ```python
    import re
    title = '你好，hello，世界'
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    result = pattern.findall(title)
    
    print (result)
    >>> ['你好', '世界']
    ```
* Match 对象
    * group([group1, ...]) 方法用于获得一个或多个分组匹配的字符串，当要获得整个匹配的子串时，可直接使用 group() 或 group(0)；
    * start([group]) 方法用于获取分组匹配的子串在整个字符串中的起始位置（子串第一个字符的索引），参数默认值为 0；
    * end([group]) 方法用于获取分组匹配的子串在整个字符串中的结束位置（子串最后一个字符的索引+1），参数默认值为 0；
    * span([group]) 方法返回 (start(group), end(group))。
  
```python
>>> import re
>>> pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.I 表示忽略大小写
>>> m = pattern.match('Hello World Wide Web')

>>> print (m)     # 匹配成功，返回一个 Match 对象
<_sre.SRE_Match object at 0x10bea83e8>

>>> m.group(0)  # 返回匹配成功的整个子串
'Hello World'

>>> m.span(0)   # 返回匹配成功的整个子串的索引
(0, 11)

>>> m.group(1)  # 返回第一个分组匹配成功的子串
'Hello'

>>> m.span(1)   # 返回第一个分组匹配成功的子串的索引
(0, 5)

>>> m.group(2)  # 返回第二个分组匹配成功的子串
'World'

>>> m.span(2)   # 返回第二个分组匹配成功的子串
(6, 11)

>>> m.groups()  # 等价于 (m.group(1), m.group(2), ...)
('Hello', 'World')

>>> m.group(3)   # 不存在第三个分组
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group

```
* 【注意：贪婪模式与非贪婪模式】
```python
示例一 ： 源字符串：abbbc
使用贪婪的数量词的正则表达式 ab* ，匹配结果： abbb。

* 决定了尽可能多匹配 b，所以a后面所有的 b 都出现了。

使用非贪婪的数量词的正则表达式ab*?，匹配结果： a。

即使前面有 *，但是 ? 决定了尽可能少匹配 b，所以没有 b。
```
```python
示例二 ： 源字符串：aa<div>test1</div>bb<div>test2</div>cc
使用贪婪的数量词的正则表达式：<div>.*</div>

匹配结果：<div>test1</div>bb<div>test2</div>

这里采用的是贪婪模式。在匹配到第一个"</div>"时已经可以使整个表达式匹配成功，但是由于采用的是贪婪模式，所以仍然要向右尝试匹配，查看是否还有更长的可以成功匹配的子串。匹配到第二个"</div>"后，向右再没有可以成功匹配的子串，匹配结束，匹配结果为"<div>test1</div>bb<div>test2</div>"

使用非贪婪的数量词的正则表达式：<div>.*?</div>

匹配结果：<div>test1</div>

正则表达式二采用的是非贪婪模式，在匹配到第一个"</div>"时使整个表达式匹配成功，由于采用的是非贪婪模式，所以结束匹配，不再向右尝试，匹配结果为"<div>test1</div>"。

```
[正则表达式验证]([http://tool.oschina.net/regex/])

* 实例脚本
[跳转脚本](duanzi_spider.py)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    





    