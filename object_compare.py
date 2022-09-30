#https://stackoverflow.com/questions/1227121/compare-object-instances-for-equality-by-their-attributes

class Card:
    def __init__(self, attack):
        self.attack = attack


card1 = Card(300)
card2 = Card(300)
card1 == card2 #False?!

#上述问题可能导致如下错误：
deck = [card1,card2]
card3 = Card(300)
deck.remove(card3)  #ValueError: list.remove(x): x not in list
#这给我们一个启示，当使用list.remove(item)函数时要注意，item和list中原有的元素是不是都能用 '==' 进行比较


#solution
class Card:
    def __init__(self, attack):
        self.attack = attack
    def __eq__(self, other): 
        if not isinstance(other, Card):
            # don't attempt to compare against unrelated types
            return NotImplemented
        else:
            return self.attack == other.attack

card1 = Card(300)
card2 = Card(300)
card1 == card2 #True as expected

# These are the so-called “rich comparison” methods,
# and are called for comparison operators in preference to __cmp__() below. 
# The correspondence between operator symbols and method names is as follows:
#  x<y calls x.__lt__(y), x<=y calls x.__le__(y), x==y calls x.__eq__(y), 
# x!=y and x<>y call x.__ne__(y), x>y calls x.__gt__(y), and x>=y calls x.__ge__(y).
