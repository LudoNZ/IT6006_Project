# FORUMS URL.PY
from django.urls import path
from . import views

app_name = 'forums'

urlpatterns = [
    path('', views.ListForums.as_view(), name='all'),
    path("detail/<pk>/", views.SingleForum.as_view(), name='single'),
    path('selected/<str:user>/',
         views.ListSelectedUserForums.as_view(), name='selected_user'),
    path('unsolved/',
         views.ListSelectedUnsolvedForums.as_view(), name='selected_unsolved'),
    path("new/", views.CreateForum.as_view(), name='create'),
    path("update/<pk>/", views.UpdateForum.as_view(), name='update'),

    path('comment/<pk>/', views.add_comment_to_post,
         name='add_comment_to_post'),
    path('comment/<pk>/remove/', views.comment_remove, name='comment_remove'),
]
