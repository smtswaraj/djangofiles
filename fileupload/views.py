from django.shortcuts import render
from django.views import View
from .forms import uploadform
from django.views.generic import CreateView,ListView
from .models import upload


# Create your views here.

class FileUpload(CreateView):
    model = upload
    template_name = "fileuploade/index.html"
    fields = '__all__'
    success_url = "/image/imagelist"

class imageView(ListView):
    model = upload
    template_name = "fileuploade/image.html"
    fields = '__all__'
    context_object_name = "image"

# def store_file(file):
#     with open("uplodes/image.jpg","wb+") as dest:
#         for i in file.chunks():
#             dest.write(i)

# class FileUpload(View):


#     def get(self,request):
#         form = uploadform()
#         return render(request,'fileuploade/index.html',{'form':form})


#     def post(self,request):
#         # store_file(request.FILES["Fileupload"])
#         # return render(request,'fileuploade/index.html')
#         form = uploadform(request.POST,request.FILES)
#         # request.POST,
#         if form.is_valid():
#             print(request.FILES['file_Upload'])
#             img = upload(file_Upload = request.FILES['file_Upload'])
#             img.save()
#             return render(request,'fileuploade/index.html',{'form':form})
#         return render(request,'fileuploade/index.html',{'form':form})
