from .dockerConfig import createDockerInstance
from .nginxConfig import siteConfig
from .utils import removeDirectory
from .utils import removeFile

def hosting(imageId, hostingType, domainName, expireDate):
    containerIp = createDockerInstance(imageId, hostingType)
    if (containerIp != ''):
        #remove the zip and folder
        if (hostingType == 'W'):
            removeDirectory("hosting/uploads/"+str(imageId))
            removeFile("hosting/uploads/"+str(imageId)+".zip")
        else:
            removeDirectory("hosting/uploads/"+str(imageId)+"_dir")
            removeFile("hosting/uploads/"+str(imageId))
    siteConfig(imageId, containerIp, domainName, hostingType)
