s = 'hello,world'
print(s[0])
print(s[0], s[-1])
# 切片，步数默认为1，可省略不写
print(s[0:2])  # 包头不包尾
# 完整切片,第三个参数就是步数
print(s[0:6:2])
print(s[1::2])
print(s[::2])

# 字符串反转（通过切片很容易实现）
print(s[-1:-12:-1])
print(s[::-1])
