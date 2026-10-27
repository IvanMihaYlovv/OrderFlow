from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'product',
            'author',
            'rating',
            'description',
        ]

        labels = {
            'description': 'Comment',
        }

        help_texts = {
            'rating': 'From 1 to 5.',
        }

        widgets = {
            'author': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'rating': forms.NumberInput(attrs={'placeholder': '1 - 5', 'min': 1, 'max': 5}),
            'description': forms.Textarea(attrs={'placeholder': 'What do you think about the product?'}),
        }

    def clean_author(self):
        name = self.cleaned_data['author'].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                'Author must contain at least 2 characters.'
            )

        return name

    def clean_rating(self):
        rating = self.cleaned_data['rating']

        if rating < 1 or rating > 5:
            raise forms.ValidationError(
                'Rating must be between 1 and 5.'
            )

        return rating

    def clean_description(self):
        description = self.cleaned_data['description'].strip()

        if len(description) < 10:
            raise forms.ValidationError(
                'description must contain at least 10 characters.'
            )

        return description