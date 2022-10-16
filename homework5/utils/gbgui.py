import tkinter
import tkinter.messagebox
from tkinter.messagebox import *
from tkinter import *

from tkinter import ttk
import threading
import random
def gbgui():
    IP_table = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

    _IP_table = [40, 8, 48, 16, 56, 24, 64, 32,
                 39, 7, 47, 15, 55, 23, 63, 31,
                 38, 6, 46, 14, 54, 22, 62, 30,
                 37, 5, 45, 13, 53, 21, 61, 29,
                 36, 4, 44, 12, 52, 20, 60, 28,
                 35, 3, 43, 11, 51, 19, 59, 27,
                 34, 2, 42, 10, 50, 18, 58, 26,
                 33, 1, 41, 9, 49, 17, 57, 25]

    s = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

         [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

         [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

         [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

         [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

         [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

         [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

         [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

    P = [16, 7, 20, 21,
         29, 12, 28, 17,
         1, 15, 23, 26,
         5, 18, 31, 10,
         2, 8, 24, 14,
         32, 27, 3, 9,
         19, 13, 30, 6,
         22, 11, 4, 25]

    change1 = [57, 49, 41, 33, 25, 17, 9,
               1, 58, 50, 42, 34, 26, 18,
               10, 2, 59, 51, 43, 35, 27,
               19, 11, 3, 60, 52, 44, 36,
               63, 55, 47, 39, 31, 23, 15,
               7, 62, 54, 46, 38, 30, 22,
               14, 6, 61, 53, 45, 37, 29,
               21, 13, 5, 28, 20, 12, 4]

    change2 = [14, 17, 11, 24, 1, 5,
               3, 28, 15, 6, 21, 10,
               23, 19, 12, 4, 26, 8,
               16, 7, 27, 20, 13, 2,
               41, 52, 31, 37, 47, 55,
               30, 40, 51, 45, 33, 48,
               44, 49, 39, 56, 34, 53,
               46, 42, 50, 36, 29, 32]

    extend = [32, 1, 2, 3, 4, 5,
              4, 5, 6, 7, 8, 9,
              8, 9, 10, 11, 12, 13,
              12, 13, 14, 15, 16, 17,
              16, 17, 18, 19, 20, 21,
              20, 21, 22, 23, 24, 25,
              24, 25, 26, 27, 28, 29,
              28, 29, 30, 31, 32, 1]

    d = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]


    class DES():
        def __init__(self):
            pass

        def keyfirstchange(self, key):
            return_list = ''
            for i in range(56):
                return_list += key[change1[i] - 1]
            return return_list

        def keysecondchange(self, key):
            return_list = ''
            for i in range(48):
                return_list += key[change2[i] - 1]
            return return_list

        def codefirstchange(self, code):
            changed_code = ''
            for i in range(64):
                changed_code += code[IP_table[i] - 1]
            return changed_code

        def functionE(self, code):
            return_list = ''
            for i in range(48):
                return_list += code[extend[i] - 1]
            return return_list

        def codeyihuo(self, code, key):
            code_len = len(key)
            return_list = ''
            for i in range(code_len):
                if code[i] == key[i]:
                    return_list += '0'
                else:
                    return_list += '1'
            return return_list

        def functions(self, key):
            return_list = ''
            for i in range(8):
                row = int(str(key[i * 6]) + str(key[i * 6 + 5]), 2)
                raw = int(str(key[i * 6 + 1]) + str(key[i * 6 + 2]) + str(key[i * 6 + 3]) + str(key[i * 6 + 4]), 2)
                return_list += self.changtos(s[i][row][raw], 4)
            return return_list

        def changtos(self, o, lens):
            return_code = ''
            for i in range(lens):
                return_code = str(o >> i & 1) + return_code
            return return_code

        def functionp(self, code):
            return_list = ''
            for i in range(32):
                return_list += code[P[i] - 1]
            return return_list

        def nichange(self, code):

            return_list = ''
            for i in range(64):
                return_list += code[_IP_table[i] - 1]
            return return_list

        def getkey(self, key):
            b = []
            key_l = key[0:28]
            key_r = key[28:56]
            for j in range(16):
                key_l = key_l[d[j]:28] + key_l[0:d[j]]
                key_r = key_r[d[j]:28] + key_r[0:d[j]]
                run_key = key_l + key_r
                key_y = self.keysecondchange(run_key)
                b.append(key_y)
            return b

        def changekey(self, key, i):
            changekey = list(map(int, key))
            j = 0
            while j < (i + 1):
                change = random.randint(1, 63)
                changekey[change] = ((changekey[change] + 1) % 2)
                j += 1
            return str(changekey)

        def changecode(self, code, i):
            changecode = list(map(int, code))
            j = 0
            while j < (i + 1):
                change = random.randint(1, 43)
                changecode[change] = ((changecode[change] + 1) % 2)
                j += 1
            return str(changecode)
    
    def encrypt(from_code, key):
        changekey = key
        des = DES()
        code = des.codefirstchange(from_code)
        key = des.keyfirstchange(key)
        run_code = ''
        output = ''
        key_code = des.getkey(key)
        code_l = code[0:32]
        code_r = code[32:64]
        for j in range(16):
            code = code_r
            code_r = des.functionE(code_r)
            key_y = key_code[j]
            code_r = des.codeyihuo(code_r, key_y)
            code_r = des.functions(code_r)
            code_r = des.functionp(code_r)
            code_r = des.codeyihuo(code_l, code_r)
            code_l = code
        code_l, code_r = code_r, code_l
        run_code = code_l + code_r
        output += des.nichange(run_code)
        return output

    def from_codetocode(key, code):
        des = DES()
        for i in range(64):
            avg = 0
            print('密钥不变，明文改变' + str(i + 1) + '位')
            for j in range(100):
                change = 0
                changecode = encrypt(des.changecode(code, i),
                                     '0011000100110010001100110011010000110101001101100011011100111000')
                for a in range(64):
                    if changecode[a] != code[a]:
                        change += 1
                avg = avg + change
            avg = avg / 100
            print('密文改变了' + str(avg) + '位')


    def decrypt(code, key):
        des = DES()
        code = des.codefirstchange(code)
        key = des.keyfirstchange(key)
        run_code = ''
        output = ''
        key_code = des.getkey(key)
        code_l = code[0:32]
        code_r = code[32:64]
        for j in range(16):
            code = code_r
            code_r = des.functionE(code_r)

            key_y = key_code[15 - j]
            code_r = des.codeyihuo(code_r, key_y)
            code_r = des.functions(code_r)
            code_r = des.functionp(code_r)
            code_r = des.codeyihuo(code_l, code_r)
            code_l = code
        code_l, code_r = code_r, code_l
        run_code = code_l + code_r
        output += des.nichange(run_code)
        print('明文：' + output)

    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()
        
    def start():
        def keytocode(key, code, time):
            des = DES()
            allavg = 0
            for alltime in range(time):
                avg = 0
                text.insert(END, "\n\n--------------------------------------------第" + str(
                    alltime + 1) + "次统计---------------------------------------------\n\n")
                for i in range(64):
                    change = 0
                    changecode = encrypt(code, des.changekey(key, i))
                    text.insert(END, "明文不变，密钥改变" + str(i + 1) + '位:' + str(changecode) + "       ")
                    for a in range(64):
                        if changecode[a] != code[a]:
                            change += 1
                    text.insert(END, '密文改变了' + str(change) + '位\n')
                    avg += change
                avg = avg / 64
                text2.insert(END, '第' + str(alltime + 1) + '次统计：' + str(avg) + '\n\n')
                allavg += avg
            alla = allavg / time
            text2.insert(END, '总计改变次数：' + str(alla) + '\n\n')

        def from_codetocode(key, code, time):
            des = DES()
            allavg = 0
            for alltime in range(time):
                avg = 0
                text.insert(END, "\n\n--------------------------------------------第" + str(
                    alltime + 1) + "次统计---------------------------------------------\n\n")
                for i in range(64):
                    change = 0
                    changecode = encrypt(des.changekey(key, i), code)
                    text.insert(END, "密钥不变，明文改变" + str(i + 1) + '位:' + str(changecode) + "       ")
                    for a in range(64):
                        if changecode[a] != code[a]:
                            change += 1
                    text.insert(END, '明文改变了' + str(change) + '位\n')
                    avg += change
                avg = avg / 64
                text2.insert(END, '第' + str(alltime + 1) + '次统计：' + str(avg) + '\n\n')
                allavg += avg
            alla = allavg / time
            text2.insert(END, '总计改变次数：' + str(alla) + '\n\n')

        getfunction = cmb.get()
        getzhi = int(mentry.get())
        code = mentry1.get()
        key = mentry2.get()
        text.delete('1.0', 'end')
        text2.delete('1.0', 'end')
        if getfunction == '明文固定，密钥改变':
            keytocode(key, code, getzhi)

        else:
            from_codetocode(key, code, getzhi)


    wuya = tkinter.Tk()

    wuya.title("明文/密钥 固定，密钥/明文 改变")
    wuya.geometry("1200x650+10+20")
    frmb = Frame(wuya)
    frmb.grid(row=0, column=0, pady=10)
    frmbutton = Frame(wuya)
    frmbutton.grid(row=1, column=0, padx=5, pady=10)
    frmbtree = Frame(wuya)
    frmbtree.grid(row=2, column=0, padx=20, pady=10)

    blabel = Label(frmb, text='明文/密钥 固定，密钥/明文 改变', justify=LEFT, font=("微软雅黑", 21), fg='blue')
    blabel.grid(row=0, column=0)

    mlabel = Label(frmbutton, text='指定一个Sbox：')

    mlabel.grid(row=1, column=0)
    cmb = ttk.Combobox(frmbutton)
    cmb.grid(row=1, column=1)
    cmb['value'] = ('明文固定，密钥改变', '密钥固定，明文改变')
    cmb.current(0)

    glabel = Label(frmbutton, text='输入统计次数：')
    glabel.grid(row=2, column=0)

    mentry = Entry(frmbutton, text='请输入1', width=70, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="green")

    mentry.grid(row=2, column=1)

    glabel1 = Label(frmbutton, text='输入明文：')
    glabel1.grid(row=3, column=0)

    mentry1 = Entry(frmbutton, text='请输入2', width=70, cursor='mouse', insertbackground="red",
                    highlightcolor="red", highlightbackground="green")

    mentry1.grid(row=3, column=1)
    glabel2 = Label(frmbutton, text='输入密文：')
    glabel2.grid(row=4, column=0)

    mentry2 = Entry(frmbutton, text='请输入3', width=70, cursor='mouse', insertbackground="red",
                    highlightcolor="red", highlightbackground="green")

    mentry2.grid(row=4, column=1)

    mentry.insert(END, "10")
    mentry1.insert(END, "0011000100110010001100110011010000110101001101100011011100111000")
    mentry2.insert(END, "1000101110110100011110100000110011110000101010010110001001101101")

    thebutton1 = Button(frmbutton, text="开始统计", bg="lightblue", width=25,
                        command=lambda: thread_it(start()))
    thebutton1.grid(row=5, column=1, pady=5)

    gtblabel = Label(frmbtree, text='过程：')
    gtblabel.grid(row=0, column=0)

    text = Text(frmbtree, width=110, height=30)
    text.grid(row=1, column=0)

    gtlabelw = Label(frmbtree, text='平均次数：')
    gtlabelw.grid(row=0, column=1)
    text2 = Text(frmbtree, width=50, height=30)
    text2.grid(row=1, column=1, padx=15)

    wuya.mainloop()