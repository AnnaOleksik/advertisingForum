
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path("register",views.register,name="register"),
    path("login", views.log, name="log"),
    path("logout",views.logoutuser,name="logout"),
    path("create",views.create,name="create"),
    path("<int:adId>",views.detail,name="detail"),
    path("my",views.my,name="my"),
    path("my/<int:adId>",views.edit,name="edit"),
    path("delete/<int:adId>",views.deleteAd,name="delete"),
    path("search",views.search,name="search"),
    path("industry/<str:industryKey>",views.display_industry,name="display_industry"),
    path("like/<int:adId>",views.like,name="like"),
    
]
