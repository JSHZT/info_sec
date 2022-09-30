import numpy as np
import sympy as sympy

VALID_CHARACTERS = np.array(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                             'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                             '.', ',', ':', '?', ' '])

PADDING = 'X'

class hill(object):
    def Encryption(self, data, key):
        result = []
        for i in data:
            result.append(self.uoc_hill_cipher(i, key))
        return result
    
    def Decrypt(self, data, key):
        result = []
        for i in data:
            result.append(self.uoc_hill_decipher(i, key))
        return result
    
    def get_position(self, char):
        char = char.upper()
        position = np.where(VALID_CHARACTERS == char)[0]
        return position[0] if len(position) > 0 else -1

    def split_array(self, array, size):
        new_array = []
        temporal_array = []
        for value in array:
            temporal_array.append(value)
            if len(temporal_array) >= size:
                new_array.append(temporal_array)
                temporal_array = []
        if len(temporal_array)> 0:
            new_array.append(temporal_array)
        return new_array

    def get_inverse_key(self, key):
        matrix = sympy.Matrix(key)
        inv_matrix = matrix.inv_mod(len(VALID_CHARACTERS))
        return np.array(inv_matrix).astype(np.int64)

    def uoc_hill_genkey(self, size):
        return np.random.randint(len(VALID_CHARACTERS), size=(size, size))

    def uoc_hill_cipher(self, message, key):
        ciphertext = ""
        message_values = []
        for char in message:
            value = self.get_position(char)
            message_values.append(value)
        splitted_array = self.split_array(message_values, len(key))
        for group in splitted_array:
            if len(group) < len(key):
                while len(group) < len(key):
                    group=np.append(group, self.get_position(PADDING))

            new_values = np.dot(key, group) % len(VALID_CHARACTERS)
            for value in new_values:
                ciphertext = ciphertext + VALID_CHARACTERS[value]
        return ciphertext

    def uoc_hill_decipher(self, message, key):
        plaintext = ""
        invers_key = self.get_inverse_key(key)
        message_values = []
        for char in message:
            value = self.get_position(char)
            message_values.append(value)
        splited_array = self.split_array(message_values, len(invers_key))
        for group in splited_array:
            new_values = np.dot(invers_key, group) % len(VALID_CHARACTERS)
            for value in new_values:
                plaintext = plaintext + VALID_CHARACTERS[int(value)]
        while plaintext[len(plaintext)-1] == PADDING:
            plaintext= plaintext[0:len(plaintext)-1]
        return plaintext