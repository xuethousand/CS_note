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








'''Self-referencing functions will oftentimes employ helper functions that refer-
ence the outer function, such as the example to the right, print sums.'''
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n+k)
    return next_sum






'''
return 0 的必要性
'''
def all_nums(k,prefix=None):
    '''output all the binary number with k bits,prefix = None'''
    if(k == 0):
        print(prefix)
        return   #return nothing
    if(prefix == None):
        return (all_nums(k-1,0),all_nums(k-1,1))
    return (all_nums(k-1,prefix*10),all_nums(k-1,prefix*10+1))

def all_nums1(k,prefix=None):
    '''output all the binary number with k bits,prefix = None'''
    if(k == 0):
        print(prefix)
        return 0   #return 0
    if(prefix == None):
        return (all_nums1(k-1,0),all_nums1(k-1,1))
    return (all_nums1(k-1,prefix*10),all_nums1(k-1,prefix*10+1))

#python -i xxx.py
all_nums(2) #出错
all_nums(2) #正常





'''
 HW3: Anonymous factorial
 '''
#如何实现一个匿名递归函数？
#Is there any way to make an anonymous function call itself?
#Y-combinator, Y组合子
#待看
# lambda calculus



''' 
python 中清屏:
import os
os.system('cls||clear')

powershell 中清屏：
ctrl+L
'''



''' linked list'''
s = [2,3]
t = [5,6]
a = s + [t] #[t]: a list containing t, the content of [t] is a reference to the list t.
print(a)
a[2][0] = -1
print(a)
print(t) #t改变了？！





#UnboundLocalError: local variable 'f' referenced before assignment
#在g中定义了f function，python在编译时，知道这个local frame里有这个f(x),因此，它不会到global frame里去找。
#在运行y = f(x)时，它需要用到g(x)中的f(x)，但这个函数仍未定义，因此python会报错
def f(x):
    return x ** 2
def g(x):
    y = f(x)
    def f():
        return y + x
    return f
g(2)

#想想下面这个正常运行的情况，就能理解了
def f(x):
    return g(x)
def g(x):
    return x
f(1)











''' something about list'''
a = list(range(1,10)) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# a[start index:end index:step],其中end index是不包含的
a[0:9:2] #[1, 3, 5, 7, 9]
a[0:8:2] #[1, 3, 5, 7]
a[::-1] #[9, 8, 7, 6, 5, 4, 3, 2, 1]
a[:]  #creates a list that is identical to list a





'''mutable data'''
a = []
b1 = a # b1,a同时指向列表[]
b1 += [1]  #列表[]变为[1]
print('a: ', a) #a: [1],也改变了！


a = []
b2 = a # b2,a同时指向列表[]
b2 = b2 + [1]  # b2 指向列表[1], 但a仍然指向的是[]
print('a: ', a) # a:[]，a没有改变！
