from django.urls import path
from color_app import views
from color_app.views import NewColorView, ColorListView, ColorDetailView


app_name = "color_app"
urlpatterns = [
    path('', views.home_view, name="index"),
    path('random/', views.random_color_view, name="random_color"),
    path('colors/', views.ColorListView.as_view(), name="color_list"),
    path('colors/new', views.NewColorView.as_view(), name="new_color"),
    path('colors/<int:pk>', ColorDetailView.as_view(), name='color_detail'),
]

