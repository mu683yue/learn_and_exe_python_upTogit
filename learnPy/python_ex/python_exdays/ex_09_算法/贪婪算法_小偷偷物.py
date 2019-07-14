#!/usr/bin/python3
# -*- coding:utf-8 -*-


"""
贪婪法例子：
小偷偷东西，只能装20公斤赃物，有如下物品。显然不能拿走所有物品，可以拿走哪些，留下哪些？
名称 价格（美元） 重量（kg）
电脑 200 20
收音机 20 4
钟 175 10
花瓶 50 2
书 10 1
油画 90 9

author：LHQ
date：2019\7\10
version:1.0

"""

class Thing(object):
    
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    @property
    def value(self):
        """价格重量比"""
        return self.price / self.weight

def input_thing():
    """
    输入物品信息
    """
    name_str,price_str,weight_str = input("请输入名称、价格、重量/（之间以空格间隔/）：").split()
    return name_str,int(price_str),int(weight_str)

def main():
    """主函数"""
    max_weight ,num_of_things = map(int,input("输入可负最大重量和最多物件数量：").split())
    all_things = []
    for _ in range(num_of_things):
        all_things.append(Thing(*input_thing()))
    all_things.sort(key=lambda x: x.value,reverse = True)
    total_weight = 0
    total_price = 0

    for thing in all_things:
        if total_weight + thing.weight <=max_weight:
            print(f"小偷拿走了{thing.name}")
            total_weight += thing.weight
            total_price += thing.price
    print(f"总价值：{total_price}美元")

if __name__=='__main__':
    main()
            
