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
b1 += [1]  #列表[]变为[1]，change local bindings
print('a: ', a) #a: [1],也改变了！


a = []
b2 = a # b2,a同时指向列表[]
b2 = b2 + [1]  # b2 指向列表[1], 但a仍然指向的是[]，re-bound existing names
print('a: ', a) # a:[]，a没有改变！








# tuples is unmutable. However, you can "change" it in some sense.
# An immtable sequence may still change if it contains a mutable value as an element
a = (3,4)
a[1] = 5 #error

a = (3,[4])
a[1][0] = 5
a









# mutable object as default argument (Dangerous)
# a default argument value is part of a function value, not generated by a call.
# everytime you call the function without argument, s will be bound to the same default value. If the default value is 
#mutable, and you mutate it in the middle of your function, then that change will still be around the next time 
#you can the function and you get that same default argument value.

def f(s=[]):
    s.append(5)
    return len(s)
     
f() #1
f() #2
f([]) #1
f()  #3



def f():
    if not ('s' in locals().keys()): # 判断变量s有没有被定义
        s = []
    s.append(5)
    return len(s)
     
f() #1
f() #2
f() #3










r = range(3,6)
ri = iter(r)


for i in ri:
    print(i) #print 3,4,5
for i in ri: # a consequence of using an iterator in a for statement. 
    print(i) #print nothing


for i in ri:
    print(i) #print 3,4,5
for i in ri: # using iterable value.
    print(i) #print 3,4,5 again.


    
    
    
    
    
    
# append 和 extend 的区别
x = [200, 300]
x.append(x)
x #[200, 300, [...]]
x = [200, 300]
x.extend(x) 
x #[200, 300, 200, 300]







# 计算fib()被运行了几次
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2)+fib(n-1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count = 0
    return counted

fib = count(fib)
fib(2)
fib.call_count

# 可以在tutor上运行看看。
# 1. counted is a function, also an instance of class ‘function’. The class ‘function’ has been defined by python already. So we can use counted.call_count
# 2. Yes, the fib(n-2) points to the new fib (counted). 
# The name f has been bound to the original fib function, while the name fib has been bound to counted, “fib=count(fib)”. So, "return f(*args)" calls original fib funcion, and the original fib function calls fib(n-1) and fib(n-2), but the name fib no longer bound to the original fib function, then we are actually calling counted(n-1) and counted(n-2).








# something about repr, str
class Bear:
    def __init__(self):
        self.__repr__ = lambda : 'self.repr'
        self.__str__ = lambda : 'self.str'
    def __repr__(self):
        return 'class.repr' # an error, considering eval(repr(Bear())) should be Bear(), here should return Bear() instead of 'class.repr'
    def __str__(self):
        return 'class.str'

oski = Bear() 
print(oski)     #class.str
print(str(oski))    #class.str
print(repr(oski))   #class.repr
print(oski.__str__()) #self.str
print(oski.__repr__()) #self.repr


#事实上，python中的str, repr函数是这样的：
def repr(x):
    return type(x).__repr__(x) #返回x所属class中的__repr__

def str(x):
    t = type(x)
    if hasattr(t, '__str__'): 
        return t.__str__(x) #若x所属class中有__str__, 返回该函数
    else:
        return repr(x) #若x所属class中没有__str__, 返回class中的__repr__
    
    
    
    
    
    
    
    
    
    
   

#If you iterate over a list, but change the contents of that list at the same time, 
# you may not visit all the elements. 
# This can be prevented by making a copy of the list.
# You can either use a list slice, or use the built-in list function.
lst = [1,2,3,4] # a list slice
lst[:] #[1, 2, 3, 4]
list(lst) #[1, 2, 3, 4], the built-in list function
lst[:] is not lst and list(lst) is not lst #True




# 下面请看一个例子
a = [1]
b = [2,3]
lst = [a, b]

for i in range(len(lst)):
    if lst[i] == [1]: # cause error
        del lst[i] 


# 可以做如下修改
a = [1]
b = [2,3]
lst = [a, b]
lst_copy = lst[:]
for i in range(len(lst_copy)):
    if lst_copy[i] == [1]:
        del lst[i]


# Notice: del lst[i] 这样的修改不会影响lst_copy, 但看下面的例子
a = [1]
b = [2,3]
lst = [a, b]
lst_copy = lst[:]
lst[0].pop()
lst_copy # changed!
















# 在class外定义属于class的函数
class X: 
    def func1(self,x):
        return x**2

x = X()
x.func1(2)
#我们想要修改instance x的func1, 让它返回x**3, how to do it?
def func2(x): return x ** 3
x.func1 = func2
print(x.func1(2)) # prints 8

#如果要修改class X的func1呢？
def func2(self,x): return x ** 3
X.func1 = func2
x.func1(2) #print 8!
