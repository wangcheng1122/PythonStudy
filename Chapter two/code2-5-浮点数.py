import math  # 官网自带库

n1 = 0.123323
n2 = 1.2
print(n1 + n2)

# 0.30000000000000004
n3 = 0.1
n4 = 0.2
print(n3 + n4)

# 四舍五入round
print(round(n3 + n4, 2))
print(round(n1 + n2, 2))

# 向上取整 ceil
print(math.ceil(n1 + n2))

# 向下取整
print(math.floor(n1 + n2))
