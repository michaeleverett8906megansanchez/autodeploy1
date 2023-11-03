#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo.1.py
# A memo demo 51备忘录
# author: De8uG


__author__ = 'De8uG'

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


is_add = True
all_time = 0    
while(is_add):  # 这是个循环输入
    in_date = input('日期：')
    in_thing = input('事件：')
    in_time = input('用时：')
    print('待办列表'.center(30, '-'))
    # one = '{date}, 处理{thing}, 用时{time}'.format(date=in_date, thing=in_thing, time=in_time)
    one = {}
    one['date'] = in_date
    one['thing'] = in_thing
    one['time'] = in_time
    all_memo.append(one)
    all_time += int(in_time)
    num = 0
    for m in all_memo:
        num += 1
        print('%s:%s' %(num, m))

    print(f'共{len(all_memo)}条待办事项, 总时长：{all_time}。', end='')
    print('（y：继续添加，n: 退出）')
    is_add = input().strip() == 'y'