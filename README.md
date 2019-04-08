# python
### 介绍
* 优点：定位是“优雅”、“明确”、“简单”
* 缺点：
    * 运行速度慢
    * 是代码不能加密（目前的互联网时代，靠卖软件授权的商业模式越来越少了，靠网站和移动应用卖服务的模式越来越多了，后一种模式不需要把源码给别人。）
### 安装
### Python解释器
Python的解释器很多，但使用最广泛的还是CPython。如果要和Java或.Net平台交互，最好的办法不是用Jython或IronPython，而是通过网络调用来交互，确保各程序之间的独立性。
### 基础
* 始终坚持使用4个空格的缩进
* 大小写敏感
* 当语句以冒号:结尾时，缩进的语句视为代码块
#### 数据类型
* 整数
    * 处理任意大小整数
    * 十六进制“0x”前缀 eg:0xff00
* 浮点数
    * 很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x10^9就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等。
    * 整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
* 运算
    * Python的整数运算结果仍然是整数，浮点数运算结果仍然是浮点数
    * 整数和浮点数混合运算的结果就变成浮点数了
    * 11 / 4    # ==> 2
    * 11 % 4    # ==> 3
    * 11.0 / 4    # ==> 2.75
* 字符串
    * 字符串是以''或""括起来的任意文本
    * 转义
        * \
        * \n 表示换行
        * \t 表示一个制表符
        * \\ 表示 \ 字符本身
    * Python中raw字符串与多行字符串
        *  raw 字符串，里面的字符就不需要转义了 eg:r'\(~_~)/ \(~_~)/'
        * 多行：表示多行字符串，可以用'''...'''表示
    * 中文：# -*- coding: utf-8 -*-
* 布尔值
    * 一个布尔值只有True、False两种值
    * 布尔值可以用and、or和not运算。
        * and运算是与运算，只有所有都为 True，and运算结果才是 True。
        * or运算是或运算，只要其中有一个为 True，or 运算结果就是 True。
        * not运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True
        * Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True，所以：
            * a = True   
              print a and 'a=T' or 'a=F'   
              继续计算 'a=T' or 'a=F' 计算结果还是 'a=T'   

* 空值
* 变量
    * 变量名必须是大小写英文、数字和下划线（_）的组合，且不能用数字开头
    * 和静态语言相比，动态语言更灵活，就是这个原因。
#### List和Tuple类型
* List
    * L = ['Adam',95.5, 'Lisa',85, 'Bart', 59]
    * 访问：L[index]
    * 使用倒序索引时，也要注意不要越界。倒叙从-1开始
    * append()总是把新的元素添加到 list 的尾部。
        eg:L.append('Paul')   
    * insert()方法，它接受两个参数，第一个参数是索引号，第二个参数是待添加的新元素;
    * pop()方法总是删掉list的最后一个元素，并且它还返回这个元素;
        * 由于Paul的索引是2，因此，用 pop(2)把Paul删掉：
    * 替换:L[2] = 'Paul'
* Tuple
    * tuple一旦创建完毕，就不能修改了
    * eg： t = ('Adam', 'Lisa', 'Bart')
    * 创建tuple和创建list唯一不同之处是用( )替代了[ ]。
    * Python之“可变”的tuple
        * t = ('a', 'b', ['A', 'B'])
#### 条件判断和循环
##### if
```
age = 20
if age >= 18:
    print 'your age is', age
    print 'adult'
print 'END'
```
* 语法：
    * 具有相同缩进的代码被视为代码块，上面的3，4行 print 语句就构成一个代码块（但不包括第5行的print）。如果 if 语句判断为 True，就会执行这个代码块。
    * 注意: if 语句后接表达式，然后用:表示代码块开始。
    * 如果你在Python交互环境下敲代码，还要特别留意缩进，并且退出缩进需要多敲一行回车
```else
score = 55
if score >= 60:
    print 'passed'
else:
    print 'failed'
```
```else if
if age >= 18:
    print 'adult'
elif age >= 6:
    print 'teenager'
elif age >= 3:
    print 'kid'
else:
    print 'baby'
# 特别注意: 这一系列条件判断会从上到下依次判断，如果某个判断为 True，执行完对应的代码块，后面的条件判断就直接忽略，不再执行了。
```
##### for
```
L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print name
#  name 这个变量是在 for 循环中定义的，意思是，依次取出list中的每一个元素，并把元素赋值给 name，然后执行for循环体（就是缩进的代码块）。
```
##### while
```
N = 10
x = 0
while x < N:
    print x
    x = x + 1
# 如果没有这一个语句，while循环在判断 x < N 时总是为True，就会无限循环下去，变成死循环，所以要特别留意while循环的退出条件。
```
#####  break退出循环、continue继续循环
* 用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。
* 在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。
##### 在循环内部，还可以嵌套循环，我们来看一个例子：
```
for x in ['A', 'B', 'C']:
    for y in ['1', '2', '3']:
        print x + y
```
#### Dict和Set类型
* Dict
    * 花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可。最后一个 key: value 的逗号可以省略。
    * 我们把名字称为key，对应的成绩称为value，dict就是通过 key 来查找 value。
```
d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
# 取值方法一：d[key]
一是先判断一下 key 是否存在，用 in 操作符：
if 'Paul' in d:
    print d['Paul']
# 取值方法二：是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None：
    d.get('Paul')
```  
* Dict VS List特点
    * 第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
    * dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢。
    * 由于dict是按 key 查找，所以，在一个dict中，key不能重复。
    * dict的第二个特点就是存储的key-value序对是没有顺序的！这和list不一样：
    * 作为 key 的元素必须不可变，Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。
* Dict更新值
d['Paul'] = 72
* Dict 遍历
```
d= {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
for key in d:
    print key + ':', d[key]
```
* set
    * set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的，这点和 dict 的 key很像。
    * 创建：创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素：
        * >>> s = set(['A', 'B', 'C'])
        * 结果显示，set会自动去掉重复的元素，原来的list有4个元素，但set只有3个元素。
    * 访问set
        *  in 操作符判断
            >>> 'Bart' in s   
            True      
        * 看来大小写很重要，'Bart' 和 'bart'被认为是两个不同的元素。
    * 特点
        * set的内部结构和dict很像，唯一区别是不存储value，因此，判断一个元素是否在set中速度很快
        * set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
        * set存储的元素也是没有顺序的
    * 遍历
    ```
          >>> s = set(['Adam', 'Lisa', 'Bart'])
          >>> for name in s:
          ...     print name
          ... 
          Lisa
          Adam
          Bart
    ```     
    * 更新set
        * s.add(4)/s.remove(4)
#### 函数
* 内置函数
    * abs( value1 )
    * cmp(x, y) 就需要两个参数，如果 x<y，返回 -1，如果 x==y，返回 0，如果 x>y，返回 1：
    * int()函数可以把其他数据类型转换为整数：
    * str()函数把其他类型转换成 str：
    * help(abs) 查看abs函数的帮助信息
* 自定义函数
    * 定义一个函数要使用 def 语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用 return 语句返回
    ```
        def my_abs(x):
            if x >= 0:
                return x
            else:
                return -x
    ```
    * 返回多个值
    ```
      #返回多个值
      import math
      def move(x, y, step, angle):
          nx = x + step * math.cos(angle)
          ny = y - step * math.sin(angle)
          return nx, ny
          
      # 调用
      >>> x, y = move(100, 100, 60, math.pi / 6)
      >>> print x, y
      151.961524227 70.0
      
      # 但其实这只是一种假象，Python函数返回的仍然是单一值：
      >>> r = move(100, 100, 60, math.pi / 6)
      >>> print r
      (151.96152422706632, 70.0)
    
       ### 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
    ```
    * 递归
    * 默认参数
        * 由于函数的参数按从左到右的顺序匹配，所以默认参数只能定义在必需参数的后面：
    ```
    def power(x, n=2):
        s = 1
        while n > 0:
            n = n - 1
            s = s * x
        return s
    ```
    * 可变参数
    ```
    def fn(*args):
        print args
    ```
#### 字符串和编码
#### 切片
   *  L[par1:par2:par3]
        * par1:起始位置
        * par2：结束位置（不包括）
        * par3：表示每N个取一个
   * 倒序切片
        * 记住倒数第一个元素的索引是-1。倒序切片包含起始索引，不包含结束索引。
   * 字符串切片
        * 同理list切片
#### 迭代
   * 因此，迭代操作就是对于一个集合，无论该集合是有序还是无序，我们用 for 循环总是可以依次取出集合的每一个元素。
   * 而迭代是一个动词，它指的是一种操作，在Python中，就是 for 循环。
   * 索引迭代
        * Python中，迭代永远是取出元素本身，而非元素的索引。
            * 方法是使用 enumerate() 函数：
            ```
                >>> L = ['Adam', 'Lisa', 'Bart', 'Paul']
                >>> for index, name in enumerate(L):
                ...     print index, '-', name
                ... 
                0 - Adam
                1 - Lisa
                2 - Bart
                3 - Paul
                # 原理
                ['Adam', 'Lisa', 'Bart', 'Paul']--------->[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
                因此，迭代的每一个元素实际上是一个tuple：
                for t in enumerate(L):
                    index = t[0]
                    name = t[1]
                    print index, '-', name
                如果我们知道每个tuple元素都包含两个元素，for循环又可以进一步简写为：
                for index, name in enumerate(L):
                    print index, '-', name        
            ```              
     * dict 那这两个方法有何不同之处呢？
       *  values() 方法实际上把一个 dict 转换成了包含 value 的list。
       *  但是 itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存。
       *  迭代key 和 value
            * for key, value in d.items()
#### 列表生成式
   * [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]>>> [x * x for x in range(1, 11)]
   * 复杂表达式
   ```
   d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
   def generate_tr(name, score):
       return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)
   
   tds = [generate_tr(name, score) for name, score in d.iteritems()]
   print tds
   print '<table border="1">'
   print '<tr><th>Name</th><th>Score</th><tr>'
   print '\n'.join(tds)
   print '</table>'
   ```
   * 条件过滤
        ``` >>> [x * x for x in range(1, 11) if x % 2 == 0]
          [4, 16, 36, 64, 100]
        ```    
   * 多层表达式
    ```
    >>> [m + n for m in 'ABC' for n in '123']
    ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
    ```
### 函数式编程
* 特点
    * 把计算视为函数而非指令
    * 纯函数式编程：不需要变量，没有副作用，测试简单
    * 支持高阶函数，代码简单
* python函数式编程特点
    * 不是纯函数式编程：允许有变量
    * 支持高阶函数：函数可以作为变量传入
    * 支持闭包：有了闭包就能返回函数
    * 有限度的支持匿名函数
#### 高阶函数
* 定义：能接受函数作为参数的函数
    * 变量可以指向函数
    * 函数的参数可以接受变量
    * 一个函数可以接受另一个函数作为参数
    * 能够接受函数作为参数的函数就是高阶函数
* 把函数作为参数
    ```
        def add (x ,y,f):
            return f(x)+f(y) 
        # 调用
        add(1,-3,abs)   
    ```
* 内置高阶函数
    * map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
        * 注意：map()函数不改变原有的 list，而是返回一个新的 list
    ```
        def f(x):
            return x*x
        print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    ```
    * reduce()函数接收的参数和 map()类似，一个函数 f，一个list，reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值。
        * reduce()还可以接收第3个可选参数，作为计算的初始值。
    * filter()函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个元素进行判断，返回 True或 False，filter()根据判断结果自动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。
     ```
     利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：
     def is_not_empty(s):
         return s and len(s.strip()) > 0
     filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
     ```  
     * sorted()自定义排序：传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。
     ```
        def cmp_ignore_case(s1, s2):
            u1=s1.upper()
            u2=s2.upper()
            if u1<u2:
                return -1
            if u1>u2:
                return 1
            return 0
        print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
     ```
     * 返回函数：返回函数可以把一些计算延迟执行。例如，如果定义一个普通的求和函数：

     ```
     例如，定义一个函数 f()，我们让它返回一个函数 g，可以这样写：
        def f():
            print 'call f()...'
            # 定义函数g:
            def g():
                print 'call g()...'
            # 返回函数g:
            return g
        # 调用
        >>> x = f()   # 调用f()
        call f()...
        >>> x   # 变量x是f()返回的函数：
        <function g at 0x1037bf320>
        >>> x()   # x指向函数，因此可以调用
        call g()...   # 调用x()就是执行g()函数定义的代码 
    
        请注意区分返回函数和返回值：
        def myabs():
            return abs   # 返回函数
        def myabs2(x):
            return abs(x)   # 返回函数调用的结果，返回值是一个数值        
     ```
     
   
 
        
        


