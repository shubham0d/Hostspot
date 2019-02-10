from .dockerConfig import createDockerInstance
from .nginxConfig import siteConfig


def hosting(imageId, hostingType, domainName, expireDate):
    #containerIp = createDockerInstance(imageId, hostingType)
    containerIp='172.17.0.2'
    siteConfig(imageId, containerIp, domainName)
