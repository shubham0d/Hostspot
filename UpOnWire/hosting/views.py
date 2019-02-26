from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadFileForm
from .forms import HostingForm
from django.utils import timezone
from .fileHandler import uploadFileHandler
from .utils import randomIdGenerator
from django.core.files.storage import FileSystemStorage
from .hostingSetup import hosting
from .models import DefaultConf
from .urlHandler import generateUrlString
# Create your views here.
def index(request):
    if request.method == "POST":
        form = HostingForm(request.POST, request.FILES)
        uploadForm = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            hashId = randomIdGenerator(128)
            hostingType = form.cleaned_data['hostingType']
            expireDays = form.cleaned_data['expireDays']
            if (form.cleaned_data['domain'] is ""):
                linkUrl = generateUrlString()
                url = linkUrl
            else:
                url = form.cleaned_data['domain']
            #uploadFileHandler(request.FILES['file'], str(hashId))
            #hosting(hashId, hostingType, url, expireDays)
            hostingInstance = DefaultConf(imageId = hashId, creationDate = timezone.now(), url = url,expireDate = expireDays,hostingType = hostingType,active = True)
            hostingInstance.save()
            submitSuccessfully = True
            context = {
            'form': form,
            'submitSuccessfully': submitSuccessfully,
            'uploadForm':uploadForm
            }
            print(context)
            return render(request, 'hosting/index.html', {'context': context})
    else:
        #form = SetupForm()
        form = HostingForm()
        uploadForm = UploadFileForm()
        submitSuccessfully = False
        context = {
        'form': form,
        'submitSuccessfully': submitSuccessfully,
        'uploadForm':uploadForm
        }
        return render(request, 'hosting/index.html', {'context': context})
