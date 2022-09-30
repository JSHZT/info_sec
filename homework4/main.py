from utils import DataOP, modules

if __name__ == '__main__' :
    data = DataOP.load_data.load_txt()
    # key = 3
    data = modules.Playfair_code().Encryption(data)
    print(data)
    data = modules.Playfair_code().Decrypt(data)
    print(data)