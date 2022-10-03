from django.urls import path

from home import views
urlpatterns = [
    path('', views.index, name="HomePage"),
    path('dashboard/', views.dashboard, name="DashBoard"),
    path('add/', views.addData, name="AddData"),
    path('filter/<str:fstr>', views.datafilter ,name="FilterData" ),
]