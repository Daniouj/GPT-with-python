motocecles = ["suzuki","teliyaki","yasai"]
#学习remove用法，如果一列表中存在多个相同的值，remove只会删除第一个出现的值。
motocecles.remove("teliyaki")
print(motocecles)
file = "teliyaki"
#\n用于换行
print("\nA " + file.title() + " is to expensive for me ")

#列表排序sort
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
