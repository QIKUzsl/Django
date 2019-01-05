# result=(i for i in range(30) if i % 3 is 0)
# for i in result:
#     print(i)


# result=[i for i in range(30) if i % 3 is 0]
# print(result)

# result= {'a':10,'b':34}
# k_frequency = {v: k for k, v in result.items()}
# print(k_frequency)

# 字典推导式
# d={key:value for{'a':10,'b':20} in iterable}

# import pickle
# pickle.dump()
# pickle.dumps()




class Singleton():
    _instance = None
    def __init__(self):
        print("调用init方法")
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(id(a))
print(id(b))







