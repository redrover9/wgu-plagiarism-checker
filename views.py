from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import UploadEssay
from forms import handle_uploaded_essay


def upload_file(request):
    if request.method == 'POST':
        form = UploadEssay(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_essay(request.FILES['file'])
            return HttpResponseRedirect('success.html')
        else:
            form = UploadEssay()
        return render(request, 'upload.html', {'form': form})
