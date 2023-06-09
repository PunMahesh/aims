from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required (login_url="login")
def add_article(request):
    if request.method == "POST":
        user = request.user
        ArticleName = request.POST.get("ArticleName")
        Article_Photo = request.FILES.get("Article_Photo")
        Description = request.POST.get("Description")

        details = Article(user=user,ArticleName=ArticleName, Article_Photo=Article_Photo, Description=Description)
        details.save()
        return redirect("Article_added")
    return render(request, 'article.html')

def get_article(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    print (context)
    return render(request, 'blog.html', context)