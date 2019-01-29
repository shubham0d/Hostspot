from .utils import uncompressFile
import commands

def createDockerInstance(imageId, hostingType):
    print (hostingType)
    if (hostingType == 'W'):
        uncompressFile(imageId)
        createDockerFile(imageId)



def createDockerFile(imageId):
    filename = "uploads/"+str(imageId)+"/Dockerfile"
    dockerFile = open(filename, 'w+')
    dockerFile.write("FROM nginx\nCOPY uploads/"+str(imageId)+"/mysite /usr/share/nginx/html")
    dockerFile.close()
    commands.getstatusoutput("docker build -t "+str(imageId)+" .")
