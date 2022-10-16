
from django.urls import path
from .views import *

urlpatterns=[
    path('',PostPageView.as_view(),name='posts'),
    path('new/',AddPostPageView.as_view(),name='add_posts'),
    path('<int:pk>/',PostDetailView.as_view(),name='detail_posts'),
    path('<int:pk>/review/',BookReview.as_view(),name='review'),
    path('<int:pk>/edit',PostEditView.as_view(),name='edit_posts'),
    path('like/<int:pk>/',LikePostView.as_view(),name='posts_like'),
    path('<int:pk>/delete',PostDeleteView.as_view(),name='delete_posts'),
]