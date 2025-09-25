from random import randint
class uuidGen:
    def genFullUUID():
        uuid=''
        characterString = "1234567890abcdefghijklmnopqrstuvwxyz"
        for i in range(0, 36):
            uuid += str(characterString[randint(0, len(characterString)-1)])
        return str(uuid)
    
    def genNumUUID(uuidLength):
        numberString = "0123456789"
        uuid = ''
        for i in range(0, int(uuidLength)):
            uuid += str(numberString[randint(0, len(numberString)-1)])
        return str(uuid)
    
    def customUUID(characterString:str, uuidLength:int):
        uuid=''
        for i in range(0, int(uuidLength)):
            uuid += str(characterString[randint(0, len(characterString)-1)])
        return str(uuid)

    def myattUUID(uuidLength:int):
        numberString = "123456789"
        uuid = ''
        for i in range(0, int(uuidLength)):
            uuid += str(numberString[randint(0, len(numberString)-1)])
        return str(uuid)
