import random
import zipfile
import shutil
import os
import string
import subprocess
from subprocess import getstatusoutput
def randomIdGenerator(length):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_lowercase + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(length))

def uncompressFile(imageId):
    zipRef = zipfile.ZipFile('hosting/uploads/'+str(imageId)+'.zip', 'r')
    zipRef.extractall('hosting/uploads/'+str(imageId))
    zipRef.close()

def mvFileToDirectory(imageId):
    try:
        os.makedirs('hosting/uploads/'+str(imageId)+'_dir')
        getstatusoutput('mv hosting/uploads/'+str(imageId)+' hosting/uploads/'+str(imageId)+'_dir/')
        #shutil.move('hosting/uploads/'+str(imageId), 'hosting/uploads/'+str(imageId)+'/'+str(imageId))
    except OSError as e:
        print (e.message)
        print ("unable to create directory")


def serviceReloader(serviceName):
    getstatusoutput("service "+serviceName+" restart")

def removeDirectory(folderName):
    shutil.rmtree(folderName)

def removeFile(fileName):
    os.remove(fileName)
