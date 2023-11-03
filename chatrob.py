#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# chatrob.py
# robot talk
# author: Peng Junwu


import pickle


class RobotUI:
    """机器人UI"""
    def __init__(self, name, admin):
        self.name = name
        self.admin = admin
        
    def talk(self):
        self.welcome()
        words = input('你：')
        answer = self.admin.answer(words)
        print(f'{self.name}: {answer}')

    def welcome(self):
        print(f'Hello,我是机器人{self.name}')
    
class RobotAdmin:
    """机器人管理"""
    def __init__(self):
        self.data = self.load_data()  # 初始化时生成读料库数据
    
    def load_data(self):
        with open('db.pkl', 'rb') as f:
            data = pickle.loads(f.read())
            print(data)
            return(data)
    
    def answer(self, listen):
        "answer something from listen"
        if listen in self.data:
            return self.data[listen]

def main():
    data = {
    '早上好': '早',
    '天气怎么样': '多云转晴，温度26度，北转南风七八级',
    'python怎么学': '请找De8uG'
    }

    with open('db.pkl', 'wb') as f:   # wb : write as binary，二进制文件，防止跨平台问题
        f.write(pickle.dumps(data))   # 序列化

    admin = RobotAdmin()
    robot = RobotUI('robot', admin)
    robot.talk()

if __name__ == "__main__":
    main()