import random
import re
import os

class XOR_code(object):
    def Encryption(self, data:list, key:str)->list:
        result = []
        for i in data:
            result.append(self.encryption_line(i, key))
        return result

    def Decrypt(self, data:list, key:list)->list:
        result = []
        for i in data:
            result.append(self.decryption_line(i, key))
        return result

    def str2int(self, string:str)->int:
        str_byte = string.encode('utf-8')
        str_hex = str_byte.hex()
        str2int = int(str_hex,16)
        return str2int

    def int2str(self, interger:int)->str:
        int2hex = hex(interger)
        hex2byte = bytes.fromhex(int2hex[2:])
        byte2str = hex2byte.decode('utf-8')
        return byte2str

    def encryption_line(self, string, key)->str:
        string2int = self.str2int(string)
        key2int = self.str2int(key)
        len_str = len(str(string2int))
        len_len_str = len(str(len_str))
        len_key = len(str(key2int))
        key_multy = (len_str - len_key) if len_str >len_key else 0
        key_use = key2int * (10**(key_multy+1))
        encry_int = string2int ^ key_use
        return str(len_len_str)+str(len_str)+str(encry_int)

    def decryption_line(self, string, key):
        key2int = self.str2int(key)
        len_len_str = int(string[0])
        len_str = int(string[1:len_len_str+1])
        len_key = len(str(key2int))
        key_multy = (len_str - len_key) if len_str >len_key else 0
        key_use = key2int * (10**(key_multy+1))
        translate_string = string[len_len_str+1:]
        decry_int = int(translate_string) ^ key_use
        decry_str = self.int2str(decry_int)
        return decry_str
    
class Caesar_code(object):   
    def __init__(self):
        self.letterSList = ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z').split(',')
        self.letterBList = ('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z').split(',')

    def Encryption(self, data:list, key:int)->list:
        result = []
        for i in data:
            result.append(self.encryption_line(i, key))
        return result

    def Decrypt(self, data:list, key:list)->list:
        result = []
        for i in data:
            result.append(self.decryption_line(i, key))
        return result
    def encryption_line(self, string:str, key:int):    
        encryption =''
        for c in string:
            if c == ' ' or c =='_' or c=='＿':
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

    def decryption_line(self,string:str , key:int):    
        decrypt=''
        for c in string:
            if c ==' ' or c=='_' or c=='＿':
                decrypt += c
            else:
                if re.match(r'[a-z]', c) != None:
                    stringNum = self.letterSList.index(c)
                    stringShiftingNum = (stringNum - key) % 26
                    decrypt +=self.letterSList[stringShiftingNum]
                elif re.match(r'[A-Z]', c) != None:
                    stringNum = self.letterBList.index(c)
                    stringShiftingNum = (stringNum - key) % 26
                    decrypt +=self.letterBList[stringShiftingNum]
                else:
                    return None
        return decrypt 
