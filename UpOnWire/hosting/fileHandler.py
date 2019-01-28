def uploadFileHandler(f, hashId):
    with open('uploads/'+str(hashId)+'.zip', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
