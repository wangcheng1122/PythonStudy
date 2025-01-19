"""
    sep设置分隔符，end设置结束符
"""

year = 2024
month = 7
name = 'Charlie'
temperature = 19.5
day = '一'
print(str(year) + '我要减肥', '可以的', sep='')
print("\n", end="*")
print(str(year) + '我要减肥', '可以的', sep='', end="\n\n")
print('今年是%d' % year)
print('今年是%d年%d月' % (year, month))
print('今年是 %d 年 %02d 月' % (year, month))
print('今年是 %d 年 %02d 月 星期%s' % (year, month, day))
print('今年是 %d 年 %02d 月 星期%s 温度%f' % (year, month, day, temperature))
print('今年是 %d 年 %02d 月 星期%s 温度%0.2f' % (year, month, day, temperature))

print(f"今年是:{year}年，{month}月")
