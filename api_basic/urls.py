from django.urls import path
from . import views

urlpatterns = [

    path('article', views.ArticleApiView.as_view()),
    path('article-details/<int:id>/', views.ArticleDetails.as_view()),

    # function based views
    # path('article', views.article),
    # path('article-details/<int:pk>/', views.article_detail),
    # generic and mixin view
    # path('article-generic/', views.GenericApiView.as_view()),
    path('article-generic/<int:id>/', views.GenericApiView.as_view())
]
