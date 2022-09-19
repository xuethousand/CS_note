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













''' recursive function key points: 
有base case；
递归能在有限步终止，ie 每次能化简为一个更简单的情况。eg，棋盘跳马问题；
The base cases are then followed by one or more recursive calls. 函数体内可以有多个recursive calls
'''






'''
As another example of mutual recursion, consider a two-player game in which there are n initial pebbles 
on a table. The players take turns, removing either one or two pebbles from the table, and the player who
 removes the final pebble wins. Suppose that Alice and Bob play this game, each using a simple strategy:
1. Alice always removes a single pebble
2. Bob removes two pebbles if an even number of pebbles is on the table, and one otherwise
'''
#显然是法一更好，利用mutual内在的逻辑，减少了控制循环的语句使用
#法1，用mutual recursion
def play_alice(n):
        if n == 0:
            print("Bob wins!")
        else:
            play_bob(n-1)
            
def play_bob(n):
        if n == 0:
            print("Alice wins!")
        elif n%2 == 0:
            play_alice(n-2)
        else:
            play_alice(n-1)
play_alice(20)



#法2：我脑海中的initial idea
def alice(n):
    return 1

def bob(n):
    if n%2 == 0:
        return 2
    else:
        return 1

def who_win(n):
    assert n != 0, "初始不能是0个pebble"
    while(True):
        #alice
        n -= alice(n)
        if(n == 0):
            print('Alice wins!')
            return 0
        n -= bob(n)
        if(n == 0):
            print('Bob wins!')
            return 0

who_win(20)
who_win(0)




''' iteration is a special case of recursion.(从数学角度理解。反之也成立？）'''
