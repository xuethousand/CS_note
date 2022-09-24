# 银行存取钱，balance记录余额，withdraw函数表示取钱的动作。怎么实现这个操作呢？


# 法1: 将该balance定义为global variable
# 这样做的坏处是，定义为全局变量减少了封装性
balance = 20 #初始化

def withdraw(amount):
    balance -= amount
    return 

withdraw(10)
withdraw(5)
balance


# 法2: Higher-order function
def func(balance):
    def withdraw(amount):
        if amount == 0: #打印balance
            print(balance)
        balance_ = balance - amount #用到了balance_ 作为临时变量
        return func(balance_)
    return withdraw

temp = func(20)
temp = temp(10)
temp = temp(5)
temp = temp(0)
    

#法3: 定义nonlocal variable. See http://composingprograms.com/pages/24-mutable-data.html#local-state for more information
def func(balance):
    def withdraw(amount):
        nonlocal balance
        if amount == 0: #打印balance
            print(balance)
        balance = balance - amount #用到了balance_ 作为临时变量
        return func(balance)
    return withdraw

temp = func(20)
temp = temp(10)
temp = temp(5)
temp = temp(0)

'''
Hint. If you're getting a local variable [var] reference before assignment error:
This happens because in Python, you aren't normally allowed to modify variables defined in parent frames.
Instead of reassigning [var], the interpreter thinks you're trying to define a new variable within the current frame.
'''

'''
Python also has an unusual restriction regarding the lookup of names: withinthe body of a function, all instances of a name must refer to the same frame.
As a result, Python cannot look up the value of a name in a non-local frame, then bind that same name in the local frame, because the same name would be accessed in two different frames in the same function.
'''

'''After executing nonlocal 'balance', any
assignment statement with 'balance' on the left-hand side of = will not
bind 'balance' in the first frame of the current environment. Instead, it
will find the first frame in which 'balance' was already defined and re-bind
the name in that frame. If 'balance' has not previously been bound to a
value, then the nonlocal statement will give an error.'''





# 法4: 利用dictionary让withdraw函数的定义与balance的定义在同一frame下
'''By storing the balance in the dispatch
dictionary rather than in the account frame directly, we avoid the need for
nonlocal statements in deposit and withdraw.'''
def account(initial_balance):
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)
def check_balance(account):
    return account['balance']

a = account(20)
withdraw(a, 10)
withdraw(a,5)
check_balance(a)









