# -*- coding: cp936 -*-
import time
from functools import wraps

 
def timeit(func):
    @wraps(func)
    def wrapper():
        start = time.clock()
        func()
        end =time.clock()
        print 'used:', end - start
        #print name
    return wrapper

def test(f):
    print 'test'
    """IP地址白名单"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print f
        print 'decora'
        return f(*args, **kwargs)
    return decorated_function

def log(text):
    print 'done'
    def decorator(func):
        print '123'
        def wrapper(*args, **kw):
            print '456'
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

@log('jack')
def foo():
    print 'in foo()'
 
##foo()
##print foo.__name__
