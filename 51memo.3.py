#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 51memo.3.py
# A memo demo 51备忘录
# author: Peng Junwu

# 1.导入标准库
# 2.导入第三方的库
# 3.导入自定义的库
from color_me import ColorMe

__author__ = 'PengJunwu'

desc = '51备忘录'.center(30, '-')
print(desc)
welcome = 'Welcome'
print(f'{welcome}', __author__)
print('请输入备忘信息：')

all_memo = []  

"""
三 完善51备忘录程序（30分）
1.使用字典和列表嵌套结构表示多条记录
2.添加信息时，直接输入一句话，进行解析拆解，记录时间与事件
3.不同信息采用不同颜色输出
"""
# 添加dict保存一条信息
"""
{
    'date': 1.1,
    'thing': 'python',
    'time': 30
}
{
    'time': 2月2日9点,
    'thing': '开python技术研讨会',
}
"""


is_add = True
all_time = 0    
while(is_add):  # 这是个循环输入
    memo_input = input('请输入待办事件（如：2月3日9点开Python技术研讨会)：')
    in_date = memo_input[:memo_input.find('点')+1]
    in_thing = memo_input[memo_input.find('点')+1:]
    # in_date = input('日期：')
    # in_thing = input('事件：')
    # in_time = input('用时：')
    print('待办列表'.center(30, '-'))
    # one = '{date}, 处理{thing}, 用时{time}'.format(date=in_date, thing=in_thing, time=in_time)
    one = {}
    one['date'] = in_date
    one['thing'] = in_thing
    # one['time'] = in_time
    all_memo.append(one)
    # all_time += int(in_time)
    num = 0
    for m in all_memo:
        num += 1
        m_output = str(num) + ":" + m['date'] + ',' + m['thing']
        if num % 2 == 0:
            m_output = ColorMe(m_output).blue()
        else:
            m_output = ColorMe(m_output).red()

        print(m_output)

    print(f'共{len(all_memo)}条待办事项', end='')
    # print(f'共{len(all_memo)}条待办事项, 总时长：{all_time}。', end='')
    print('（y：继续添加，n: 退出）')
    is_add = input().strip() == 'y'