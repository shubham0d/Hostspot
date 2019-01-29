import random
import zipfile

def randomIdGenerator():
    hashId = random.getrandbits(128)
    return hashId

def uncompressFile(imageId):
    zipRef = zipfile.ZipFile('uploads/'+str(imageId)+'.zip', 'r')
    zipRef.extractall('uploads/'+str(imageId))
    zipRef.close()
