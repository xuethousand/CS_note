#我的做法，用时太长，不能通过test

def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.
    
    """
    if x<10:
        if x == 8:
            return 1
        else: 
            return 0
    return num_eights(x//10) + num_eights(x%10)
  
def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    
    """
    if(n <= 8):
        return n
    
    if((n-1)%8 == 0 or num_eights(n-1) != 0): #n-1是转折点
        return pingpong(n-2)
    else:
        if(pingpong(n-2) > pingpong(n-1)):
            return pingpong(n-2) - 2
        else:
            return pingpong(n-2) + 2
        

        
       
#助教的做法
def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    """
    def direction_change(index,direction):
        if(index%8 == 0 or num_eights(index) != 0):
            return not direction
        else:
            return direction
    def value_change(value,direction):
        if direction:
            return value+1
        else:
            return value-1

    

    def pingpong_helper(value,index,direction):
        if(index == n):
            return value
        return pingpong_helper(value_change(value,direction),index+1,direction_change(index+1,direction))

    return pingpong_helper(1,1,True)
