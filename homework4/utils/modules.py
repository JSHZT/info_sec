from asyncio.windows_events import NULL
from pickle import NONE
import re
import os

class user_info(object):
    def __init__(self, src, code=NONE) -> None:
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
