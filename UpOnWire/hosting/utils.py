import random
import zipfile
import shutil
import os
import string
from subprocess import getstatusoutput
def randomIdGenerator():
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(128))

def uncompressFile(imageId):
    zipRef = zipfile.ZipFile('hosting/uploads/'+str(imageId)+'.zip', 'r')
    zipRef.extractall('hosting/uploads/'+str(imageId))
    zipRef.close()

def serviceReloader(serviceName):
    getstatusoutput("service "+serviceName+" restart")

def removeDirectory(folderName):
    shutil.rmtree(folderName)

def removeFile(fileName):
    os.remove(fileName)
