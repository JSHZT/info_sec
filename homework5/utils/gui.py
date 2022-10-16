from utils.changebasesystem import *
from utils.function import *
from utils.cfgui import *
from utils.gbgui import *
import tkinter
import tkinter.messagebox
from tkinter.messagebox import *
from tkinter import *

import threading
import os
import re
import time

def runGUI():
    def start():
        key = all_hex(mentry.get())
        existswriting = all_hex(jentry.get())
        global msg
        msg = []
        msg.clear()
        msg = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        msg[0].append(existswriting)
        answer = get_mk(existswriting, key)
        answer_change = hex(int(answer, base=2)).upper()
        lb.delete(0, END)
        lb.insert(END, "                 加密过程：  初始状态                                       ")
        for i in range(1, 17):
            lb.insert(END, "                 加密过程：  N=" + str(i) + "                                       ")
        text.insert(END, "时间： " + get_current_time() + "\n" + "输入明文： " + str(jentry.get()) + "\n输入密钥： " + str(
            mentry.get()) + "\n密文： " + str(answer))
        text.insert(END, "                                        初始状态\n\n" + "加密过程：\n\n" + "加密信息明文： " + str(
            msg[0][0]) + "\n\n初始置换： " + str(
            msg[0][1]) + '\n\nL0：' + str(msg[0][2]) + '\n\nR0：' + str(msg[0][3]) + '\n\n密钥：' + str(msg[0][4]))
        for num in range(1, 17):

            text.insert(END, "                                          N=" + str(
                num) + "\n\n" + "加密过程：\n\n" + '32位输入：' + str(msg[num][6])
                        + '\n\n选择运算：' + str(msg[num][3]) + '\n\nS盒：：' + str(msg[num][4]) + '\n\np置换：' + str(
                msg[num][5]) + '\n\nL' + str(num) + '：' + str(msg[num][6]) + '\n\nR' + str(num) + '：' + str(msg[num][7])
                        + "\n\n\n密钥扩展：" + '\n\nC' + str(num) + '：' + str(msg[num][0]) + '\n\nD' + str(num) + '：' + str(
                msg[num][1]) + '\n\n子密钥K' + str(num) + '：' + str(msg[num][2])
                        )

    def get_current_time():
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        return current_time

    def openimf(event):
        global msg
        temp = lb.get(lb.curselection())
        top = Tk()
        top.geometry("700x410+200+150")
        xu = re.split('                 ', temp)
        top.title(xu[1])
        xnext = re.search(r'加密过程：  (.*).*', xu[1], re.M | re.I).group(1).replace(" ", "")
        if (xnext == '初始状态'):
            frmtop = Frame(top)
            frmtop.pack(fill=X, padx=10, pady=3)
            toptap = Label(frmtop, text=xu[1], font=("微软雅黑", 20), fg='blue')
            toptap.pack(fill=X, padx=10, pady=6)
            ttext = Text(frmtop, width=50, height=30)
            ttext.pack(fill=X, padx=10, pady=3)
            ttext.insert(END, "                                        初始状态\n\n" + "加密过程：\n\n" + "加密信息明文： " + str(
                msg[0][0]) + "\n\n初始置换： " + str(
                msg[0][1]) + '\n\nL0：' + str(msg[0][2]) + '\n\nR0：' + str(msg[0][3]) + '\n\n密钥：' + str(msg[0][4]))

        else:
            num = int(xnext.replace("N=", ""))

            frmtop = Frame(top)
            frmtop.pack(fill=X, padx=10, pady=3)
            toptap = Label(frmtop, text=xu[1], font=("微软雅黑", 20), fg='blue')
            toptap.pack(fill=X, padx=10, pady=6)
            ttext = Text(frmtop, width=50, height=30)
            ttext.pack(fill=X, padx=10, pady=3)
            ttext.insert(END, "                                          N=" + str(
                num) + "\n\n" + "加密过程：\n\n" + '32位输入：' + str(msg[num][6])
                         + '\n\n选择运算：' + str(msg[num][3]) + '\n\nS盒：' + str(msg[num][4]) + '\n\np置换：' + str(
                msg[num][5]) + '\n\nL' + str(num) + '：' + str(msg[num][6]) + '\n\nR' + str(num) + '：' + str(
                msg[num][7])
                         + "\n\n\n密钥扩展：" + '\n\nC' + str(num) + '：' + str(msg[num][0]) + '\n\nD' + str(
                num) + '：' + str(
                msg[num][1]) + '\n\n子密钥K' + str(num) + '：' + str(msg[num][2])
                         )


    def thread_it(func, *args):
        '''将函数打包进线程'''
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()

    def IP(Mingwen):
        assert len(Mingwen) == 64
        ret = ""
        for i in IPtable:
            ret = ret + Mingwen[i - 1]
        global msg
        msg[0].append(ret)
        msg[0].append(ret[:32])
        msg[0].append(ret[32:])

        return ret

    def shift(a, s):
        try:
            if len(a) > 28:
                raise NameError
        except TypeError:
            pass

        a = a[s:] + a[0:s]
        return a

    def createSubkey(key):
        assert len(key) == 64
        C0 = ""
        D0 = ""
        for i in Clist:
            C0 += key[i - 1]
        for i in Dlist:
            D0 += key[i - 1]
        assert len(C0) == 28
        assert len(D0) == 28

        retkey = []

        for i in range(0, 16):
            C0 = shift(C0, Movetimes[i])
            D0 = shift(D0, Movetimes[i])
            global msg
            msg[i + 1].append(C0)
            msg[i + 1].append(D0)
            temp = C0 + D0
            tempkey = ""
            for i in PC_2:
                tempkey += temp[i - 1]
            assert len(tempkey) == 48
            retkey.append(tempkey)
            tempkey = ""

        return retkey

    def Etuozhan(Rn):
        retRn = ""
        for i in Elist:
            retRn += Rn[i - 1]
        assert len(retRn) == 48
        return retRn

    def S_sub(Ln, Rn, subkey, oldRn, liskey):
        global msg
        tempresult = int(Rn, base=2) ^ int(subkey, base=2)
        tempresult = bin(tempresult)[2:]
        while len(tempresult) < 48:
            tempresult = "0" + tempresult
        index = 0
        retstr = ""
        for list in Slist:
            hang = int(tempresult[index] + tempresult[index + 5], base=2)
            lie = int(tempresult[index + 1:index + 5], base=2)
            a = bin(list[hang * 16 + lie])[2:]
            while len(a) < 4:
                a = "0" + a
            retstr += a
            index += 6
        msg[liskey].append(retstr)
        assert len(retstr) == 32
        tmp = ""
        for i in Phezhihuan:
            tmp += retstr[i - 1]
        msg[liskey].append(tmp)
        a = int(tmp, base=2) ^ int(Ln, base=2)
        a = bin(a)[2:]
        while len(a) < 32:
            a = "0" + a
        assert len(a) == 32
        (Ln, Rn) = (oldRn, a)
        return (Ln, Rn)

    def P_1(L16, R16):
        tmp = L16 + R16
        retstr = ""
        for i in list:
            retstr += tmp[i - 1]
        assert len(retstr) == 64
        return retstr

    def get_mk(mw, key):
        global msg
        Chushizhihuan = IP(mw)
        msg[0].append(key)
        subkeylist = createSubkey(key)
        Ln = Chushizhihuan[0:32]
        Rn = Chushizhihuan[32:]
        for ikey in range(1, 17):
            msg[ikey].append(subkeylist[ikey - 1])

        lissubkey = 1
        for subkey in subkeylist:
            while len(Rn) < 32:
                Rn = "0" + Rn
            while len(Ln) < 32:
                Ln = "0" + Ln
            Rn_tuozhan = Etuozhan(Rn)
            msg[lissubkey].append(Rn_tuozhan)

            (Ln, Rn) = S_sub(Ln, Rn_tuozhan, subkey, Rn, lissubkey)
            msg[lissubkey].append(Ln)
            msg[lissubkey].append(Rn)
            lissubkey += 1
        (Ln, Rn) = (Rn, Ln)
        b = P_1(Ln, Rn)
        return b


    master = Tk()
    master.geometry("900x600+100+100")
    master.title("DES")

    frmb = Frame(master)
    frmb.grid(row=0, column=0, pady=10)
    frmbutton = Frame(master, borderwidth=2, relief="ridge")
    frmbutton.grid(row=1, column=0, padx=5, pady=10)
    frmn = Frame(master)
    frmn.grid(row=3, column=0)
    frmgbt = Frame(master)
    frmgbt.grid(row=2, column=0)

    sblabel = Label(frmn, text='双击题目可查看具体过程', justify=LEFT, font=("微软雅黑", 12), fg='red')
    sblabel.grid(row=0, column=1)
    sblabel = Label(frmn, text='↓↓↓详细过程↓↓↓', justify=LEFT, font=("微软雅黑", 12))
    sblabel.grid(row=0, column=3)
    blabel = Label(frmb, text='      DES算法实现', justify=LEFT, font=("微软雅黑", 21), fg='blue')
    blabel.grid(row=0, column=0)

    jlabel = Label(frmbutton, text='加密信息：')
    jlabel.grid(row=0, column=1, padx=15, pady=5)
    jentry = Entry(frmbutton, text='请输入16进制的8位明文', width=35, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="black")
    jentry.insert(END, "3031323334353637")
    jentry.grid(row=0, column=2, padx=15, pady=5)
    mlabel = Label(frmbutton, text='密钥：')
    mlabel.grid(row=0, column=3, padx=15, pady=5)
    mentry = Entry(frmbutton, text='请输入16进制的8位密钥', width=35, cursor='mouse', insertbackground="red",
                   highlightcolor="red", highlightbackground="green")
    mentry.insert(END, "3132333435363738")

    mentry.grid(row=0, column=4, padx=15, pady=5)
    thebutton1 = Button(frmbutton, text="开始加密", bg="lightblue", width=20,
                        command=lambda: thread_it(start()))
    thebutton1.grid(row=0, column=5, pady=5)
    thebutton2 = Button(frmgbt, text="Sbox差分", bg="lightblue", width=50,
                        command=lambda: thread_it(cfgui()))
    thebutton2.grid(row=0, column=0, pady=5)
    thebutton3 = Button(frmgbt, text="明文/密钥 固定，密钥/明文 改变", bg="lightblue", width=50,
                        command=lambda: thread_it(gbgui()))
    thebutton3.grid(row=0, column=1, padx=10,pady=5)

    sb = Scrollbar(frmn)
    sb.grid(row=1, column=2, sticky='ns')
    lb = Listbox(frmn, width=45, height=20, selectmode=SINGLE, yscrollcommand=sb.set)
    lb.grid(row=1, column=1)
    sb.config(command=lb.yview)
    lb.bind('<Double-Button-1>', openimf)

    text = Text(frmn, width=75, height=30)
    text.grid(row=1, column=3)

    master.mainloop()
