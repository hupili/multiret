from functools import wraps
import inspect

def multi(f1, f2):
    def liu(func):
        @wraps(func)
        def _(*args, **kwargs):
            frame,filename,line_number,function_name,lines,index=\
                inspect.getouterframes(inspect.currentframe())[1]
            call_str = lines[0].strip()
            #return execute_method_for(call_str)
            print 'call_str:', call_str
            return func()
        return _
    return liu

@multi(1,2)
def f(*args, **kwargs):
    return 1, 2

print f()
a, b = f()
