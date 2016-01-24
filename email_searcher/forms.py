from django import forms


class nameSearcher(forms.Form):
    first_name = forms.CharField(label='Person First Name',min_length=1,required=True)
    last_name = forms.CharField(label='Person Last Name',min_length=1,required=True)
    company_domain = forms.CharField(label='Company Domain',required=True)
