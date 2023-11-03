#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo_v27.py
# A memo demo 51备忘录，使用函数优化
# 使用正则表达式
# author: PengJunwu


import sys


__author__ = 'PengJunwu'


def welcom():
    " 欢迎词！"
    desc = '51备忘录'.center(30, '-')
    print(desc)

    welcome = 'welcome'
    print(f'{welcome}', __author__)

    print('请输入备忘信息：')

all_memo = []  

# 添加dict保存一条信息
"""
{
    'date': 1.1,
    'thing': 'python',
    'time': 30
}
{
    'time': 8,
    'thing': 'python',
}
"""

def input_memo():
    "输入备忘录记录"
    try:
        is_add = True
        all_time = 0    
        while(is_add):  # 这是个循环输入
            in_date = input('日期：')
            in_thing = input('事件：')
            in_time = input('用时：')
            print('待办列表'.center(30, '-'))
            add_memo(in_date, in_thing, in_time)
            all_time += int(in_time)
            print_memo(all_time)

            is_add = input().strip() == 'y'
    except Exception as e:
        print('添加memo出错：', e)

def print_memo(all_time):
    "打印Memo"
    num = 0
    for m in all_memo:
        num += 1
        print('%s:%s' % (num, m))
    print(f'共{len(all_memo)}条待办事项, 总时长：{all_time}。', end='')
    print('（y：继续添加，n: 退出）')

def add_memo(in_date, in_thing, in_time):
    "添加备忘记录"
    one = {}
    one['date'] = in_date
    one['thing'] = in_thing
    one['time'] = in_time
    all_memo.append(one)

def help():
    print("""usage: python 51memo_v26.py 
    -a or -add, 添加记录
    -d or --delete, 删除记录
    -m or --modify, 修改记录
    """)

def delete_meme():
    print("请完成删除函数")

def modify_memo():
    print("请完成修改函数")

def main():
    """
    main: 程序主入口，当前文件单独运行时从这里运行
    函数优化：每个函数尽量只干一件事！
    用sys模块添加系统参数
    """
    # print(sys.argv)
    if len(sys.argv) == 1:
        help()

    welcom()
    try:
        if sys.argv[1] in {"-a","--add"}:
            input_memo()
        elif sys.argv[1] in {"-d","--delete"}:
            delete_meme()
        elif sys.argv[1] in {"-m","--modify"}:
            modify_memo()
        else:
            helo()
    except Exception as e:
        print(e)
        help()

if __name__ == '__main__':
    main()
