from shutil import copy


def editSiteTemplate(siteConfFile):
    # with is like your try .. finally block in this case
    with open(siteConfFile, 'r') as file:
    # read a list of lines into data
    configData = file.readlines()
    print data
    print "Your name: " + data[0]
    data[1] = 'Mage\n'
    # and write everything back
    with open('stats.txt', 'w') as file:
        file.writelines( data )

def siteConfig(imageId, containerIp, domainName):
    siteConfFile = "/etc/nginx/sites-available/"+imageId+".conf"
    copy("hosting/config/defaultNginxSiteTemplate.conf", siteConfFile)
    editSiteTemplate(siteConfFile)
