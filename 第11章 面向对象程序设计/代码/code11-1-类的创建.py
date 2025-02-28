class Player(object):  # object 基类
    pass  # pass 是一个占位符语句，用于表示“什么都不做”


tom = Player()  # 类的实例化（创建对象）
print(type(tom))
print(isinstance(tom, object))
print(isinstance(tom, Player))