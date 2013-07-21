# -*- coding: utf-8 -*-

__author__ = 'hupili'
__copyright__ = 'Unlicensed'
__license__ = 'Unlicensed'
__version__ = '0.1'
__maintainer__ = 'hupili'
__email__ = 'hpl1989@gmail.com'
__status__ = 'development'

from nose.tools import ok_
from nose.tools import eq_
from test_config import *
from test_utils import *

sys.path = [DIR_TEST] + sys.path

from multiret import multi

def is_success1(err_msg):
    '''
    ``is_success2`` is the upgraded version
    '''
    if err_msg == '':
        return True
    else:
        return False

def is_success2(err_msg):
    '''
    The upgrade:

       * We piggyback the ``err_msg`` to our client.
       The client can look into the problem upon a ``False`` return.

    This version is not decorated by "multi". It breaks client codes.
    '''
    if err_msg == '':
        return True, err_msg
    else:
        return False, err_msg

@multi
def is_success3(err_msg):
    '''
    Same as is_success2 but decorated with "multi".

    Former simple invokation is preserved.
    '''
    if err_msg == '':
        return True, err_msg
    else:
        return False, err_msg

@multi
def return_a_tuple(count):
    '''
    Return a tuple (1, 2, ... count)
    '''
    return tuple(range(1, (count+1)))

class TestMulti(TestBase):

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_normal_client_success_1(self):
        eq_(is_success1(''), True)
        eq_(is_success1('hello'), False)
        eq_(is_success1('succeed'), False)
        if is_success1('you can not come here'):
            assert(False)
        ok_(is_success1(''))

    def test_normal_client_success_2(self):
        # The client codes are broken by is_success2
        eq_(is_success2(''), (True, ''))
        eq_(is_success2('hello'), (False, 'hello'))
        eq_(is_success2('succeed'), (False, 'succeed'))

    def test_advanced_client_success_2(self):
        ret, msg = is_success2('')
        eq_(ret, True)
        eq_(msg, '')
        ret, msg = is_success2('hello')
        eq_(ret, False)
        eq_(msg, 'hello')

    def test_normal_client_success_3(self):
        # The client codes are preserved by is_success3
        eq_(is_success3(''), True)
        eq_(is_success3('hello'), False)
        eq_(is_success3('succeed'), False)

    def test_advanced_client_success_3(self):
        ret, msg = is_success3('')
        eq_(ret, True)
        eq_(msg, '')
        ret, msg = is_success3('hello')
        eq_(ret, False)
        eq_(msg, 'hello')

    def test_success_3_wiht_extra_expected_variables(self):
        ret, msg, ex1, ex2 = is_success3('hello')
        eq_(ret, False)
        eq_(msg, 'hello')
        eq_(ex1, None)
        eq_(ex2, None)

    def test_more_returned_variables(self):
        r1 = return_a_tuple(4)
        eq_(r1, 1)
        r1, r2 = return_a_tuple(4)
        eq_(r1, 1)
        eq_(r2, 2)
        r1, r2, r3, r4 = return_a_tuple(4)
        eq_(r3, 3)
        eq_(r4, 4)
        r1, r2, r3, r4, r5 = return_a_tuple(4)
        eq_(r5, None)
        eq_(return_a_tuple(1) + return_a_tuple(2), 2)

    #TODO:
    #    When the function is assigned to another variable,
    #    the name may be different.
    #
    #def test_advanced_client_success_2_decorated(self):
    #    func = multi(is_success2)
    #    ret, msg = func('')
    #    eq_(ret, True)
    #    eq_(msg, '')
    #    ret, msg = func('hello')
    #    eq_(ret, False)
    #    eq_(msg, 'hello')
