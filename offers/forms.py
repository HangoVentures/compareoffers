from django import forms
from .models import Offer

# Render Offer class as form
class Offerform(forms.ModelForm):
	class Meta:
		model = Offer
		fields = '__all__'
		