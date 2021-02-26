from django import forms


def handle_uploaded_essay(f):
    with open('essay.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


class UploadEssay(forms.Form):
    title = forms.CharField(max_length=150)
    file = forms.FileField()
