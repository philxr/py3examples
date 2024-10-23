class A:
    def __init__(self, n=42, *args, **kwargs):
        self.n=42
        self.args, self.kwargs = args, kwargs
    def __str__(self):
        return '[A] n: '+str(self.n)

class Desc:
    def __init__(self, n=42):
        self._n = n
    def __get__(self, obj, objType=None):
        print('GetAttr: '+type(obj).__name__+'.n value='+str(self._n))
        return self._n
    def __set__(self, obj, value):
        print('Trying SetAttr: '+type(obj).__name__+'.n value='+str(self._n)+' to '+str(value))
        try:
            self._n = int(value)
            print('SetAttr: '+type(obj).__name__+'.n value='+str(self._n)+' to '+str(value))
        except:
            print('Error SetAttr: '+type(obj).__name__+'.n value='+str(self._n)+' to '+str(value))
            print(type(obj).__name__+'.n value still '+str(self._n))

class B(A):
    n = Desc()
    def __init__(self, n=42, *args, **kwargs):
        A.__init__(self, n, args, kwargs)

class C:
    n = Desc()
    def __init__(self, n=42, *args, **kwargs):
        self.n = n
        self.args, self.kwargs = args, kwargs

def dec(cls):
    cls.n = Desc()
    return cls

@dec
class A2(A): pass

class Desc2:
    def __init__(self, n=42):
        self._n = n
    def __get__(self, obj, objType=None):
        if hasattr(obj, 'Logging') and obj.Logging == True:
            print('GetAttr: '+type(obj).__name__+'.n value='+str(self._n))
        return self._n
    def __set__(self, obj, value):
        if hasattr(obj, 'Logging') and obj.Logging == True:
            print('Trying SetAttr: '+type(obj).__name__+'.n value='+str(self._n)+' to '+str(value))
        try:
            self._n = int(value)
            if hasattr(obj, 'Logging') and obj.Logging == True:
                print('SetAttr: '+type(obj).__name__+'.n value='+str(self._n)+' to '+str(value))
        except:
            if hasattr(obj, 'Logging') and obj.Logging == True:
                print('Error SetAttr: '+type(obj).__name__+'.n value='+str(self._n)+' to '+str(value))
                print(type(obj).__name__+'.n value still '+str(self._n))
            else:
                raise

class Desc2Ex:
    Logging = False
    n = Desc2()
    def __init__(self, n=42, *args, **kwargs):
        self.n = n
        self.args, self.kwargs = args, kwargs
    @classmethod
    def ToggleLogging(cls):
        cls.Logging = not cls.Logging

class Desc2Ex2(Desc2Ex):
    def __init__(self, n=42, logging=False, *args, **kwargs):
        Desc2Ex.__init__(self, n, args, kwargs)
        self.Logging = logging

