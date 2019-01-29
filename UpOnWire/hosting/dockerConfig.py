
import zipfile


def createDockerInstance(imageId, hostingType):
    print (hostingType)
    if (hostingType == 'W'):
        uncompressFile(imageId)






def createDockerFile(imageId):
    filename = "uploads/Dockerfile"
    dockerFile = open(filename, 'w+')

def uncompressFile(imageId):
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    zip_ref.extractall(directory_to_extract_to)
    zip_ref.close()
