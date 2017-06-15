# !/usr/bin/env python
# 不加env相当于写死了python路径，相反会去环境设置寻找python目录,推荐这种写法
""""此次作业是写一登陆程序，输入三次被锁定
    并且重新打开也是锁定状态
"""
fo = open("pass.txt", "r")
seq = fo.readline()
seq = seq.split(",", 2)
fo.close()
while True:
    acount = input("请输入您的账号：")
    password = input("请输入您的密码：")
    if acount == seq[0] and password == seq[1] and int(seq[2]) < 3:
        print("登陆成功！")
        break
    elif int(seq[2]) == 3:
        print("账户已被锁定！")
        break
    else:
        if 2-int(seq[2]):
            print("密码错误，您还有", 2-int(seq[2]), "次机会")
            seq[2] = int(seq[2])+1
        else:
            print("禁止登陆！")
            seq[2] = '3'
            break
fo = open("pass.txt", "w")
seq = ",".join(seq)
fo.writelines(seq)
fo.close()

