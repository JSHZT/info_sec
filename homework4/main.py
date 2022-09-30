from utils import DataOP, Caesar_code, XOR_code, hill_code, Playfair

if __name__ == '__main__' :
    data = DataOP.load_data.load_txt()
    key = [[5, 15, 18, 15, 10], [22, 10, 35, 10, 37], [28, 33, 31, 7, 30], [14, 35, 33, 38, 28], [30, 0, 37, 26, 6]]
    data = hill_code.hill().Encryption(data, key)
    print(data)
    data = hill_code.hill().Decrypt(data, key)
    print(data)