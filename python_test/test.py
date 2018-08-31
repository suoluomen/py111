from functools import wraps
# 导入装饰器
def logit(logfile='out.log'):
    # 编辑装饰器
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # 打开文件，在文件末尾追加日志
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
        return wrapped_function
    return logging_decorator
# 定义新的文件路径
@logit("out1.log")
def myfunc1():
    pass
myfunc1()
