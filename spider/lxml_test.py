from lxml import etree

def parse_xml():
    text = '''
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
    </div>
    '''
    # 解析字符串为html文档
    html = etree.HTML(text)
    print(html)
    # 按照字符串序列号html文档
    result = etree.tostring(html)
    print(result)

def read_xml_file():

    html = etree.parse('./hello.html')
    print(html)
    result = etree.tostring(html, pretty_print=True)

    print(result)
def xpath_test():

    html = etree.parse('./hello.html')
    print(type(html))
    result = html.xpath("//li")
    print(type(result))
    for ele in result:
        val = ele.xpath("@class")
        print(val)
if __name__ == '__main__':
    xpath_test()