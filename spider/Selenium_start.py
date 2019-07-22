import time
from selenium import webdriver
# 调用键盘按键操作时需要引入的Keys包
from selenium.webdriver.common.keys import Keys
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
def run():
    # driver = webdriver.PhantomJS()
    # 如果没有在环境变量指定PhantomJS位置
    driver = webdriver.PhantomJS(executable_path="/Users/v_anjie01/PycharmProjects/python/phantomjs-2.1.1-macosx/bin/phantomjs")
    # get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择 time.sleep(2)
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    # 获取页面名为 wrapper的id标签的文本内容
    data = driver.find_element_by_id("wrapper").text
    print(data)
    print(driver.title)
    driver.save_screenshot("baidu.png")
    # id="kw"是百度搜索输入框，输入字符串"长城"
    driver.find_element_by_id("kw").send_keys(u"长城")

    # id="su"是百度搜索按钮，click() 是模拟点击
    driver.find_element_by_id("su").click()

    # 获取新的页面快照
    driver.save_screenshot("长城.png")

    # 打应渲染后源码
    print(driver.page_source)

    # cookie
    print(driver.get_cookies())
    # ctrl+a 全选输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'a')
    # ctrl+x 剪切输入框内容
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL, 'x')
    # 输入框重新输入内容
    driver.find_element_by_id("kw").send_keys("itcast")
    # 模拟Enter回车键
    driver.find_element_by_id("su").send_keys(Keys.RETURN)
    time.sleep(1)
    # 清除输入框内容
    # driver.find_element_by_id("kw").clear()

    # 生成新的页面快照
    driver.save_screenshot("itcast.png")

    # 获取当前url
    print(driver.current_url)
    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':

    run()