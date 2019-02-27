from .dockerConfig import createDockerInstance
from .nginxConfig import siteConfig
from .utils import removeDirectory
from .utils import removeFile

def hosting(imageId, hostingType, domainName, expireDate, userUrl):
    #containerIp = createDockerInstance(imageId, hostingType)
    #if (containerIp!= ''):
        #remove the zip and folder
        #removeDirectory("hosting/uploads/"+str(imageId))
        #removeFile("hosting/uploads/"+str(imageId)+".zip")
    #siteConfig(imageId, containerIp, domainName, userUrl, hostingType)
    print ("Buuuluu")
