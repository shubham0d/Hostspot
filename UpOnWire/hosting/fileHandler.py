def uploadFileHandler(f, hashId):
    hashString = str(hashId)
    print (hashString)
    filename = ('hosting/uploads/'+hashString+'.zip')
    with open(filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
