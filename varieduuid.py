from random import randint
class uuidGen:
    def __init__(self):
        pass

    def genFullUUID():
        characterString = "1234567890abcdefghijklmnopqrstuvwxyz"
        return randint(0,len(characterString)+1), characterString, len(characterString)
    
    def genNumUUID(uuidLength):
        numberString = "0123456789"
        for i in range(0, int(uuidLength)):
            uuid += str(numberString[randint(0, len(numberString)-1)])
        return uuid
    
    def customUUID(characterString:str, uuidLength:int):
        uuid=""
        for i in range(0, int(uuidLength)):
            uuid += str(characterString[randint(0, len(characterString)-1)])
        return uuid

number = "AllCatsAreBeautiful1312161"
print(uuidGen.customUUID(number, 32))
