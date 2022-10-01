###############################################################
# Implement pairs with functions.(S2.2)
# Pairs: the behavior we require to implement a pair is that it
# glues two values together. Stated as a behavior condition:
# If a pair p was constructed from values x and y, then select(p, 0) returns x, and select(p, 1) returns y.
# we can implement two functions pair and select that fulfill this description just as well as a two-element list.
def pair(x, y):
    '''return a function that represents a pair.'''
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
        return get

def select(p, i):
    '''return the element at index i of pair p.'''
    return p(i)

#例子
p = pair(1,2) #相当于 p = [1,2]
select(p, 1)  # p[1]
select(p, 0)  # p[0]

###############################################################
# Inplement sequences(linked lists) with pairs(S2.3)
# The linked list can store a sequence of values in order, and we can get its length and do element selection.
empty = 'empty'
def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

def link(first, rest):
    """Construct a linked list from its first element and the rest."""
    assert is_link(rest), "rest must be a linked list."
    return [first, rest] #这里为了简便起见，仍用两个元素的list来代表pair，而不用function implemented的pair

def first(s):
    """Return the first element of a linked list s."""
    assert is_link(s), "first only applies to linked lists."
    assert s != empty, "empty linked list has no first element."
    return s[0]

def rest(s):
    """Return the rest of the elements of a linked list s."""
    assert is_link(s), "rest only applies to linked lists."
    assert s != empty, "empty linked list has no rest."
    return s[1] 

def len_link(s):
    """Return the length of linked list s."""
    length = 0
    while s != empty:
        s, length = rest(s), length + 1
    return length

def getitem_link(s, i):
    """Return the element at index i of linked list s."""
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

#例子
four = link(1, link(2, link(3, link(4, empty)))) # 相当于four = [1, 2, 3, 4]
len_link(four) #len(four) = 4
getitem_link(four, 1) #four[1]

#例子
b = [1]
b.append(b)
b # [1, [...]]
is_link(b) #RecursionError: maximum recursion depth exceeded in comparison
#question: lst = [1,lst], 那么lst是一个linked list吗？
#按照定义，lst is a linked list iff lst( the rest of the list) is a linked list. (这似乎陷入了某种循环的怪圈)


#########################################################
# Implement mutable linked list with inmutable linked list & functions (see S2.4.7 for more details)
# 上面的implement的list是inmutable的，无法在同一片内存里对已有的list进行修改。
# 我们using functions with local states to implement a mutable list.
# We will represent a mutable linked list by a function that has a linked list as its local state. Lists need to have an identity, like any mutable value.
def mutable_link():
    """
    Return a functional implementation of a mutable linked list.
    Our mutable list will respond to five different messages: 
    len, getitem, push_first, pop_first, and str. 
    The first two implement the behaviors of the sequence abstraction. 
    The next two add or remove the first element of the list. 
    The final message returns a string representation of the whole linked list.
    """
    contents = empty #开辟一片内存，存储这个list
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ", ")
    return dispatch


def join_link(s, separator):
        """Return a string of all elements in s separated by separator."""
        if s == empty:
            return ""
        elif rest(s) == empty:
            return str(first(s))
        else:
            return str(first(s)) + separator + join_link(rest(s), separator)





###############################################################
# Implement dictionaried with lists
# In this case, we use a list of key-value pairs to store the contents of the dictionary. Each pair is a two-element list.
def dictionary():
        """Return a functional implementation of a dictionary."""
        records = []
        def getitem(key):
            matches = [r for r in records if r[0] == key]
            if len(matches) == 1:
                key, value = matches[0]
                return value
        def setitem(key, value):
            nonlocal records
            non_matches = [r for r in records if r[0] != key]
            records = non_matches + [[key, value]]
        def dispatch(message, key=None, value=None):
            if message == 'getitem':
                return getitem(key)
            elif message == 'setitem':
                setitem(key, value)
        return dispatch


# 例子
d = dictionary()
d('setitem', 3, 9)
d('setitem', 4, 16)
d('getitem', 3)
d('getitem', 4)




############################################################
# Message passing (S 2.4)
# 在implement mutable list和dictionary的过程中，我们都用到了dispatch函数

# Encapsulates the logic for all operations on a data value within one function that responds to different messages, 
# is a discipline called message passing. 
# A program that uses message passing defines dispatch functions, each of which may have local state, 
# and organizes computation by passing "messages" as the first argument to those functions. 
# The messages are strings that correspond to particular behaviors.

# The built-in dictionary data type provides a general method for looking up a value for a key. 
# Instead of using conditionals to implement dispatching, we canuse dictionaries with string keys.

# 将dictionary的例子改成用dictionary dispatch来实现
def dictionary_dispatch():
        """Return a functional implementation of a dictionary."""
        records = []
        def getitem(key):
            matches = [r for r in records if r[0] == key]
            if len(matches) == 1:
                key, value = matches[0]
                return value
        def setitem(key, value):
            nonlocal records
            non_matches = [r for r in records if r[0] != key]
            records = non_matches + [[key, value]]
        dispatch = {'getitem': getitem, 'setitem': setitem} #dispatch 不是带有分支的函数了，而是dictionary
        return dispatch



# 例子
d = dictionary_dispatch()
d['setitem'](3,9)
d['setitem'](4,16)
d['getitem'](3)
d['getitem'](4)




###########################################################
# Implementing Classes and Objects using dictionaries
# instance
def make_instance(cls): # cls是instance所属的class
        """Return a new object instance, which is a dispatch dictionary."""
        def get_value(name):
            if name in attributes: #若name是instance attribute
                return attributes[name]
            else:
                value = cls['get'](name) # In get, if name does not appear in the local attributes dictionary, then it is looked up in the class.
                return bind_method(value, instance) #If the value returned by cls is a function, it must be bound to the instance.
        def set_value(name, value):
            attributes[name] = value
        attributes = {}
        instance = {'get': get_value, 'set': set_value}
        return instance


def bind_method(value, instance):
        """Return a bound method if value is callable, or value otherwise."""
        if callable(value):
            def method(*args):
                return value(instance, *args)
            return method
        else:
            return value


#class
def make_class(attributes, base_class=None):
        """
        Return a new class, which is a dispatch dictionary.
        our attributes dictionary much like __dict__.
        an instance of any user-defined class has a special attribute __dict__ that stores the local instance attributes for that object in a dictionary.
        """
        def get_value(name):
            if name in attributes:
                return attributes[name]
            elif base_class is not None:
                return base_class['get'](name)
        def set_value(name, value):
            attributes[name] = value
        def new(*args):
            return init_instance(cls, *args) #classes can create new instances, and they apply their __init__ constructor function immediately after instance creation.
        cls = {'get': get_value, 'set': set_value, 'new': new}
        return cls

def init_instance(cls, *args):
        """Return a new object with type cls, initialized with args."""
        instance = make_instance(cls)
        init = cls['get']('__init__')
        if init:
            init(instance, *args)
        return instance


# 例子
def make_account_class():
        """Return the Account class, which has deposit and withdraw methods."""
        interest = 0.02
        def __init__(self, account_holder):
            self['set']('holder', account_holder)
            self['set']('balance', 0)
        def deposit(self, amount):
            """Increase the account balance by amount and return the new balance."""
            new_balance = self['get']('balance') + amount
            self['set']('balance', new_balance)
            return self['get']('balance')
        def withdraw(self, amount):
            """Decrease the account balance by amount and return the new balance."""
            balance = self['get']('balance')
            if amount > balance:
                return 'Insufficient funds'
            self['set']('balance', balance - amount)
            return self['get']('balance')
        return make_class(locals()) #The final call to locals returns a dictionary with string keys that contains the name-value bindings in the current local frame.

Account = make_account_class() #The Account class is finally instantiated via assignment.
kirk_account = Account['new']('Kirk') #an account instance is created via the new message
kirk_account['get']('holder') #get messages passed to kirk_account retrieve properties and methods.
kirk_account['get']('deposit')(20)

#setting an attribute of an instance does not change the corresponding attribute of its class.
kirk_account['set']('interest', 0.04)
Account['get']('interest') #still 0.02

# inheritance
def make_checking_account_class():
        """Return the CheckingAccount class, which imposes a $1 withdrawal fee."""
        interest = 0.01
        withdraw_fee = 1
        def withdraw(self, amount):
            fee = self['get']('withdraw_fee')
            return Account['get']('withdraw')(self, amount + fee)
        return make_class(locals(), Account)
