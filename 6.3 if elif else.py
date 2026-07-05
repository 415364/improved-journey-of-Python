#if condition1:
    # 如果条件 1 成立，则执行此处的代码块
#elif condition2:
    # 如果条件 2 成立，则执行此处的代码块
#else:
    # 如果所有条件都不成立，则执行此处的代码块
#me=int(input())
#wl=int(input())
#if me < wl:
    #print("WL赢了")
#elif me = wl:
    #print("打平手了")
#else:
    #print("我赢了")

        #猜数小游戏
import random
a = 'Ture'
while a:
    b = int(random.random())
    c = int(input("猜数字小游戏：请输入一个数字，看一下你猜不猜的中"))
    if c == b:
        print("恭喜你猜中了")
    elif c > b:
        print("输入的太大了了，再来一次")
    elif c < b:
        print("输入的太小了，再输入大一点的数字，再来一次")
#代码原理：通过运用random模块（以后会在模块章节详讲）来调用random函数，从而生成随机数字并赋值给判断语句来判断。
# 如果玩家输入的数字刚好时随机数，条件为真，输出恭喜你猜中了。反之，如果大于随机数。输出输入的数字太大了，再来一次；
# 小于，输出输入的太小了，再输入大一点的数字，再来一次。
