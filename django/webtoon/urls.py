from django.urls import path
from . import views

app_name = 'webtoon'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.webtoon_list, name='webtoon-list'),
    path('detail/<int:pk>/', views.webtoon_detail, name='webtoon-detail'),
    path('search/', views.search_list, name='search-list'),
    path('save/<int:webtoon_id>/<str:title>/', views.save_webtoon, name='save-webtoon'),
]