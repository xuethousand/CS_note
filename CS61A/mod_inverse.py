def mod_inverse(m,n):
    '''
    return the inverse of m mod n. If None, return -1.
    '''
    if m > n:
        return mod_inverse(m%n,n)
    
    def func(m1,n1,m2,n2,quotient,remainder):
        '''
        quotient = (m1,n1)*(m,n);remainder = (m2,n2)*(m,n)
        '''
        if remainder == 1:
            return (m2%n)
        elif remainder == 0:
            return -1
        else:
            temp = quotient//remainder
            return func(m2, n2, m1 - temp*m2, n1 - temp*n2, remainder, quotient%remainder)
    
    return func(1,0,-(n//m),1,m,n%m)
