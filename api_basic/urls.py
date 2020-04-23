from django.urls import path
from . import views
from rest_framework.authtoken import views as token
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # class bassed view url

    path('article', views.ArticleApiView.as_view()),
    path('article-details/<int:id>/', views.ArticleDetails.as_view()),

    # function based views
    # path('article', views.article),
    # path('article-details/<int:pk>/', views.article_detail),

    # generic and mixin view
    path('article-generic/', views.GenericApiView.as_view()),
    path('article-generic/<int:id>/', views.GenericApiView.as_view())
]

urlpatterns += [
    # normal token based auth
    path('api-token-auth/', token.obtain_auth_token),

    # jwt token purpose use url
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', views.HelloView.as_view(), name='hello'),

]
