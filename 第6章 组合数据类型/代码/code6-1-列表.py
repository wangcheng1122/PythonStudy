# 列表的创建
list1 = []  # 空列表
print(list1)
print(type(list1))
list2 = [1, 2, 3, True, False, 'hello']
print(list2)
list3 = list()  # 当调用 list() 函数且不传入任何参数时，它会创建一个空的列表对象
print(list3)
list3 = list('12345678')  # 当调用 list() 传入参数时，会发生类型转换：str-->list（注意：其他类型不行，例如 boolean float int 等等）
print(list3)

# 列表的索引（从零开始）
print(list3[5])

# 列表的切片（list[start:stop:step]）
print(list3[2:6:2])

# 列表的加法和乘法
print(list3 + list2)
print(list3 * 3)

# 列表的成员运算
print('1' not in list3)
print('1' in [1, 2, 3, 4])
print([3, 2, 3, 4] < [2, 1])  # 意义不大，看看就好

# 一些关于列表的内置函数
print(len(list3))  # 求元素个数
print(max(list3))  # 求元素的最大值
print(min(list3))  # 求元素的最小值
# del list3   # 删除变量
# print(list3)

print('-' * 30)
# 列表的遍历
print(list2)
for i in list2:
    print(i)

for i, j in enumerate(list2):  # 枚举（这里会把索引和值都返回）
    print(i, j)

for i in range(len(list2)): # 不常用
    print(i, list2[i])

print('-' * 30)
# 列表的常用方法  变量.方法名()
# 添加元素
list3.append('666')
print(list3)
# 添加列表
list3.extend([1, 2, 3])
print(list3)
# 插入元素
list3.insert(2, 'hello')
print(list3)
# 根据索引删除元素
list3.pop(3)
print(list3)
# 根据元素删除
list3.remove('7')
print(list3)
list3.append('hello')
print(list3)
list3.remove('hello')
print(list3)
# 清空列表
list3.clear()
print(list3)

# 计算若干个人的平均年龄
age = [10, 20, 30, 40, 23, 45, 78, 43]
print(sum(age) / len(age))