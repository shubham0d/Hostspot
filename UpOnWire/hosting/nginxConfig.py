from shutil import copy
from subprocess import getstatusoutput

# use better config file editing method
def editSiteTemplate(siteConfFile, domainName, containerIp, imageId):
    # with is like your try .. finally block in this case
    with open(siteConfFile, 'r') as file:
        configData = file.readlines()
    file.close()
    configData[2] = '    server_name '+domainName+';'
    configData[6] = '            proxy_pass http://'+containerIp+':80/;\n'
    # and write everything back
    with open(siteConfFile, 'w') as file:
        file.writelines( configData )
    file.close()
    print ("works tll here")
    stat = getstatusoutput("ln -s "+siteConfFile+" /etc/nginx/sites-enabled/"+str(imageId)+".conf")
    #symlink(siteConfFile, " /etc/nginx/sites-enabled/"+str(imageId)+".conf")
    print ("this is strtus")


def editHosts(domainName):
    

def siteConfig(imageId, containerIp, domainName):
    siteConfFile = "/etc/nginx/sites-available/"+str(imageId)+".conf"
    copy("hosting/config/defaultNginxSiteTemplate.conf", siteConfFile)
    editSiteTemplate(siteConfFile, domainName, containerIp, imageId)


#siteConfig("assaass",'192.168.122.1', "test")
