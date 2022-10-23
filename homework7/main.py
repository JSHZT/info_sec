from RSA import *

def test1():
    e = 31
    n = 3599
    factors = factor(n)
    fn = (factors[0] - 1)*(factors[1] - 1)
    d = rsa_tool().match_d(e, fn)    
    print(d)


if __name__ == "__main__":
    test1()    #答案3031
    