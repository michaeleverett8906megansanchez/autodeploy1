#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# 21point.py
# 21点猜猜看游戏
# author: Peng Junwu
"""
二 完善21点游戏（30分）
- 两个玩家，游戏开始先输入名字
- 用字典保存每个玩家信息：姓名，获胜次数
- 电脑随机产生2个数，每个玩家轮流猜1个数，与电脑随机两个数求和，最接近21的获胜
- 每轮结束显示玩家信息
- 按q退出游戏
"""

# 1.导入标准库
import random
# 2.导入第三方的库
# 3.导入自定义的库

# 定义变量
target = 21

goon = True

# 玩家姓名输入
user1 = input('第一个玩家姓名：')
user2 = input('第二个玩家姓名：')
print(f'玩家:{user1},{user2}')
users = {
    user1:{'win':0},
    user2:{'win':0}
}
# print(users)

while (goon):
    # 生产２个随机数
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    #print(f'电脑随机选数:{num1},{num2}')

    #　玩家猜数并求和
    user1_guess = input(f'请{user1}请猜数：')
    user2_guess = input(f'请{user2}猜数：')
    user1_sum = int(num1) + int(num2) + int(user1_guess)
    user2_sum = int(num1) + int(num2) + int(user2_guess)
    # print(f'电脑随机选数与玩家猜数求和:{user1_sum},{user2_sum}')

    #　计算猜数大小，并输出结果
    if abs(user1_sum - 21) > abs(user2_sum - 21):
        print(f'{user1}求和为：{user1_sum}',', 'f'{user2}求和为：{user2_sum}')
        users[user2]['win'] += 1
        print(f'{user2} 获胜!')
    else:
        print(f'{user1}求和为：{user1_sum}',', 'f'{user2}求和为：{user2_sum}')
        users[user1]['win'] += 1
        print(f'{user1}　获胜!')
    
    # user1_scorp = users[user1]['win']
    # user2_scorp = users[user2]['win']

    print(f'---比赛结果：{user1}/{user2} = {users[user1]["win"]}/{users[user2]["win"]}---')
    print('请输入(y:继续，q:退出):')
    goon = input().strip() == 'y' 

