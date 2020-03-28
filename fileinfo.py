#Script Name			:fileinfo.py
#Author					:ZhangGuoyi
#Created				:28th March 2020
#Last Modified		:
#Version				:1.0
#Modifications		:



#计算平方根
eps=0.01
numberGuess=0
#1.输入
x=int(input("请输入你要计算平方根的整数:"))
#2.计算
g=1
while abs(g**2-x)>=eps and g<=x:
    g =(g+x/g)/2
    numberGuess += 1
#3.输出
print("猜想的次数为：",numberGuess)
if abs(g**2-x)>eps:
    print("骚年，这个数并没有平方根。",x)
else:
    print(x,"的平方根是{:.3f}".format(g))
input()