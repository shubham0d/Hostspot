from .utils import uncompressFile
from .utils import mvFileToDirectory
from subprocess import getstatusoutput
from .utils import removeFile

def createDockerInstance(imageId, hostingType):
    if (hostingType == 'W'):
        uncompressFile(imageId)
        createDockerFile(imageId, True)
        if (startContainer(imageId, True) == 0):
            print ("failed to create image")
    else:
        mvFileToDirectory(imageId)
        createDockerFile(imageId, False)
        if (startContainer(imageId, False) == 0):
            print ("failed to create image")
    containerIp = getContainerIp(imageId)
    return containerIp


def createDockerFile(imageId, isWebsite):
    if (isWebsite == True):
        filename = "hosting/uploads/"+str(imageId)+"/Dockerfile"
        dockerFile = open(filename, 'w+')
        dockerFile.write("FROM nginx\nCOPY hosting/uploads/"+str(imageId)+"/mysite /usr/share/nginx/html")
    else:
        filename = "hosting/uploads/"+str(imageId)+"_dir/Dockerfile"
        dockerFile = open(filename, 'w+')
        dockerFile.write("FROM nginx\nCOPY hosting/uploads/"+str(imageId)+"_dir /usr/share/nginx/html")
    dockerFile.close()



def startContainer(imageId, isWebsite):
    if (isWebsite == True):
        if (getstatusoutput("docker build -t "+str(imageId)+" -f hosting/uploads/"+str(imageId)+"/Dockerfile .")[0] == 0):
            getstatusoutput("docker run --name "+str(imageId)+"_running -d "+str(imageId))
        else:
            return 0
    else:
        if (getstatusoutput("docker build -t "+str(imageId)+" -f hosting/uploads/"+str(imageId)+"_dir/Dockerfile .")[0] == 0):
            getstatusoutput("docker run --name "+str(imageId)+"_running -d "+str(imageId))
        else:
            return 0

def getContainerIp(imageId):
    ip = getstatusoutput("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' " + str(imageId) +"_running")[1]
    return str(ip)
