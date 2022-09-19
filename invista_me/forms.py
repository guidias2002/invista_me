from django.forms import ModelForm
from .models import Investimento


class InvestimentoForm(ModelForm):
    class Meta:
        model = Investimento
        # selecinando todos os campos do banco de dados
        fields = '__all__'
