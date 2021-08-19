from django.shortcuts import render,redirect,get_object_or_404,reverse
from .forms import ArticleForm
from django.contrib import messages
from .models import Blog, Comment
from django.contrib.auth.decorators import login_required


def articles(request):
    keyword = request.GET.get("keyword")

    if keyword:
        articles = Blog.objects.filter(name__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Blog.objects.all()

    return render(request,"articles.html",{"articles":articles})
      

def index(request):
    return render(request,'index.html')


def about(request):
    data = [
        'Learn java',
        'Learn unity',
        'Learn Spring',
        'Learn Swing',
        'Learn Python',
        'Learn C#',
        'Learn Django',
    ]
    
    return render(request,'about.html',{'items':data})
@login_required(login_url="/user/login/")
def dashboard(request):
    articles = Blog.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,'dashboard.html',context)
@login_required(login_url="/user/login/")
def publish_article(request):
    
    form = ArticleForm(request.POST or None,request.FILES or None)
    
    if form.is_valid():
        article = form.save(commit = False)        
        article.author = request.user
        article.save()

        messages.success(request," Blog was published")
        return redirect("dashboard")

    context = {
        "form":form
        }
    return render(request,"publisharticle.html",context)
@login_required(login_url="/user/login/")
def details(request,id):
    article = get_object_or_404(Blog,id = id)
    comments = article.comments.all()
    context ={
        "article" : article,
        "comments": comments
    }
    
    return render(request,"detail.html",context)
@login_required(login_url="/user/login/")
def updateArticle (request,id):
    article =get_object_or_404(Blog,id = id)
    form = ArticleForm(request.POST or None, request.FILES or None,instance= article)

    if form.is_valid():
        article = form.save(commit = False)        
        article.author = request.user
        article.save()

        messages.success(request," Blog was edited")
        return redirect("index")

    return render(request,"update.html",{"form":form})

@login_required(login_url="/user/login/")
def deleteArticle(request,id):
    article =get_object_or_404(Blog,id = id)

    article.delete()

    messages.success(request, "The blog was removed")
    return redirect("dashboard")

def addComment(request,id):
    
    article = get_object_or_404(Blog, id = id)

    if request.method =="POST":

        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")


        newComment = Comment(comment_author= comment_author, comment_content= comment_content)

        newComment.article =article
        newComment.save()
        
    
    return redirect(reverse("details", kwargs = {"id": id }))
