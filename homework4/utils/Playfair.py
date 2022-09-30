import re


class Playfair_code(object):
    def __init__(self, omissionRule=0, psw='hello', doublePadding='X', endPadding='X'):
        self.doublePadding = doublePadding
        self.endPadding = endPadding
        self.omissionRule = omissionRule
        # omissionRules = ['Merge J into I','Omit', 'Merge I into J'] 三种构成25个密钥轮的规则
        self.grid = self.generateGrid(psw)

    def convertLetter(self, letter):
        if self.omissionRule == 0:
            if letter == 'J':
                letter = 'I'
            return letter
        elif self.omissionRule == 1:
            if letter == 'Q':
                letter = None
            return letter
        elif self.omissionRule == 2:
            if letter == 'I':
                letter = 'J'
            return letter

    def getAlphabet(self):
        fullAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        alphabet = ''
        for letter in fullAlphabet:
            letter = self.convertLetter(letter)
            if letter is not None and letter not in alphabet:
                alphabet += letter
        return alphabet

    def generateGrid(self, password):
        grid = ''
        alphabet = self.getAlphabet()
        for letter in password:
            if letter not in grid and letter in alphabet:
                grid += letter
        for letter in alphabet:
            if letter not in grid:
                grid += letter
        return grid

    def generateDigraphs(self, input):
        input = self.toAlphabet(input).upper()
        inputFixed = ''
        for i in range(len(input)):
            letter = self.convertLetter(input[i])
            if letter is not None:
                inputFixed += letter
        digraphs = []
        counter = 0
        while counter < len(inputFixed):
            digraph = ''
            if counter + 1 == len(inputFixed):
                digraph = inputFixed[counter] + self.endPadding
                digraphs.append(digraph)
                break
            elif inputFixed[counter] != inputFixed[counter + 1]:
                digraph = inputFixed[counter] + inputFixed[counter + 1]
                digraphs.append(digraph)
                counter += 2
            else:
                digraph = inputFixed[counter] + self.doublePadding
                digraphs.append(digraph)
                counter += 1
        return digraphs

    def encryptDigraph(self, input):
        firstLetter = input[0]
        secondLetter = input[1]
        firstLetterPosition = self.grid.find(firstLetter)
        secondLetterPosition = self.grid.find(secondLetter)
        firstLetterCoordinates = (firstLetterPosition %5, int(firstLetterPosition / 5))
        secondLetterCoordinates = (secondLetterPosition %5, int(secondLetterPosition / 5))
        #same column
        if firstLetterCoordinates[0] == secondLetterCoordinates[0]:
            firstEncrypted = self.grid[(
                ((firstLetterCoordinates[1] + 1) % 5) * 5) + firstLetterCoordinates[0]]
            secondEncrypted = self.grid[(
                ((secondLetterCoordinates[1] + 1) % 5) * 5) + secondLetterCoordinates[0]]
        #same row
        elif firstLetterCoordinates[1] == secondLetterCoordinates[1]:
            firstEncrypted = self.grid[(
                firstLetterCoordinates[1] * 5) + ((firstLetterCoordinates[0] + 1) % 5)]
            secondEncrypted = self.grid[(
                secondLetterCoordinates[1] * 5) + ((secondLetterCoordinates[0] + 1) % 5)]
        else:  #form a rectangle
            firstEncrypted = self.grid[(
                firstLetterCoordinates[1] * 5) + secondLetterCoordinates[0]]
            secondEncrypted = self.grid[(
                secondLetterCoordinates[1] * 5) + firstLetterCoordinates[0]]
        return firstEncrypted+secondEncrypted

    def decryptDigraph(self, input):
        firstEncrypted = input[0]
        secondEncrypted = input[1]
        firstEncryptedPosition = self.grid.find(firstEncrypted)
        secondEncryptedPosition = self.grid.find(secondEncrypted)
        firstEncryptedCoordinates = (
            firstEncryptedPosition % 5, int(firstEncryptedPosition / 5))
        secondEncryptedCoordinates = (
            secondEncryptedPosition % 5, int(secondEncryptedPosition / 5))
        #same column
        if firstEncryptedCoordinates[0] == secondEncryptedCoordinates[0]:
            firstLetter = self.grid[(
                ((firstEncryptedCoordinates[1] - 1) % 5) * 5) + firstEncryptedCoordinates[0]]
            secondLetter = self.grid[(
                ((secondEncryptedCoordinates[1] - 1) % 5) * 5) + secondEncryptedCoordinates[0]]
        #same row
        elif firstEncryptedCoordinates[1] == secondEncryptedCoordinates[1]:
            firstLetter = self.grid[(
                firstEncryptedCoordinates[1] * 5) + ((firstEncryptedCoordinates[0] - 1) % 5)]
            secondLetter = self.grid[(
                secondEncryptedCoordinates[1] * 5) + ((secondEncryptedCoordinates[0] - 1) % 5)]
        else:  #form a rectangle
            firstLetter = self.grid[(
                firstEncryptedCoordinates[1] * 5) + secondEncryptedCoordinates[0]]
            secondLetter = self.grid[(
                secondEncryptedCoordinates[1] * 5) + firstEncryptedCoordinates[0]]
        return firstLetter+secondLetter
    def Encryption(self, data):
        result = []
        for i in data:
            result.append(self.Encryption_line(i))
        return result
    
    def Decrypt(self, data):
        result = []
        for i in data:
            result.append(self.Decrypt_line(i))
        return result
    
    def Encryption_line(self, input):
        digraphs = self.generateDigraphs(input)
        encryptedDigraphs = []
        for digraph in digraphs:
            encryptedDigraphs.append(self.encryptDigraph(digraph))
        return ''.join(encryptedDigraphs)

    def Decrypt_line(self, input):
        digraphs = self.generateDigraphs(input)
        decryptedDigraphs = []
        for digraph in digraphs:
            decryptedDigraphs.append(self.decryptDigraph(digraph))
        return ''.join(decryptedDigraphs)

    def setPassword(self, password):
        password = self.toAlphabet(password).upper()
        self.grid = self.generateGrid(password)

    def toAlphabet(self, input):
        return re.sub('[^A-Za-z]', '', input)

    def isAlphabet(self, input):
        if re.search('[^A-Za-z]', input):
            return False
        return True

    def isUpper(self, input):
        if re.search('[^A-Z]', input):
            return False
        return True
