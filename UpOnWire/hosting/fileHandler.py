def uploadFileHandler(f):
    with open('testData', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
