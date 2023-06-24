from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index')
    # path("", views.home, name="home"),
    # path("about/", views.about, name="about"),
    # path("book/", views.about, name="book"),
    # path("menu/", views.menu, name="menu"),
    # path('menu_item/<int:pk>/', views.menu_item, name='menu_item'),
]
