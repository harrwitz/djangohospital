from django.forms import ModelForm
from .models import appointments


class Appoform(ModelForm):
	class Meta:
		model = appointments
		fields = '__all__'
