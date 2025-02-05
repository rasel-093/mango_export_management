from django import forms
from .models import MangoExport

# class MangoExportForm(forms.ModelForm):
#     class Meta:
#         model = MangoExport
#         fields = ['variety', 'description', 'price']

#     def clean_variety(self):
#         variety = self.cleaned_data.get('variety')
#         if MangoExport.objects.filter(variety=variety).exists():
#             raise forms.ValidationError("This variety already exists.")
#         return variety

from django.core.exceptions import ValidationError
from .models import MangoExport

class MangoExportForm(forms.ModelForm):
    class Meta:
        model = MangoExport
        fields = ['variety', 'description', 'price']

    def clean_variety(self):
        variety = self.cleaned_data['variety']
        order_id = self.instance.order_id  # Get the current object's order_id

        # Check for uniqueness, but exclude the current record
        if MangoExport.objects.filter(variety=variety).exclude(order_id=order_id).exists():
            raise ValidationError("This variety already exists.")
        return variety
