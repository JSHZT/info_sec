from utils import DataOP, modules

if __name__ == '__main__' :
    data = DataOP.load_data.load_txt()
    key = 'jshzt'
    data = modules.XOR_code().Encryption(data, key)
    print(data)
    data = modules.XOR_code().Decrypt(data, key)
    print(data)