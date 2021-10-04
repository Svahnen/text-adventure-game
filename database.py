import json

def readDatabase():
    readStream = open("database.JSON", "r")
    jsonList = readStream.read()
    readStream.close()
    dataList = json.loads(jsonList) # Convert the json array to a python list
    return dataList # Will return a List


def writeToDatabase(dataList): # Will overwrite everythin in database.JSON
    writeStream = open("database.JSON", "w")
    json_string = json.dumps(dataList)
    writeStream.write(json_string)
    writeStream.close()
