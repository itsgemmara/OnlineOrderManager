from django import forms

from .models import Menu, Pay


class OrderForm(forms.ModelForm):
    menu = Menu.objects.all()

    class Meta:
        model = Pay
        fields = ['table']

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        for product in self.menu:
            self.fields[product.name] = forms.IntegerField(required=False)
            self.fields[f"_{product.name}_"] = forms.CharField(required=False, widget=forms.Textarea)
