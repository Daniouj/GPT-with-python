motocycles = ["suzuki","dukati","honda","yamaha"]
#学习apend用法
motocycles.append("grant")
print(motocycles)
#学习在列表中添加元素的用法
motocycles[0] = "bicycles"
print(motocycles)
#学习insert的用法（位置，字符）
motocycles.insert(0,"suzuki")
print(motocycles)
#学习列表删除用法del
del motocycles[0]
print(motocycles)
#学习POP用法，POP用法对列表中的最后一个元素删除并显示出来
motocycles_poped = motocycles.pop()
print(motocycles)
print(motocycles_poped)
