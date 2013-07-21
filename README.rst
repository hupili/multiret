multi-value-return pattern in Python
====================================

Related Pages
-------------

- http://stackoverflow.com/questions/17648591/multiple-value-return-pattern-in-python-not-tuple-list-dict-or-object-soluti

originally, you have:

.. code:: python

    def func():
        return 1
    print func() + func()

Then you decided that ``func()`` can return some extra information but you don't want to break previous code
(or modify them one by one).
It looks like

.. code:: python

    def func():
        return 1, "extra info"
    value, extra = func()
    print value # 1 (expected)
    print extra # extra info (expected)
    print func() + func() # (1, 'extra info', 1, 'extra info') (not expected, we want the previous behaviour, i.e. 2)

The previous codes (``func() + func()``) are broken. You have to fix it.

The solution is adapted from the answer,

http://stackoverflow.com/questions/17648591/multiple-value-return-pattern-in-python-not-tuple-list-dict-or-object-soluti/17680730#17680730
