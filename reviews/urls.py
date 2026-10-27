from django.urls import path
from .views import (
    ReviewListView,
    ReviewDetailView,
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView,
)

urlpatterns = [
    path('', ReviewListView.as_view(), name='review-list'),
    path('create/', ReviewCreateView.as_view(), name='review-create'),
    path('<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('<int:pk>/edit/', ReviewUpdateView.as_view(), name='review-update'),
    path('<int:pk>/delete/', ReviewDeleteView.as_view(), name='review-delete'),
]