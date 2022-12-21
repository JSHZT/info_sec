import hashlib
import argparse
import os
import sys


class usr_info_manage(object):
    def __init__(self, args) -> None:
        self. sql = {}
        
    def generate_token(self, passw, salt)->str:
        return hashlib.md5((passw + salt).encode()).hexdigest()

    def register(self, usr, passw):
        pass
    
    def login(self):
        pass
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # add the input folder arg 
    parser.add_argument('--load', type=bool, default=False, help="if true, load the user data from file")
    parser.add_argument('--path_to_data', type=str, default=os.path.dirname(__file__)+"data.txt")
    args = parser.parse_args()
    manager = usr_info_manage(args)
    
    usr = "root"
    passw = "ajzhyadsa"
    
    usr_info_manage.register(usr=usr, passw=passw)