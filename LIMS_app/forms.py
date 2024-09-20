from django import forms
from .models import Reader


class ReaderForm(forms.ModelForm):
    class Meta:
        model=Reader
        fields="__all__"
        widget={
            'reader_name':forms.TextInput(attrs={'class':'form-control'}),
            'reader_contact':forms.NumberInput(attrs={'class':'form-control'}),
            'reader_card.no':forms.NumberInput(attrs={'class':'form-control'}),
            'reader_address':forms.TextInput(attrs={'class':'form-control'}),
            'number_of_books':forms.NumberInput(attrs={'class':'form-control'}),
            'Books':forms.TextInput(attrs={'class':'form-control'}),
            'book_taken_at':forms.DateInput(attrs={'class':'form-control'}),
            'book_returned_at':forms.DateInput(attrs={'class':'form-control'}),      
        }

