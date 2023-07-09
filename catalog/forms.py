from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    banned_words = ['казино', 'криптовалют', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'category', 'price',)

    def clean_name(self):
        cleaned_data = str(self.cleaned_data['name'])

        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии товара фигурируют запрещенные слова')

        return cleaned_data

    def clean_description(self):
        cleaned_data = str(self.cleaned_data['description'])

        for word in self.banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании товара фигурируют запрещенные слова')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = "__all__"
