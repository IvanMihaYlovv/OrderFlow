from django.urls import path
from .views import InquiriesList, InquiryDetailView, InquiryCreateView, InquiryUpdateView, InquiryDeleteView

urlpatterns = [
    path('inquiries/', InquiriesList.as_view(), name='inquiries'),
    path('inquirydetails/<int:pk>', InquiryDetailView.as_view(), name='inquirydetails'),
    path('inquiries/create/',InquiryCreateView.as_view(),name='inquiry-create'),
    path('inquiries/<int:pk>/edit/',InquiryUpdateView.as_view(),name='inquiry-update'),
    path('inquiries/<int:pk>/delete/',InquiryDeleteView.as_view(),name='inquiry-delete'),

]