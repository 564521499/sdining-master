import threading


class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance


class Mets:
    pass


# obj1 = Singleton()
# obj2 = Singleton()
# obj1 = Mets()
# obj2 = Mets()
# print(obj1, obj2)

