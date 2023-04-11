class Affine:

    def __init__(self, string, key1, key2):
        assert ((1 <= key1 <= 94) and key1 != 5 and key1 != 19)
        assert (0 <= key1 <= 94)
        self.key1 = key1
        self.key2 = key2
        self.string = string

    def encrypt(self, string , key1 , key2):
        newString = ''
        for char in string:
            x = ord(char) - 32
            y = (key1 * x + key2) % 95
            newString += chr(y + 32)
        return newString

    def decrypt(self, string, key1 , key2):
        newString = ''
        for char in string:
            x = ord(char) - 32
            print ("x: ",x)
            y = (x-key2)//key1
            print("y: ",y)
            newString += chr(y + 32)
        return newString

class Transposition:
    def __init__(self, string,key1,key2):
        self.key1 = key1
        self.key2 = key2
        self.string = string
    
    def encrypt(string, row, column):
        newString =''
        for index in range(row):


def main(string, crypto, do = 'encrypt', key1 = 3, key2 = 3 ):

    if crypto.lower() == 'affine' or crypto.lower() == 'a':
        message = Affine(string, key1, key2)
        if do.lower() == 'decrypt' or do.lower() == 'd':
            decrypted = message.decrypt(string, key1, key2)
            print(decrypted)
            return
        encrypted = message.encrypt(string, key1, key2)
        print(encrypted)


main('(+.', 'affine','e')


