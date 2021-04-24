# -*- coding: utf-8 -*-
import random

class LotteryNumber:
    def __init__(self):
        self.rules = {
            'mega millions': ((5, 1, 70), (1, 1, 25)), 
            'power ball': ((5, 1, 69), (1, 1, 26)), 
            'superlotto plus': ((5, 1, 47), (1, 1, 27)), 
            '福彩 双色球': ((6, 1, 33), (1, 1, 16)), 
            '体彩 大乐透': ((5, 1, 35), (2, 1, 12))
        }
        self.defaultRule = self.rules['mega millions']

    def setRule(self, rule):
        self.defaultRule = rule

    def generateNum(self):
        length = 0
        for r in self.defaultRule:
            length += r[0]
        num = [None] * length
        i = 0
        for r in self.defaultRule:
            for _ in range(r[0]):
                num[i] = random.randint(r[1], r[2])
                i += 1
        return tuple(num)

if __name__ == '__main__':
    lotto_num = LotteryNumber()
    rules = tuple(lotto_num.rules.keys())
    for _ in range(10):
        rule = random.choice(rules)
        lotto_num.setRule(lotto_num.rules[rule])
        print(rule, ': ', lotto_num.generateNum())