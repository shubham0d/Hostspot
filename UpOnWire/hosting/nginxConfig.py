from shutil import copy
from subprocess import getstatusoutput
#from .utils import serviceReloader
import threading
# use better config file editing method
def editSiteTemplate(siteConfFile, domainName, containerIp, imageId, userUrl, hostingType):
    # with is like your try .. finally block in this case
    with open(siteConfFile, 'r') as file:
        configData = file.readlines()
    file.close()
    if (userUrl == True):
        configData[2] = '    server_name '+domainName+';\n'
        if (hostingType == 'W'):
            configData[5] = '            proxy_pass http://'+containerIp+':80/;\n'
        else:
            configData[5] = '            proxy_pass http://'+containerIp+':80/'+str(imageId)+';\n'
    else:
        configData[2] = '    server_name uponwire.com;\n'
        configData[3] = '    location '+domainName+' {\n'
        if (hostingType == 'W'):
            configData[5] = '            proxy_pass http://'+containerIp+':80/;\n'
        else:
            configData[5] = '            proxy_pass http://'+containerIp+':80/'+str(imageId)+';\n
    with open(siteConfFile, 'w') as file:
        file.writelines( configData )
    file.close()
    stat = getstatusoutput("ln -s "+siteConfFile+" /etc/nginx/sites-enabled/"+str(imageId)+".conf")


def editHosts(domainName):
    with open("/etc/hosts", 'a') as file:
        file.write("127.0.0.1 "+ domainName+"\n")
    file.close()

def siteConfig(imageId, containerIp, domainName, userUrl, hostingType):
    siteConfFile = "/etc/nginx/sites-available/"+str(imageId)+".conf"
    copy("config/defaultNginxSiteTemplate.conf", siteConfFile)
    editSiteTemplate(siteConfFile, domainName, containerIp, imageId, userUrl, hostingType)
    if (userUrl == True):
        editHosts(domainName)
    #threading.Thread(target=serviceReloader, args = ("nginx"))


#siteConfig("bibibib",'192.168.122.1', "pinki.com", True)
