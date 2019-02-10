from shutil import copy

# use better config file editing method
def editSiteTemplate(siteConfFile, domainName, containerIp):
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

def siteConfig(imageId, containerIp, domainName):
    siteConfFile = "/etc/nginx/sites-available/"+imageId+".conf"
    copy("hosting/config/defaultNginxSiteTemplate.conf", siteConfFile)
    editSiteTemplate(siteConfFile, domainName, containerIp)


#siteConfig("assaass",'192.168.122.1', "test")
