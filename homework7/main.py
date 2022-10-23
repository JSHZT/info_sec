from RSA import *

def test1():
    e = 31
    n = 3599
    factors = factor(n)
    fn = (factors[0] - 1)*(factors[1] - 1)
    d = rsa_tool().match_d(e, fn)    
    print(d)

def test2():
    e = 5
    n = 35
    C = 10
    factors = factor(n)
    fn = (factors[0] - 1)*(factors[1] - 1)
    d = rsa_tool().match_d(e, fn)    
    result = rsa_tool().decrypt(d=d, C=C, m=n)
    print(result)

if __name__ == "__main__":
    test1()    #答案3031
    test2()    #答案 5