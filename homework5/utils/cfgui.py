import tkinter
import tkinter.messagebox
from tkinter.messagebox import *
from tkinter import *

from tkinter import ttk
import threading
def cfgui():
    S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
          [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
          [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
          [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
          [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
          [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
          [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
          [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
          [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
          [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
          [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
          [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
          [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
          [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
          [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
          [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
          [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
          [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
          [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
          [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
          [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
          [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    S7 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
          [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
          [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
          [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]


    def start():
        x = tree.get_children()
        for item in x:
            tree.delete(item)
        b = ''
        d = ''
        a = []
        c = []
        gg = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        getfunction = cmb.get()
        getzhi = mentry.get()
        for i in range(64):
            b += str(functions(str('{:06b}'.format(i)), getfunction))
            d += str(functions(str(codeyihuo('{:06b}'.format(i), str(getzhi))), getfunction))
            a.append(str(codeyihuo(b[i * 4:i * 4 + 4], d[i * 4:i * 4 + 4])))
            gg[int(str(codeyihuo(b[i * 4:i * 4 + 4], d[i * 4:i * 4 + 4])), 2)].append(
                str(codeyihuo('{:06b}'.format(i), str(getzhi))))
        for pi in range(len(gg)):
            g3 = ''
            g1 = str('{:04b}'.format(pi))
            g2 = str(len(gg[pi]))
            for btg in gg[pi]:
                g3 += str(btg) + str(' ')
            tree.insert("", pi, text=str(pi + 1), values=(g1, g2, str(g3)))


    def functions(key, getf):
        return_list = ''
        row = int(str(key[0]) + str(key[5]), 2)
        raw = int(str(key[1]) + str(key[2]) + str(key[3]) + str(key[4]), 2)
        if getf == 'S1':
            return_list += changtos(S1[row][raw], 4)
        if getf == 'S2':
            return_list += changtos(S2[row][raw], 4)
        if getf == 'S3':
            return_list += changtos(S3[row][raw], 4)
        if getf == 'S4':
            return_list += changtos(S4[row][raw], 4)
        if getf == 'S5':
            return_list += changtos(S5[row][raw], 4)
        if getf == 'S6':
            return_list += changtos(S6[row][raw], 4)
        if getf == 'S7':
            return_list += changtos(S7[row][raw], 4)
        # if getf == 'S8':
        #     return_list += changtos(S8[row][raw], 4)
        return return_list


    def changtos(o, lens):
        return_code = ''
        for i in range(lens):
            return_code = str(o >> i & 1) + return_code
        return return_code


    def codeyihuo(code, key):
        code_len = len(key)
        return_list = ''

        for i in range(code_len):
            if code[i] == key[i]:
                return_list += '0'
            else:
                return_list += '1'
        #    print(return_list)
        return return_list


    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()


    wuya = tkinter.Tk()
    wuya.title("Sbox差分")
    wuya.geometry("950x450+10+20")
    frmb = Frame(wuya)
    frmb.grid(row=0, column=0, pady=10)
    frmbutton = Frame(wuya)
    frmbutton.grid(row=1, column=0, padx=5, pady=10)
    frmbtree = Frame(wuya)
    frmbtree.grid(row=2, column=0, padx=20, pady=10)

    blabel = Label(frmb, text='Sbox差分情况', justify=LEFT, font=("微软雅黑", 21), fg='blue')
    blabel.grid(row=0, column=0)

    mlabel = Label(frmbutton, text='指定一个Sbox：')

    mlabel.grid(row=1, column=0)
    cmb = ttk.Combobox(frmbutton)
    cmb.grid(row=1, column=1)
    cmb['value'] = ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8')
    cmb.current(0)

    glabel = Label(frmbutton, text='指定输入差分（6位）：')
    glabel.grid(row=2, column=0)

    mentry = Entry(frmbutton, text='请输入', width=20, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="green")

    mentry.insert(END, "000001")
    mentry.grid(row=2, column=1)

    thebutton1 = Button(frmbutton, text="开始分析", bg="lightblue", width=25,
                        command=lambda: thread_it(start()))
    thebutton1.grid(row=3, column=1, pady=5)

    tree = ttk.Treeview(frmbtree)  # 表格
    tree["columns"] = ("输出差分△S", "输入数量N", "可能的输入IN")
    tree.column("输出差分△S", width=100, anchor="center")  # 表示列,不显示
    tree.column("输入数量N", width=100, anchor="center")
    tree.column("可能的输入IN", width=500, anchor="center")

    tree.heading("输出差分△S", text="输出差分△S")  # 显示表头
    tree.heading("输入数量N", text="输入数量N")
    tree.heading("可能的输入IN", text="可能的输入IN")


    tree.grid(row=4, column=0, pady=5)
    wuya.mainloop()