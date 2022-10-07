import re


class Caesar_code(object):
    def __init__(self):
        self.letterSList = (
            'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').split(',')
        self.letterBList = (
            'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z').split(',')

    def Encryption(self, data: list, key: int) -> list:
        result = []
        for i in data:
            result.append(self.encryption_line(i, key))
        return result

    def Decrypt(self, data: list, key: list) -> list:
        result = []
        for i in data:
            result.append(self.decryption_line(i, key))
        return result

    def encryption_line(self, string: str, key: int):
        encryption = ''
        for c in string:
            if c == ' ' or c == '_' or c == '＿':
                encryption += c
            else:
                if re.match(r'[a-z]', c) != None:
                    stringNum = self.letterSList.index(c)
                    stringShiftingNum = (stringNum + key) % 26
                    encryption += self.letterSList[stringShiftingNum]
                elif re.match(r'[A-Z]', c) != None:
                    stringNum = self.letterBList.index(c)
                    stringShiftingNum = (stringNum + key) % 26
                    encryption += self.letterBList[stringShiftingNum]
                else:
                    return None
        return encryption

    def decryption_line(self, string: str, key: int):
        decrypt = ''
        for c in string:
            if c == ' ' or c == '_' or c == '＿':
                decrypt += c
            else:
                if re.match(r'[a-z]', c) != None:
                    stringNum = self.letterSList.index(c)
                    stringShiftingNum = (stringNum - key) % 26
                    decrypt += self.letterSList[stringShiftingNum]
                elif re.match(r'[A-Z]', c) != None:
                    stringNum = self.letterBList.index(c)
                    stringShiftingNum = (stringNum - key) % 26
                    decrypt += self.letterBList[stringShiftingNum]
                else:
                    return None
        return decrypt