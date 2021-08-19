from django.urls import path
from .views import index,about,dashboard,publish_article,details,updateArticle,deleteArticle,articles,addComment
urlpatterns = [
    path('',index, name ='index'),
    path('about/',about, name = 'about'),
    path('dashboard/',dashboard, name ='dashboard'),
    path('publisharticle/',publish_article, name = 'publisharticle'),
    path('article/<int:id>/',details, name = 'details'),
    path('update/<int:id>/',updateArticle, name = 'update'),
    path('delete/<int:id>/',deleteArticle, name = 'delete'),
    path('articles/',articles, name = 'articles'),
    path('comment/<int:id>/',addComment, name = 'comment'),

]
 