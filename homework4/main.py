from utils import DataOP, modules

if __name__ == '__main__' :
    data = DataOP.load_data.load_txt()
    key = 3
    data = modules.Caesar_code().Encryption(data, key)
    print(data)
    data = modules.Caesar_code().Decrypt(data, key)
    print(data)