import os
import tkinter
from tkinter import filedialog

class load_data(object):
    def load_txt():
        root = tkinter.Tk()
        root.withdraw()
        filePath = filedialog.askopenfilename()
        data = []
        with open(filePath) as f:
            for line in f.readlines():
                data.append(line.strip('\n'))
        return data
    
    def load_txt_gui(a, filePath):
        data = []
        with open(filePath) as f:
            for line in f.readlines():
                data.append(line.strip('\n'))
        return data
    
class save_data(object):
    def write_txt_gui(a, data,  filepath):
        with open(filepath,"w") as f:
            f.write(data)
    
def get_char_num(data:list)->dict:
    charset = set(data)
    result = {}
    for c in charset:
        result[c] = data.count(c)
    return result