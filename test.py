import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 执行函数
        # end_time = time.time()  # 记录结束时间
        # print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to complete.")
        # print(f"my name is {args[0]}")
        return result

    return wrapper


@timer
def some_function(name):
    # 这里模拟一个耗时的操作
    time.sleep(2)
    print("Function is running...")
    print(f"my name is {name}")


# some_function("wang")
result = some_function("wang")
print(result)
print(some_function.__name__)

print("-----------------------------")


def separate_log(func):
    # @functools.wraps(func)
    def wrapper(level, log_msg):
        func(level, log_msg)
        if level == "info":
            print(f"Info: system is working well")
        elif level == "error":
            print(f"Error: system is dead")
        else:
            print(f"Debug: system is debugging")

    return wrapper


@separate_log
def print_log(level, log_msg):
    print(f"Log: {log_msg}")


print_log("info", "my info")
print_log("error", "my error")
print_log("debug", "my debug")

print("-----------------------------")


def repeat(num):
    def upper_wrapper(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                result = func(*args, **kwargs)
                print(result)  # 在这里打印每次的结果
            return result

        return wrapper

    return upper_wrapper


@repeat(5)
def say_hello(name):
    return f"hello, {name}"


say_hello("Alice")
