def decorator(func):
    def inner(*args,**kwargs):
        print("before function run")
        result = func(*args,**kwargs)
        print("after function run")
    return inner
@decorator
def simple():
    print("hello")
simple()