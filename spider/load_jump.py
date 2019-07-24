import json
import chardet


def to_loads():
    strList = '[1, 2, 3, 4]'
    strDict = '{"city": "北京", "name": "大猫"}'

    print(type(strDict))
    print (type(json.loads(strDict)))


def to_dumps():
    listStr = [1, 2, 3, 4]
    tupleStr = (1, 2, 3, 4)
    dictStr = {"city": "北京", "name": "大猫"}

    # 注意：json.dumps() 序列化时默认使用的ascii编码
    # 添加参数 ensure_ascii=False 禁用ascii编码，按utf-8编码
    # chardet.detect()返回字典, 其中confidence是检测精确度

    print(json.dumps(dictStr))
    print(json.dumps(dictStr).encode())
    print(chardet.detect(json.dumps(dictStr).encode()))
    # {'confidence': 1.0, 'encoding': 'ascii'}
    print(json.dumps(dictStr,ensure_ascii=False))
    print(chardet.detect(json.dumps(dictStr,ensure_ascii=False).encode()))
def to_dump():
    listStr = [{"city": "北京"}, {"name": "大刘"}]
    json.dump(listStr, open("listStr.json", "w"), ensure_ascii=False)
def to_load():
    strList = json.load(open("listStr.json"))
    print(strList)

    # [{u'city': u'\u5317\u4eac'}, {u'name': u'\u5927\u5218'}]

    strDict = json.load(open("dictStr.json"))
    print(strDict)
if __name__ == '__main__':
    # to_loads()
    # to_dumps()
    # to_dump()
    to_load()