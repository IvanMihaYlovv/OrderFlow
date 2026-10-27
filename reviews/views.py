from reviews.forms import ReviewForm
from reviews.models import Review


from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class ReviewListView(ListView):
    model = Review
    context_object_name = 'reviews'
    template_name = 'reviews/review_list.html'
    paginate_by = 7
    ordering = ['-created_at']


class ReviewDetailView(DetailView):
    model = Review
    context_object_name = 'review'
    template_name = 'reviews/review_detail.html'


class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review-list')


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm
    context_object_name = 'review'
    template_name = 'reviews/review_form.html'
    success_url = reverse_lazy('review-list')


class ReviewDeleteView(DeleteView):
    model = Review
    context_object_name = 'review'
    template_name = 'reviews/review_confirm_delete.html'
    success_url = reverse_lazy('review-list')
