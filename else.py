def f():
    return 'cake'

print('cake') #输出cake
f()           #输出'cake'



'''
We can transform multiple-argument functions into a chain of single-argument, higher order functions by taking advantage of lambda expressions. 
For example, we can write a function f(x, y) as a different function g(x)(y). This is known as currying.
currying 的用处：
下面的例子中，当然可以用三个参数的函数func(f,g,x)来判断f(g(x)) is equal to g(f(x))。但我们想要得到的是func(x):判断f(g(x)) is equal to g(f(x)).这里用了currying的思想
'''
def compose1(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = compose1(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = compose1(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))



def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    def func(x):
        if(compose1(f,g)(x) == compose1(g,f)(x)):
            return True
        else:
            return False
    return func
