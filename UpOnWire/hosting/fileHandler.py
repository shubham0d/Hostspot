def uploadFileHandler(f, hashId, hostingType):
    hashString = str(hashId)
    print (hashString)
    if (hostingType == 'W'):
        filename = ('hosting/uploads/'+hashString+'.zip')
    elif (hostingType == 'V' or hostingType == 'I' or hostingType == 'O'):
        filename = ('hosting/uploads/'+hashString)
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
