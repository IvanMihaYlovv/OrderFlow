from django import forms

from catalog.models import Material, Category, Product


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        exclude = ('id','created_at')

        labels = {
            'is_available': 'Available',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Oak wood'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write something about the material...'}),
        }


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('id','created_at')

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Tables'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write something about the category...'}),
        }


class ProductForm(forms.ModelForm):
    created_at = forms.DateTimeField(required=False, disabled=True, label='Created at')

    class Meta:
        model = Product
        exclude = ('id',)

        labels = {
            'name': 'Product name',
            'price': 'Price (EUR)',
            'is_available': 'Available',
        }

        help_texts = {
            'price': 'Price must be greater than 0.',
            'materials': 'Choose one or more materials.',
        }

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g. Wooden table'}),
            'description': forms.Textarea(attrs={'placeholder': 'At least 10 characters...'}),
            'price': forms.NumberInput(attrs={'placeholder': 'e.g. 149.99'}),
            'materials': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['created_at'].initial = self.instance.created_at
        else:
            del self.fields['created_at']

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        if len(name) < 3:
            raise forms.ValidationError(
                'Product name must contain at least 3 characters.'
            )

        return name

    def clean_price(self):
        price = self.cleaned_data['price']

        if price <= 0:
            raise forms.ValidationError(
                'Price must be greater than zero.'
            )

        return price

    def clean_description(self):
        description = self.cleaned_data['description'].strip()

        if len(description) < 10:
            raise forms.ValidationError(
                'Description must contain at least 10 characters.'
            )

        return description
