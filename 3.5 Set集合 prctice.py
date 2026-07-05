    #Set（集合）数据类型它和Tuple、List一样都属于复合数据类型，而且集合数据类型是一种无序不重复元素的序列
    #在Python中，我们可以使用大括号｛｝或内置函数Set()来创建一个集合(创建一个空集合必须用Set()函数，不可用｛｝，
    # 因为｛｝实质是创建一个空的字典
a={'a','b','c','d','a'}
print(a)#因为集合是无序不重复元素序列，所以不会输出多出的a
b=set('sjienfnekngjf')
print(b)
a={'a','b','c','d','a'}
print('a' in a,'e'in a)#判断元素是否在集合内,在就输出True，反之位False
#数学运算

a=set('dfjenfkeighnneandlasfienglzi')
b=set('nncappjfddsnfnadfmm')
print(a-b)#减号(-)的作用就是输出a集合中b集合内没有的元素
print(a|b)# 竖线符号(|)主要输出集合a或b中包含的元素
print(a&b)# 逻辑符号(&:and,和，拉丁美语为et)就是要输出集合a和b中共同包含的元素
print(a^b)# 乘方(^)主要输出不同时包含于a和b的元素
#在集合中，我们可以使用关键字add或update来添加新的元素；之前的添加是列表，是append
b=set('nncappjfddsnfnadfmm')
print(b)
b.add('fuck')
b.update('good')#为什么无效？good没办法输出？
print(b)
    #删除某些元素，可以使用关键字remove，discard或pop(pop会随机删除某些元素);函数clear()来进行全部删除
b=set('nncappjfddsnfnadfmm')
b.remove('c')
b.discard('n')
b.pop()#pop(pop会随机删除某些元素)
print(b)

b=set('nncappjfddsnfnadfmm')
b.clear()
print(b)