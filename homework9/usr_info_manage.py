import hashlib
import argparse
import os
import sys
import json

class usr_info_manage(object):
    def __init__(self, args) -> None:
        self. sql = {}
        self.args = args
        if args.load:
            self.load()
        
    def generate_token(self, passw, salt)->str:
        return hashlib.md5((passw + salt).encode()).hexdigest()

    def register(self, usr, passw)->bool:
        try:
            salt = os.urandom(8)
            token = self.generate_token(passw, salt)
            self.sql[usr] = (token, salt)
            self.save()
            return True
        except:
            return False
    
    def login(self, usr, passw)->bool:
        if self.comp(hashlib.md5((passw + self.sql[usr][1]).encode()).hexdigest(), self.sql[usr][0]):
            return True
        return False
    
    def comp(self, token1, token2)->bool:
        return token1 == token2

    def save(self):
        js = json.dumps(self.sql)   
        file = open('data.txt', 'w')  
        file.write(js)  
        file.close()
        
    def load(self):
        file = open(self.args.path_to_data, 'r') 
        js = file.read()
        self.sql = json.loads(js)   
        file.close()
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # add the input folder arg 
    parser.add_argument('--load', type=bool, default=False, help="if true, load the user data from file")
    parser.add_argument('--path_to_data', type=str, default=os.path.dirname(__file__)+"/data.txt")
    args = parser.parse_args()
    manager = usr_info_manage(args)
    
    usr = "root"
    passw = "ajzhyadsa"
    
    usr_info_manage.register(usr=usr, passw=passw)