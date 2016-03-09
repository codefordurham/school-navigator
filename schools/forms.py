from django.forms import ModelForm
import schools.models as schools_models

class SchoolProfileForm(ModelForm):
    class Meta:
        model = schools_models.SchoolProfile
        exclude = ('school', 'created_at', 'submitted_at', )
