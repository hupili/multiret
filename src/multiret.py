from functools import wraps
import inspect
import re

PATTERN_MULTI_RETURN = r'(\w+(\s*,\s*\w+)*)\s*=\s*%s'

def multi(func):
    '''
    This decorator makes a function able to return multiple variables.

    How many variables the client get depends on the caller's pattern.
    '''
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        mypattern = PATTERN_MULTI_RETURN % func.__name__
        frame, filename, line_number, function_name, lines, index = \
            inspect.getouterframes(inspect.currentframe())[1]
        call_str = lines[0].strip()
        print 'call_str:', call_str
        ret = re.search(mypattern, call_str)
        if ret:
            expected_vars = map(str.strip, ret.groups()[0].split(','))
            print expected_vars
        else:
            expected_vars = ['x']
        returned_vars = func(*args, **kwargs)
        if len(expected_vars) == 1:
            if isinstance(returned_vars, tuple):
                return returned_vars[0]
            else:
                return returned_vars
        else:
            if not isinstance(returned_vars, tuple):
                returned_vars = (returned_vars, )
            if len(expected_vars) <= len(returned_vars):
                return returned_vars[0:len(expected_vars)]
            else:
                return returned_vars + (None, ) * (len(expected_vars) - len(returned_vars))
    return wrapped_func


if __name__ == '__main__':
    @multi
    def f(*args, **kwargs):
        return 1, 2
    print f()
    a, b = f()
    print a, b
    a, b, c = f()
    print a, b, c

