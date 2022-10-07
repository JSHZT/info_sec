from utils import DataOP, Caesar_code, XOR_code, hill_code, Playfair

def loop():
    notvalid = True 
    hill_key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
    xor_key = 'default',
    caesar_key = 5
    while 1:
        isencode = True if (input("请选择加密还是解密：1.加密 2.解密\n")=='1') else False
        isfile = True if (input("请选择需要对文件还是纯字符串进行操作: 1.文件（仅支持txt）  2.纯字符串\n") == '1') else False
        way = None
        while notvalid:
            way = int(input("请选择一种方法: 1.异或   2.凯撒  3.playfair  4.hill\n"))
            notvalid = False if way in set({1, 2, 3, 4}) else True
        if isfile:
            data = DataOP.load_data.load_txt()
        else:
            data = [input("输入字符串:\n")]
        if way == 1:
            xor_key = input("请输入密钥(字符串)\n")
            if isencode:
                result = XOR_code.XOR_code().Encryption(data=data, key = xor_key)
            else:
                result = XOR_code.XOR_code().Decrypt(data=data, key = xor_key)
        elif way == 2:
            caesar_key = int(input("请输入密钥(整数)\n"))
            if isencode:
                result = Caesar_code.Caesar_code().Encryption(data=data, key=caesar_key)
            else:
                result = Caesar_code.Caesar_code().Decrypt(data=data, key=caesar_key)
        elif way == 3:
            if isencode:
                result = Caesar_code.Caesar_code().Encryption(data=data)
            else:
                result = Caesar_code.Caesar_code().Decrypt(data=data)
        elif way == 4:
            hill_key = int(input("请输入密钥(可逆矩阵), 默认为[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]\n"))
            if isencode:
                result = hill_code.hill().Encryption(data=data, key=hill_key)
            else:
                result = Caesar_code.Caesar_code().Decrypt(data=data, key=hill_key)
        else:
            pass
        print(result)



if __name__ == '__main__' :
    loop()
    