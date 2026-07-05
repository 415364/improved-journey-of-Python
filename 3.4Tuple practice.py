    #小括号();中括号[列表]；大括号{}
    #元组使用小括号，括号中元素不能被改变,创建元组可以不需要括号
    #变量名称 = ('元素',元素)
    #变量名称 = "元素","元素"
a = ('C/c++','Python',2)	#创建两个元组
b = "Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"
print(a,b)
a = ('C/c++','Python',2)	#创建两个元组
b = "Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"
c=a+b
print(c)
print(len(c),len(b),len(a))
print(a*2,c*4)
print(b in ("Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"))
#判断元素是否存在
for c in("Python","Love to lxx for Li wenli","never change","Love to lxx for Li wenli","never change",'C/c++','Python',2):
    print(c,)#迭代输出
#元组的内置函数（具体在注释）
a = ('C/c++','Python',2)
b = "Python菜中菜的菜鸟","Love to lxx for Li wenli","never change"
c=a+b
c=tuple(c)#强制转换为元组
print(len(c))#输出列表内数据个数
d=('3','4','7','8')
print(max(d))#输出d元组内最大数值
print(min(d))#输出d元组内最小数值，max()是判断最大值函数，min()反之