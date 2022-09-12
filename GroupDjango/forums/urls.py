# FORUMS URL.PY
from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ListForums.as_view(), name='all'),
    path("new/", views.CreateForum.as_view(), name='create'),
    path("update/", views.CreateForum.as_view(), name='update'),
    path("detail/<pk>/", views.SingleForum.as_view(), name='single'),
    path('detail/<pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),
]
