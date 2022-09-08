# FORUMS URL.PY
from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ListForums.as_view(), name='all'),
    path("new/", views.CreateForum.as_view(), name='create'),
    path("detail/<slug>", views.SingleForum.as_view(), name='single'),
    path('new_post/', views.CreatePost.as_view(), name='createpost'),
]
