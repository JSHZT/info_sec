import PyQt5 as qt
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".")))
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(os.path.abspath(__file__))) + os.path.sep + "."))

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from mainwin import Ui_MainWindow
from utils import DataOP, Caesar_code, XOR_code, hill_code, Playfair

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.result = ''
        self.result_en = ''
        self.URL_show.setText('./')
        self.URL_show.setReadOnly(True)
        self.notvalid = True
        self.hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
        self.xor_key = 'default'
        self.caesar_key = 5
        self.chose_button.clicked.connect(self.get_url)
        self.encode_button_d.clicked.connect(self.chose_way_d)
        self.encode_button_file.clicked.connect(self.chose_way_file)
        self.decode_button_d.clicked.connect(self.chose_way_d_de)
        self.decode_button_file.clicked.connect(self.chose_way_file_de)
        self.ouput_file_de.clicked.connect(self.output_file_dec)
        self.ouput_file_en.clicked.connect(self.output_file_enc)

    def output_file_enc(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(None,  "选取文件","./", "Text Files (*.txt)")[0]
        if directory == '':
            return
        DataOP.save_data().write_txt_gui(self.result_en, directory)
        
    def output_file_dec(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(None,  "选取文件","./", "Text Files (*.txt)")[0]
        if directory == '':
            return
        DataOP.save_data().write_txt_gui(self.result, directory)
        
    def chose_way_file(self):
        way = self.comboBox_file.currentText()
        if way == 'Caecar(凯撒加密解密)':
            self.caesar_encode(isfile=True)
        elif way == "XOR(异或加密解密)":
            self.XOR_encode(isfile=True)
        elif way == "Playfair(皮菲特加密解密)":
            self.playfair_encode(isfile=True)
        elif way == "Hill(希尔加密解密)":
            self.hill_encode(isfile=True)
    
    def chose_way_d(self):
        way = self.comboBox_d.currentText()
        if way == 'Caecar(凯撒加密解密)':
            self.caesar_encode(isfile=False)
        elif way == "XOR(异或加密解密)":
            self.XOR_encode(isfile=False)
        elif way == "Playfair(皮菲特加密解密)":
            self.playfair_encode(isfile=False)
        elif way == "Hill(希尔加密解密)":
            self.hill_encode(isfile=False)
            
    def chose_way_file_de(self):
        way = self.comboBox_file.currentText()
        if way == 'Caecar(凯撒加密解密)':
            self.caesar_decode(isfile=True)
        elif way == "XOR(异或加密解密)":
            self.XOR_decode(isfile=True)
        elif way == "Playfair(皮菲特加密解密)":
            self.playfair_decode(isfile=True)
        elif way == "Hill(希尔加密解密)":
            self.hill_decode(isfile=True)
    
    def chose_way_d_de(self):
        way = self.comboBox_d.currentText()
        if way == 'Caecar(凯撒加密解密)':
            self.caesar_decode(isfile=False)
        elif way == "XOR(异或加密解密)":
            self.XOR_decode(isfile=False)
        elif way == "Playfair(皮菲特加密解密)":
            self.playfair_decode(isfile=False)
        elif way == "Hill(希尔加密解密)":
            self.hill_decode(isfile=False)
    
    def get_url(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(None,  "选取文件","./", "Text Files (*.txt)")[0]
        self.URL_show.setText(directory)
        self.filepath = directory
        
    def print_charnum(self, isfile, dict_:dict):
        str_ = ''
        for key,value in dict_.items():
            str_ +="(" + str(key) + ": " + str(value) + ") "
        if isfile:
            self.char_num_file.setText(str_)
        else:
            self.char_num_d.setText(str_)
            
    def caesar_encode(self, isfile:bool):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.caesar_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.caesar_key
            result_list = Caesar_code.Caesar_code().Encryption(data=data, key=self.caesar_key)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_file.setText(self.result_en)
            self.caesar_key = 5
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            self.caesar_key = int(self.input_key_d.toPlainText()) if self.input_key_d.toPlainText() else self.caesar_key
            result_list = Caesar_code.Caesar_code().Encryption(data=data, key=self.caesar_key)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_d.setText(self.result_en)
            self.caesar_key = 5
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
            
    def XOR_encode(self, isfile):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.xor_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.xor_key
            result_list = XOR_code.XOR_code().Encryption(data=data, key=self.xor_key)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_file.setText(self.result_en)
            self.xor_key = 'default'
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            self.xor_key = int(self.input_key_d.toPlainText()) if self.input_key_d.toPlainText() else self.xor_key
            result_list = XOR_code.XOR_code().Encryption(data=data, key=self.xor_key)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_d.setText(self.result_en)
            self.xor_key = 'default'
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
    
    def playfair_encode(self, isfile):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            result_list = Playfair.Playfair_code().Encryption(data=data)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_file.setText(self.result_en)
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            result_list = Playfair.Playfair_code().Encryption(data=data)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_d.setText(self.result_en)
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
            
    def hill_encode(self, isfile:bool):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.hill_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.hill_key
            result_list = hill_code.hill().Encryption(data=data, key=self.hill_key)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_file.setText(self.result_en)
            self.hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            self.hill_key = int(self.input_key_d.toPlainText()) if self.input_key_d.toPlainText() else self.hill_key
            result_list = hill_code.hill().Encryption(data=data, key=self.hill_key)
            self.result_en = ''
            for line in result_list:
                self.result_en += line
            self.textBrowser_d.setText(self.result_en)
            self.hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
            char_dict = DataOP.get_char_num(self.result_en)
            self.print_charnum(isfile, char_dict)
    
    def caesar_decode(self, isfile:bool):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.caesar_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.caesar_key
            result_list = Caesar_code.Caesar_code().Decrypt(data=data, key=self.caesar_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_file.setText(self.result)
            self.caesar_key = 5
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            self.caesar_key = int(self.input_key_d.toPlainText()) if self.input_key_d.toPlainText() else self.caesar_key
            result_list = Caesar_code.Caesar_code().Decrypt(data=data, key=self.caesar_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_d.setText(self.result)
            self.caesar_key = 5
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
            
    def XOR_decode(self, isfile):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.xor_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.xor_key
            result_list = XOR_code.XOR_code().Decrypt(data=data, key=self.xor_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_file.setText(self.result)
            self.xor_key = 'default'
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            self.xor_key = int(self.input_key_d.toPlainText()) if self.input_key_d.toPlainText() else self.xor_key
            result_list = XOR_code.XOR_code().Decrypt(data=data, key=self.xor_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_d.setText(self.result)
            self.xor_key = 'default'
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
    
    def playfair_decode(self, isfile):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            result_list = Playfair.Playfair_code().Decrypt(data=data)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_file.setText(self.result)
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            result_list = Playfair.Playfair_code().Decrypt(data=data)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_d.setText(self.result)
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
            
    def hill_decode(self, isfile:bool):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.hill_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.hill_key
            result_list = hill_code.hill().Decrypt(data=data, key=self.hill_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_file.setText(self.result)
            self.hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)
        else:
            self.input = self.input_str_d.toPlainText()
            data = [self.input]
            self.hill_key = int(self.input_key_d.toPlainText()) if self.input_key_d.toPlainText() else self.hill_key
            result_list = hill_code.hill().Decrypt(data=data, key=self.hill_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_d.setText(self.result)
            self.hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
            char_dict = DataOP.get_char_num(self.result)
            self.print_charnum(isfile, char_dict)

