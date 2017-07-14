from django import forms

class twitterForm(forms.Form):
    twitterUserId = forms.CharField(label='twitterUserId', max_length=100)