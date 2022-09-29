import random
import re
import os

class XOR_code(object):
    def Encryption(data:list)->list:
        result = []
        return result
    
    def Decrypt(data:list)->list:
        result = []
        return result
    
    def str2int(self, string):
        str_byte = string.encode('utf-8')
        str_hex = str_byte.hex()
        str2int = int(str_hex,16)
        return str2int

    def int2str(self, interger):
        int2hex = hex(interger)
        hex2byte = bytes.fromhex(int2hex[2:])
        byte2str = hex2byte.decode('utf-8')
        return byte2str

    def encryption_line(self, string, key):
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

class user_info(object):
    def __init__(self, src, code=None) -> None:
        self.src = src
        self.code = code
    
class Caesar_code(object):
    def __init__(self, user:user_info) -> None:
        self.user = user_info
    
    # encode   
    def CaesarEncryption(self,cipher,shifting): 
        pass
    
    # decode 
    def CaesarDecrypt(self,cipher,shifting): 
        pass
