from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import InquiryForm
from .models import Inquiry
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class InquiriesList(ListView):
    model = Inquiry
    context_object_name = 'inquiries'
    template_name = 'orders/inquiries_list.html'
    paginate_by = 7



class InquiryDetailView(DetailView):
    model = Inquiry
    context_object_name = 'inquiry'
    template_name = 'orders/inquiry_detail.html'


class InquiryCreateView(CreateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'orders/inquiry_form.html'
    success_url = reverse_lazy('inquiries')


class InquiryUpdateView(UpdateView):
    model = Inquiry
    form_class = InquiryForm
    template_name = 'orders/inquiry_form.html'
    success_url = reverse_lazy('inquiries')


class InquiryDeleteView(DeleteView):
    model = Inquiry
    context_object_name = 'inquiry'
    success_url = reverse_lazy('inquiries')
    template_name = 'orders/inquiry_confirm_delete.html'

