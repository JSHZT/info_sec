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
    
class save_data(object):
    def write_txt():
        pass