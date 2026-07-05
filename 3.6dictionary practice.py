    #典是另外一种数据储存的可变容器，而且可以存储任何数据类型的数据值对象。
    #创建一个空字典需要用大括号｛｝，在字典中每一个值对用冒号，且每个值需要逗号（,）分隔

    #演示创建一个字典并输出
a={'a':'Python','b':'347','c':'hkhndggs'}
b={'a':'HTML/Javasctipt','b':'Rust'}
print(b)
print(a['a'],a['c'])
    #在这个代码中a['a']与a['c']是分别访问并输出字典内对应数据值，与索引方式差不多，而print(b)则负责输出整个字典b内数据。
    #有点没看懂
a={'a':'Python','b':'347','c':'hkhndggs'}
b={'a':'HTML/Javasctipt','b':'Rust'}
print(b)
print(a['a'],a['c'])#KeyError: 'd'

a={'a':'Python','b':'347','c':'hkhndggs'}
b={'a':'HTML/Javasctipt','b':'Rust'}
a['c']=('perl')
a['a']=('fuking everything')
print(a['a'],a['c'])#print 打印出来的是中括号里面的数字

    #清除字典数据也很简单，与集合一样，使用clear()函数，然而删除的话就需要用到del语句
a={'a':'Python','b':'347','c':'hkhndggs'}
a.clear()#清除字典所有数据
print(a)
del a#删除字典 #del语句把字典删除了，所以hui输出异常
print(a)