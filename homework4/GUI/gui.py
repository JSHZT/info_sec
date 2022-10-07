import PyQt5 as qt
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from mainwin import Ui_MainWindow
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), ".")))
from utils import DataOP, Caesar_code, XOR_code, hill_code, Playfair

class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.URL_show.setText('./')
        self.URL_show.setReadOnly(True)
        self.notvalid = True
        self.hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
        self.xor_key = 'default'
        self.caesar_key = 5
        self.chose_button.clicked.connect(self.get_url)
        self.encode_button_d.clicked.connect(self.chose_way_d)
        self.encode_button_file.clicked.connect(self.chose_way_file)
        
    def chose_way_file(self):
        way = self.comboBox_file.currentText()
        if way == 'Caecar(凯撒加密解密)':
            self.caesar_encode(isfile=True)
        elif way == "XOR(异或加密解密)":
            pass
        elif way == "Playfair(皮菲特加密解密)":
            pass
        elif way == "Hill(希尔加密解密)":
            pass
    
    def chose_way_d(self):
        pass
    
    def get_url(self):
        directory = QtWidgets.QFileDialog.getOpenFileName(None,  "选取文件","./", "Text Files (*.txt)")[0]
        self.URL_show.setText(directory)
        self.filepath = directory
        
    def caesar_encode(self, isfile:bool):
        if isfile:
            data = DataOP.load_data().load_txt_gui(self.filepath)
            self.caesar_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.caesar_key
            result_list = Caesar_code.Caesar_code().Encryption(data=data, key=self.caesar_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_file.setText(self.result)
        else:
            data = DataOP.load_data().load_txt_gui(self.input)
            self.caesar_key = int(self.input_key_file.toPlainText()) if self.input_key_file.toPlainText() else self.caesar_key
            result_list = Caesar_code.Caesar_code().Encryption(data=data, key=self.caesar_key)
            self.result = ''
            for line in result_list:
                self.result += line
            self.textBrowser_file.setText(self.result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())