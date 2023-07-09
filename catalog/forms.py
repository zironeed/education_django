from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
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
