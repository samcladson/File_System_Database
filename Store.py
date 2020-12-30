import json
from datetime import datetime
from sys import getsizeof

class Data:
    def __init__(self):
        self.__key=None
        self.__value=None
    
    def setKey(self,key):
        if len(key)>=32:
            return False
        else:
            self.__key=key
            return True

    def getKey(self):
        return self.__key

    def setValue(self,value):
        if type(value)==dict:
            value.update({"date":datetime.now().strftime('%D'),"time":datetime.now().strftime("%H:%M:%S")})
            self.__value=value
            return True
        else:
            return False

    def getValue(self):
        return self.__value

class Store:

    def create(self,key,value):
        newData = Data()
        if newData.setKey(key)==True:
            if newData.setValue(value)==True:
                try:
                    readFile=None
                    with open('./db.json','r') as fr:
                        if getsizeof(fr)>=1000000000:
                            return print("\n[ERROR]....Store size exceeded 1GB.\n")
                        readFile = json.load(fr)
                        
                except:
                    return print('\n[Error opening file]....\n')
                if readFile:
                    if newData.getKey() in readFile.keys():
                        return print('\n!Oops name already exist\n')
                try: 
                    with open('./db.json','w') as fw:
                        if getsizeof(newData.getValue())>16384:
                            return print('\n[ERROR]....Size of value must be below 16KB.\n')
                        readFile[newData.getKey()]=newData.getValue()
                        json.dump(readFile,fw,indent=2)
                        return print("\n[DATA CREATED]...Data Created Successfuly.\n")
                except:
                    return print('\n[Error opening file]....')
            else:
                return print("\n[ERROR]....Value must be of type json.\n")
        else:
            return print("\n[ERROR]....Key must be of length less than 32!\n")
        
    def read(self,key=None):
        try:
            with open('./db.json','r') as fr:
                data = json.load(fr)
                if key:
                    data = data[key]
                return print('\n[READING DATA]....\n\n',json.dumps(data,indent=2))
        except:
            return print('\n[Error opening file]....\n')


    def delete(self,key):
        try:
            readFile=None
            with open('./db.json','r') as fr:
                readFile = json.load(fr)
        except:
            return print('\n[Error opening file]....\n')
        if readFile:
            if key in readFile.keys():
                try:
                    with open('./db.json','w') as fw:
                        del readFile[key]
                        json.dump(readFile,fw,indent=2,sort_keys=True)
                        return print('\n[DELETED]....Deleted Successfuly\n')
                except:
                    return print('\n[Error opening file]....\n')
            else:
                return print('\n[NOT FOUND]....key not found!\n')
        else:
            return print('\n[NO DATA]....store is empty!\n')