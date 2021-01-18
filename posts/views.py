from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment,Category
from .forms import PostForm,CommentForm,KeyForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages


def index(request) :
    return render(request,'posts/index.html')

def schedule(request) :
    return render(request, 'posts/schedule.html')

def introduction(request) :
    return render(request,'posts/introduction.html')


def list(request) :
    posts=Post.objects.order_by('-created_date')
    context={'posts':posts}
    return render(request,'posts/list.html',context)


def detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    context={'post':post}
    return render(request,'posts/detail.html',context)

@login_required
def create(request):
   if request.method=="POST" :
       form=PostForm(request.POST,request.FILES)
       if form.is_valid():
           post = form.save(commit=False)
           post.user=request.user
           post.save()
           return redirect('posts:list')

   else:
       form=PostForm()
       context = {'form':form}

   return render(request,'posts/create.html',context)

@login_required
def delete(request,pk) :
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated :
        if post.user == request.user :
           post= get_object_or_404(Post,pk=pk)
           post.delete()
           return redirect('posts:list')
    else :
        messages.add_message(request, messages.WARNING, '로그인이 필요합니다.')
        messages.warning(request, '로그인이 필요합니다.')
        return redirect('posts:list')


@login_required
def edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if post.user == request.user :
      post=get_object_or_404(Post,pk=pk)
      if request.method=="POST" :
          form=PostForm(request.POST,request.FILES,instance=post)
          if form.is_valid() :
             post = form.save(commit=False)
             post.user=request.user
             post.save()
             return redirect('posts:detail',pk=post.pk)

      else:
          form = PostForm(instance=post)
          context={'form':form}
          return render(request,'posts/create.html',context)

@login_required
def comments_create(request,pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST" :
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()

            return redirect('posts:detail',pk=post.pk)
    else:
        form = CommentForm()
        context = {'form' : form,
                   'post': post
                   }
    return render(request,'posts/comment.html',context)


@login_required
def comment_delete(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method=="POST":
        if comment.user == request.user:
            comment.delete()
    return redirect('posts:detail',pk=comment.post.pk)



def category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    context={'category':category}
    return render(request,'posts/category.html',context)

def category_list(request) :
    categorys=Category.objects.all()
    context={'categorys': categorys,
             }
    return render(request,'posts/category_list.html',context)

def key(request):

        if request.method == 'POST':
            form = KeyForm(request.POST, request.FILES)
            if form.is_valid():
                key = form.save(commit=False)
                key.save()
                number = request.POST.get('key_number')
                if number == 'tmj-advance-2102':
                    return redirect('posts:index')

        else:
            form = KeyForm()
            context = {'form': form}
            return render(request,'posts/key.html',context)
