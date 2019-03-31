from .utils import randomIdGenerator
from .models import DefaultConf


def generateUrlString():
    for j in range(6,100):
        for i in range(1,100):
            linkString = randomIdGenerator(j)
            serverName = "uponwire.com"
            urlLocation = "/uploads/"+str(linkString)
            isUrlPresent = DefaultConf.objects.filter(url=serverName+urlLocation)
            if (len(isUrlPresent) == 0):
                return urlLocation
