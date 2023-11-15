from django.forms import ModelForm
from aluno.models import Cidade

class CidadeForm(ModelForm):
    class Meta:
        model = Cidade
        fields = '__all__'
