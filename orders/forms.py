from django import forms
from orders.models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'customer_name',
            'customer_email',
            'customer_phone',
            'product',
            'description',
            'desired_quantity',
        ]

        labels = {
            'customer_name': 'Your name',
            'customer_email': 'Email',
            'customer_phone': 'Phone number',
        }

        help_texts = {
            'desired_quantity': 'How many pieces do you need?',
        }

        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'e.g. Ivan Ivanov'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'e.g. ivan@mail.com'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': 'e.g. 0888123456'}),
            'description': forms.Textarea(attrs={'placeholder': 'Tell us what you need (at least 10 characters)...'}),
            'desired_quantity': forms.NumberInput(attrs={'placeholder': 'e.g. 5'}),
        }

    def clean_customer_name(self):
        name = self.cleaned_data['customer_name'].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                'Name must contain at least 3 characters.'
            )

        return name

    def clean_customer_phone(self):
        phone = self.cleaned_data['customer_phone'].strip()

        if len(phone) < 7:
            raise forms.ValidationError(
                'Phone number must contain at least 7 characters.'
            )

        return phone

    def clean_desired_quantity(self):
        quantity = self.cleaned_data['desired_quantity']

        if quantity < 1:
            raise forms.ValidationError(
                'Quantity must be at least 1.'
            )

        return quantity

    def clean_description(self):
        description = self.cleaned_data['description'].strip()

        if len(description) < 10:
            raise forms.ValidationError(
                'Description must contain at least 10 characters.'
            )

        return description

