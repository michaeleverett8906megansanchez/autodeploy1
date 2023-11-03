#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# guess21.py
# author: De8uG


# 1.导入标准库
import random

# 2.第三方的库
# 3.自定义的库

"""
案例：21点

- 两个玩家，游戏开始先输入名字
- 用字典保存每个玩家信息：姓名，获胜次数
- 电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21的获胜
- 每轮结束显示玩家信息
- 按q退出游戏
"""

target = 21

# 人类
user1 = input('第一个玩家名字：')
user2 = input('第二个玩家名字：')
print(f'玩家：{user1}, {user2}')

users = {
    user1:
    {'win': 0},
    user2:
    {'win': 0}
}

print(users)

# PC 随机出2个数
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

# 此处不应该现在打印出来
# print(f'电脑随机选数：{num1}, {num2}')

user1_guess = input(f'{user1} guess:')
user2_guess = input('user2 guess:')
user1_sum = int(num1) + int(num2) + int(user1_guess)
user2_sum = int(num1) + int(num2) + int(user2_guess)
print(user1_sum, user2_sum)

if abs(user1_sum-21) > abs(user2_sum-21):
    print(f'{user1_sum}', f'{user2_sum}')
    print('user2 win!')
else:
    print('user1 win!')

print(f'电脑随机选数：{num1}, {num2}')
