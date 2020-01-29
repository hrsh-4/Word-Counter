from django.forms import ModelForm
from .models import URLInformation

class URLForm(ModelForm):
	class Meta:
		model = URLInformation
		fields = ['url']
