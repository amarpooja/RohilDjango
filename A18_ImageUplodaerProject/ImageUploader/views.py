from django.shortcuts import render, HttpResponseRedirect
from .models import ImageTable
from .froms import ImageForm

def ImageUpload(request):
    if request.method=='POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ImageForm()
    images = ImageTable.objects.all()
    return render(request,'ImageFile.html',{'form':form,'images':images})