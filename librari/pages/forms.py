from django import forms

class Search(forms.Form):
    searchText = forms.CharField(max_length=100)
    fields = ['searchText']

    def __init__(self, *args, **kwargs):
        super(Search, self).__init__(*args, **kwargs)
        self.fields['searchText'].widget.attrs\
            .update({
            'placeholder': 'Search book',
            'class': 'search_input'
        })
    def clean(self):
        cleaned_data = super().clean()