from django import forms
from datetime import datetime
from crispy_forms.helper import FormHelper
from django.urls import reverse_lazy
from crispy_forms.layout import Submit

class RegisterForm(forms.Form):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_action = reverse_lazy('register')
		self.helper.form_method = 'GET'
		self.helper.add_input(Submit('submit','Submit'))
	firstName = forms.CharField()
	lastName = forms.CharField()
	dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','max': datetime.now().date()}))
	email = forms.EmailField()
	userName = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)
