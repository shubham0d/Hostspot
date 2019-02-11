import random
import zipfile
import shutil
import os
from subprocess import getstatusoutput
def randomIdGenerator():
    hashId = random.getrandbits(128)
    return hashId

def uncompressFile(imageId):
    zipRef = zipfile.ZipFile('hosting/uploads/'+str(imageId)+'.zip', 'r')
    zipRef.extractall('hosting/uploads/'+str(imageId))
    zipRef.close()

def serviceReloader(serviceName):
    if (getstatusoutput("service "+serviceName+" restart")[0] == 0):
        return True
    else:
        return False

def removeDirectory(folderName):
    shutil.rmtree(folderName)

def removeFile(fileName):
    os.remove(fileName)
