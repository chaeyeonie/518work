from django import forms

class SearchingForm(forms.Form):
    qeury = forms.CharField()

    def clean_query(self):
        data = self.cleaned_data['renewal_data']
        return data
    