from django.shortcuts import render , redirect
from django.urls import reverse
from .models import Post
from .form import Post_Form

# Create your views here.




def post_list(request):
    objects = Post.objects.all()
    return render(request,'posts/post_list.html',{'posts':objects})


def post_details (request,id):
    single = Post.objects.get(id=id)
    return render(request,'posts/post-details.html',{'post':single})


def new_post(request):
    if request.method == 'POST':
        form = Post_Form(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auther = request.user
            myform.save()
            return redirect(reverse('blog:post_list'))
    else:
        form = Post_Form()
    return render(request,'posts/new-post.html',{'form':form})



def edit_post(request,id):
    single = Post.objects.get(id=id)
    if request.method == 'POST':
        form = Post_Form(request.POST,request.FILES,instance=single)
        if form.is_valid():
            form.save()
            return redirect(reverse('blog:post_list'))

    else :
        form = Post_Form(instance=single)
    return render(request,'posts/edit-post.html',{'form':form})


def delete_post(request,id):
    single = Post.objects.get(id=id)
    single.delete()
    return redirect(reverse('blog:post_list'))

