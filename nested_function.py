#全局变量与局部变量
#若一个变量step，它只在某个函数step_function中被应用。但每次它被该函数应用时，都有可能改变该变量的状态。这种情况该怎么处理呢？

#法1，将该变量定义为global variable
#这样做的坏处是，让一个在其他地方用不到的变量定义为了全局变量
def step_function(step):
    make_use_step(step)
    step += 1 #change step
    return step


def make_use_step(step):
    print(step)
    return None



step = 0 #global variable
step = step_function(step) 
step = step_function(step)


#法2：Higher-order function
def f(step):
    def step_function():
        temp_step = step #这里使用temp_step的原因见：https://blog.csdn.net/sinat_40304087/article/details/115701595
        make_use_step(temp_step)
        temp_step += 1
        return f(temp_step)
    return step_function

a = f(0) #a: step = 0时的step_function
a = a() #a: step = 1时的step_function
a = a()




#法3，定义nonlocal variable.
def f(step):
    def step_function():
        nonlocal step 
        '''After executing nonlocal step, any
assignment statement with step on the left-hand side of = will not
bind step in the first frame of the current environment. Instead, it
will find the first frame in which step was already defined and re-bind
the name in that frame. If step has not previously been bound to a
value, then the nonlocal statement will give an error.'''
        make_use_step(step)
        step += 1
        return f(step)
    return step_function

a = f(0) #a: step = 0时的step_function
a = a() #a: step = 1时的step_function
a = a()





'''
Hint. If you're getting a local variable [var] reference before assignment error:

This happens because in Python, you aren't normally allowed to modify variables defined in parent frames. Instead of reassigning [var], the interpreter thinks you're trying to define a new variable within the current frame. We'll learn about how to work around this in a future lecture, but it is not required for this problem.

To fix this, you have two options:

1) Rather than reassigning [var] to its new value, create a new variable to hold that new value. Use that new variable in future calculations.

2) For this problem specifically, avoid this issue entirely by not using assignment statements at all. Instead, pass new values in as arguments to a call to announce_highest.
'''




