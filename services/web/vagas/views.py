from django.shortcuts import render
from .forms import CadastroVagasForm

def create_view(request):
    form = CadastroVagasForm()
    return render(request, 'oportunidades_new.html', {'form': form})
